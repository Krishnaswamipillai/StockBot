#!/usr/bin/env python3
import urllib3
import time
from datetime import date, datetime
import math
from bs4 import BeautifulSoup;
import concurrent.futures
letters = list("abcdefghijklmnopqrstuvwxyz")
import cProfile

http = urllib3.PoolManager()
startDate = None
endDate = None
ticker = None

def truncate(number, values=3):
    d = str(number)
    decimalLocation = d.index(".")
    if len(d[decimalLocation:-1]) >= values + 1:
        return float(d[0:decimalLocation + values + 1])
    else:
        return float(number)


#
#First data point is always day up
#  "%5EGSPC" is SP500
#

def getTickers():
    tickers = []
    r = http.request('GET', "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    #Mostly up to date list on wikipedia with al stocks in SP500
    soup = BeautifulSoup(r.data, "html.parser")
    for i in soup.find_all("table")[0]:
        for x in i:
            for y in x:
                if "nofollow" in str(y):
                    #Finds the correct tag within the html -- contains the data
                    ticker = str(y).split(">")[1].split("<")[0]
                    if "reports" not in ticker:
                        tickers.append(ticker.replace(".", "-"))
    return tickers

def getCurrentStockPrice(ticker):
    r = http.request('GET', "https://finance.yahoo.com/quote/" + ticker)
    #Figured out yahoo's url structure, replaces necessary parts with what i need
    soup = BeautifulSoup(r.data, "html.parser")

    inputTag = soup.find_all("span")
    print(inputTag)
    realOptions = []

    #print(inputTag)
    for x in inputTag:
        i = str(x)
        print(i)
        if "<script" not in i[0:13]:
            if '<span class="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)" data-reactid="35">' in i:
                #The ellement with this text in it was found to contain the data I'm looking for
                realOptions.append(i)

    return realOptions[-1].split(">")[1].split("<")[0]


def getHistoricalData(ticker, startDate, endDate):
    def dateToEpoch(date):
        date_time = date
        pattern = '%d.%m.%Y'
        return int(time.mktime(time.strptime(date_time, pattern)))
        #Converts a calender date into epoch dates

    def daysBetween(day1, day2):
        pattern = '%d.%m.%Y'
        return (datetime.strptime(day1, pattern) - datetime.strptime(day2, pattern)).days
        #Returns the number of days between two dates

    startEpoch = dateToEpoch(startDate) + 8640000
    #Adds overlap in the stock data requests to make sure it has everything
    endEpoch = startEpoch - 86400 * 100
    days = daysBetween(startDate, endDate)
    returnValues = []
    dates = []

    print(int(math.ceil(days/100)) + 1)
    #Yahoo requires you to ask it to load more than 100 days, but that requires user interaction.
    #Instead, i split the requests into multiple 100 day requests
    for i in range(int(math.ceil(days)/100) + 1):
        startEpoch -= (86400 * 100)
        endEpoch -= (86400 * 100)
        #86400 is one day in epoch time

        print(startEpoch, endEpoch)

        url = "https://finance.yahoo.com/quote/" + ticker + "/history?period1=" + str(endEpoch) +"&period2=" + str(startEpoch) + "&interval=1d&filter=history&frequency=1d"
        #Yahoo url format takes in the epoch in place of actual dates

        print(url)
        r = http.request('GET', url)
        soup = BeautifulSoup(r.data, "html.parser")
        inputTag = soup.findAll()
        realOptions = []
        for x in inputTag:
            i = str(x)
            if "<script" not in i[0:13]:
                if 'tbody data-reactid="50"' in i and len(i) > 10:
                    #This is where the data is kept
                    realOptions.append(x)
        values = []
        counter = 0
        for i in realOptions[-1].findAll('tr'):
            epoch = datetime(1970, 1, 1)

            date = str(i.findAll('span')[0]).split(">")[1].split("<")[0]
            #Gets data between html tags : "<html> THIS IS THE DATA </html>" would return "THIS IS THE DATA"
            mydt = datetime.strptime(date, '%b %d, %Y')

            val = int((mydt - epoch).total_seconds())
            if val < dateToEpoch(startDate) and val > dateToEpoch(endDate) and str(mydt) not in dates:
                #Makes sure the data for that date hasn't already been retrieved, and that it is within the asked for dates
                dates.append(str(mydt))
                passed = True
                for x in letters:
                    if x in str(i.findAll('span')[-2]).split(">")[1].split("<")[0]:
                        passed = False
                if passed == True:
                    returnValues.append(truncate(float(str(i.findAll('span')[-2]).split(">")[1].split("<")[0].replace(",", ""))))
            counter += 1

    print(len(returnValues))
    return returnValues#[0:-(100-(days%100))]


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def fetchSP500():
    startEpoch = "1.1.2018"
    endEpoch = "1.1.2000"
    sp500index = getHistoricalData("%5EGSPC", startEpoch, endEpoch)
    #Fetches sp500 prices to compare against
    print(sp500index)
    tickers = getTickers()
    spPercentages = [truncate(100 * (b - a) / a) for a, b in zip(sp500index[::1], sp500index[1::1])]
    #Calculates daily percentage change
    print(spPercentages)
    results = {}

    def process(i):
        results[i] = {"prices" : getHistoricalData(i, startEpoch, endEpoch)}
        #Gets prices
        print(len(results[i]['prices']))

        """
        results[i]['percentages'] = [truncate(100 * (b - a) / a) for a, b in zip(results[i]["prices"][::1], results[i]["prices"][1::1])]
        #Calculates daily change
        differences = []
        counter = 0
        for x in results[i]['percentages']:
            differences.append(truncate(x - spPercentages[counter]))
            #Calculates daily % change vs sp500
            counter += 1


        results[i]['differentPercentages'] = differences
        """

        #print(results[i])
        print(i + "\n\n\n\n")
    for i in tickers:
        process(i)

    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        #Fetches 5 stocks at once, goes through list of stock tickers
        future_to_url = {executor.submit(process, url): url for url in tickers}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except:
                pass
    #writes it all to a file
    f = open('sp500stocks18y', 'w+')
    f.write(str(results))
    f.close()

def reorder():
    #Dayn { "Ticker" : {"prices":[(pO, pC)], "relPercentChange" : []}}
    #                            [Dayn-100 -> Dayn]
    pass
