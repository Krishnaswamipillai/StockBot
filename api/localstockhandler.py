import os
import sys; sys.path.append("../algos/")
from datetime import datetime
from linreg import LinReg

months = {
    'Jan' : 1,'Feb' : 2,'Mar' : 3,'Apr' : 4,'May' : 5,'Jun' : 6,
    'Jul' : 7,'Aug' : 8,'Sep' : 9, 'Oct' : 10,'Nov' : 11,'Dec' : 12}

def convertMonth(month):
    return months[month]

def getLinArrays(index, arr):
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

    returndict = {}

    for i in days:
        returndict[i] = {}

    for stock in stocks.keys():
        print(stock)
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

def processStocks():
    daystocks = loadStocks()

    counter = 1
    for x in range(len(daystocks)):
        min = x-90
        if min < 0:
            min = 0
        daystolinreg = daystocks[min: x]
