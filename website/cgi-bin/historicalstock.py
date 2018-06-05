#!/usr/bin/env python3
import stocks
import cgi
import json

STOCKDIR = "../api/results20/"

print('here')
arguments = cgi.FieldStorage()
print('after')
ticker = None
def main():
    for i in arguments.keys():
        if i == "ticker":
            ticker = arguments[i].value
            
    f = eval(open(STOCKDIR + ticker, 'r').read())
    print("Content-Type: text/html\n\n" + json.dumps(f['prices']))
    
main()
