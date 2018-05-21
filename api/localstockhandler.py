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

        d = [x[1].split(" ")[-1] + " " + str(convertMonth(x[1].split(" ")[0])) + " " + x[1].split(" ")[1][:-1] for x in stocks[i]['prices']]
        days.update(d)


    #move to ordered list
    #add stock price of beginning of list
    returndict = dict.fromkeys(days, [])
    print(returndict)
    for stock in stocks.keys():
        for price in stocks[stock]['prices']:
            x = price[1]
            print(price[0])
            splitted = x.split(" ")
            date = splitted[-1] + " " + str(convertMonth(splitted[0])) + " " + splitted[1][:-1]
            returndict[date].append({stock: price[0], "lin30" : None, "lin60" : None, "lin90" : None, "percentageDif" : None})

    counter = 0
    for i in returndict.keys():
        if counter % 20 == 0:
            #print(returndict[i], counter)
            pass
        counter += 1
