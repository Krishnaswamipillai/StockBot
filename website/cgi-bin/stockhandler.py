#!/usr/bin/env python3
import stocks
import cgi


print('here')
arguments = cgi.FieldStorage()
print('after')
ticker = None
def main():
    f = open('testingtesting','w')

    for i in arguments.keys():
        if i == "ticker":
            ticker = arguments[i].value

    print("Content-Type: text/html\n\n" + stocks.getCurrentStockPrice(ticker))

main()