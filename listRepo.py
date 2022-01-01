#! /usr/bin/env python3
import os
import requests
import argparse
import webbrowser
from simple_term_menu import TerminalMenu


# Immutable Variables
API_URL="https://api.github.com"
headers = {
    "Accept": "application/vnd.github.v3+json"
}
GITHUB_USER=os.getenv("USER")

# CLI parser
parser = argparse.ArgumentParser()
parser.add_argument("--user", "-u", type=str, dest="user", required=False)


# Arguments
args = parser.parse_args()
user = args.user

# Storing Data From The API
data=[]
options=["Quit"]
if user:
    try:
        r = requests.get(f"{API_URL}/users/{user}/repos", headers=headers)
        for i in r.json():
            json_data={
                i["name"]:i["html_url"]   
            }
            data.append(json_data)
            
        
        # Functionality of the Options
        for j in r.json():
            options.append(j["name"])

        mainMenu=TerminalMenu(options)
        quitting=False

        while quitting == False:
            optionsIndex = mainMenu.show()
            optionsChoice=options[optionsIndex]

            if optionsChoice == "Quit":
                quitting = True
            
            for option in data:
                key,value = list(option.items())[0]
                if key == optionsChoice:
                    print(value)
                    webbrowser.open(value, new=0, autoraise=True)
                    quitting= True
                
    except Exception as e:
          print(e)
else:
    try:
        r = requests.get(f"{API_URL}/users/{GITHUB_USER}/repos", headers=headers)
        for i in r.json():
            json_data={
                i["name"]:i["html_url"]   
            }
            data.append(json_data)
        
        # Functionality of the Options
        for j in r.json():
            options.append(j["name"])

        mainMenu=TerminalMenu(options)
        quitting=False

        while quitting == False:
            optionsIndex = mainMenu.show()
            optionsChoice=options[optionsIndex]

            if optionsChoice == "Quit":
                quitting = True
            
            for option in data:
                key,value = list(option.items())[0]
                if key == optionsChoice:
                    print(value)
                    webbrowser.open(value, new=0, autoraise=True)
                    quitting= True
    except Exception as e:
          print(e)
