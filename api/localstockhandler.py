import os
from datetime import datetime

months = {
    'Jan' : 1,'Feb' : 2,'Mar' : 3,'Apr' : 4,'May' : 5,'Jun' : 6,
    'Jul' : 7,'Aug' : 8,'Sep' : 9, 'Oct' : 10,'Nov' : 11,'Dec' : 12}

def convertMonth(month):
    return months[month]

stocks = {}
days = set()
directorylist = os.listdir('results8/')
def loadStocks():
    for i in directorylist:
        print(i)
        loaded = open("results8/" + i, "r").read()
        stocks[i] = eval(loaded)
        stockdays = []

        d = [x[1].split(" ")[-1] + " " + str(convertMonth(x[1].split(" ")[0])) + " " + x[1].split(" ")[1][:-1] for x in stocks[i]['prices']]
        days.update(d)

    return dict.fromkeys(days, key=lambda date: datetime.strptime(date, "%Y %m %d"), dict.fromkeys(directorylist, None))
