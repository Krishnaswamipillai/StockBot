#!/usr/bin/env python3
import cgi
import cgitb; cgitb.enable()
import stocks

arguments = cgi.FieldStorage()
ticker = None
for i in arguments.keys():
    if i == "ticker":
        ticker = arguments[i].value

print("Content-Type: text/html\n\n" + stocks.getCurrentStockPrice(ticker))
