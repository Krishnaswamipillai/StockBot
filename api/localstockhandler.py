import os
import sys; sys.path.append("../algos/")
from datetime import datetime
from linreg import LinReg

months = {
    'Jan' : 1,'Feb' : 2,'Mar' : 3,'Apr' : 4,'May' : 5,'Jun' : 6,
    'Jul' : 7,'Aug' : 8,'Sep' : 9, 'Oct' : 10,'Nov' : 11,'Dec' : 12}

def convertMonth(month):
    return months[month]

def loadStocks():
    stocks = {}
    days = set()
    directorylist = os.listdir('results8/')

    for i in directorylist:
        print(i)
        loaded = open("results8/" + i, "r").read()
        stocks[i] = eval(loaded)
        stockdays = []

        d = []
        for x in stocks[i]['prices']:
            d.append(x[1].split(" ")[-1] + " " + str(convertMonth(x[1].split(" ")[0])) + " " + x[1].split(" ")[1][:-1])

        days.update(d)


    #move to ordered list
    #add stock price of beginning of list
    returndict = dict.fromkeys(days, {})
    for stock in stocks.keys():
        for price in stocks[stock]['prices']:
            if stock == "AMD":
                print(price[0])
            x = price[1]
            splitted = x.split(" ")
            date = splitted[-1] + " " + str(convertMonth(splitted[0])) + " " + splitted[1][:-1]
            if stock == "AMD":
                print(date)
            date = date.strip()
            if ("2010 1" in date) and (stock == "AMD"):
                returndict[date][stock] = {"price":price[0], "lin30" : None, "lin60" : None, "lin90" : None, "percentageDif" : None}
                print(returndict[date][stock])
            else:
                returndict[date][stock] = {"price":price[0], "lin30" : None, "lin60" : None, "lin90" : None, "percentageDif" : None}
    dictToList = []
    counter = 0
    for i in returndict.keys():
        counter += 1
        dictToList.append((i, returndict[i]))
        if counter % 100 == 0:
            print((i, returndict[i]))
            print("\n\n\n\n")

    returnlist = sorted(dictToList, key=lambda date: datetime.strptime(date[0], "%Y %m %d"))

    return returnlist
