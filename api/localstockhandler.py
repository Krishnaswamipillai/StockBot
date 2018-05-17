import os

months =
    {
    'Jan' : 1,'Feb' : 2,'Mar' : 3,'Apr' : 4,'May' : 5,'Jun' : 6,'Jul' : 7,
    'Aug' : 8,'Sep' : 9, 'Oct' : 10,'Nov' : 11,'Dec' : 12
    }
    
def convertMonth(month):
    return months[month]

stocks = {}
days = set()
def loadStocks():
    for i in os.listdir('results/'):
        print(i)
        loaded = open("results/" + i, "r").read()
        stocks[i] = eval(loaded)
        stockdays = []

        d = [x[1].split(" ")[-1] + " " + str(convertMonth(x[1].split(" ")[0])) + " " + x[1].split(" ")[1][:-1] for x in stocks[i]['prices']]
        print(d)
        changed = False
        for x in d:
            if x not in days:
                days.append(d)
                changed = True
        print(len(days))

    days.sort(key=lambda date: datetime.strptime(date, "%Y-%m-%d"))
    print(days)
