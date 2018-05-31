#!/usr/bin/env python3
from google.oauth2 import id_token
from google.auth.transport import requests
import cgi
import json

# (Receive token by HTTPS POST)
# ...
arguments = cgi.FieldStorage()

userdata = None
returnData = {}
database = json.load(open("../database.json"))
print(type(database))
print(database)

def verifyUser():
    intent = None

    token = None;
    for i in arguments.keys():
        if i == "clientId":
            token = arguments[i].value
        if i == "newStock":
            intent = "createStock"
                
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), "400909393742-fagoekann6vpms68vsmjdtohvisdsrlj.apps.googleusercontent.com")
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            print('vauleerror')
            raise ValueError('Wrong issuer.')

        userid = idinfo['sub']
        
        returnData["userdata"] = idinfo
        if idinfo['email'] in database['users'].keys():
            if intent == "createStock":
                database['users'][idinfo['email']][arguments["newStock"].value] = arguments["number"].value
                
            returnData["stocks"] = database['users'][idinfo['email']]
        
        else:
            database['users'][idinfo['email']] = {}
            
            if intent == "createStock":
                database['users'][idinfo['email']][arguments["newStock"].value] = arguments["number"].value
                
            returnData["stocks"] = database['users'][idinfo['email']]
            
        print("Content-Type: text/html\n\n" + json.dumps(returnData))
        open("../database.json", "w").write(json.dumps(database))
        
    except ValueError:
        # Invalid token
        pass

verifyUser();