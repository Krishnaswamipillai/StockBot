import os
import sys; sys.path.append("../algos/")
from datetime import datetime
from linreg import LinReg

months = {
    'Jan' : 1,'Feb' : 2,'Mar' : 3,'Apr' : 4,'May' : 5,'Jun' : 6,
    'Jul' : 7,'Aug' : 8,'Sep' : 9, 'Oct' : 10,'Nov' : 11,'Dec' : 12}

def convertMonth(month):
    return months[month]

def getLinArrays(arr):
    index = len(arr)-1
    arr30 = []
    arr60 = []
    arr90 = []
    counter = 0
    while counter <= 90 and index-counter >= 0:
        arr90.append(arr[index - counter])
        counter += 1
    counter = 0
    while counter <= 60 and index-counter >= 0:
        arr60.append(arr[index - counter])
        counter += 1
    counter = 0
    while counter <= 30 and index-counter >= 0:
        arr30.append(arr[index - counter])
        counter += 1

    return LinReg(arr30), LinReg(arr60), LinReg(arr90)


STOCKDIR = 'results8/'

def loadStocks():
    stocks = {}
    days = set()
    directorylist = os.listdir(STOCKDIR)

    for i in directorylist:
        print(i)
        loaded = open(STOCKDIR + i, "r").read()
        stocks[i] = eval(loaded)
        stockdays = []

        d = []
        for x in stocks[i]['prices']:
            d.append(x[1].split(" ")[-1] + " " + str(convertMonth(x[1].split(" ")[0])) + " " + x[1].split(" ")[1][:-1])

        days.update(d)

    returndict = {}

    for i in days:
        returndict[i] = {}

    for stock in stocks.keys():
        for price in stocks[stock]['prices']:
            x = price[1]
            splitted = x.split(" ")
            date = splitted[-1] + " " + str(convertMonth(splitted[0])) + " " + splitted[1][:-1]
            date = date.strip()
            returndict[date][stock] = {"price":price[0], "lin30" : None, "lin60" : None, "lin90" : None, "percentageDif" : None}

    dictToList = []
    counter = 0
    for i in returndict.keys():
        dictToList.append((i, returndict[i]))

    returnlist = sorted(dictToList, key=lambda date: datetime.strptime(date[0], "%Y %m %d"))

    return returnlist



def process(daystocks, filelist, simday):
    x = simday
    print(x)
    min = x-90
    if min < 0:
        min = 0
    stocks = {}
    daystolinreg = None
    if x + 1 <= len(daystocks):
        daystolinreg = daystocks[min: x]
    else:
        daystolinreg = daystocks[min:]
    for i in filelist:
        stocks[i] = []
    for day in range(len(daystolinreg)-1):
        for stock in daystolinreg[day][1].keys():
            stocks[stock].append(daystolinreg[day][1][stock]['price'])
    for i in stocks.keys():
        try:
            thirty, sixty, ninty = getLinArrays(stocks[i])
            daystocks[x][1][i]['lin30'] = thirty
            daystocks[x][1][i]['lin60'] = sixty
            daystocks[x][1][i]['lin90'] = ninty

        except:
            pass

    return daystocks[x]

def startSimulation(date1, date2):
    filelist = os.listdir(STOCKDIR)

    print("""
    ##########################
    ### STOCK TRADING BOT ####
    ##########################
    """)
    print("starting.")
    print("############################")
    print("#### READING STOCK DATA ####")
    print("############################")
    daystocks = loadStocks()
    print("############################")
    print("#### DONE LOADING STOCK ####")
    print("############################")

    firstIndex = None
    endIndex = None

    for i in range(len(daystocks)-1):
        if daystocks[i][0] == date1:
            firstIndex = i
            print(i)
        elif daystocks[i][0] == date2:
            endIndex = i
            print("triggered")


    daystocks = daystocks[firstIndex:endIndex + 1]
    for i in range(len(daystocks)):
        dayresults = process(daystocks, filelist, i)
