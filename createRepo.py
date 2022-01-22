#! /usr/bin/env python3
import os 
import requests
import argparse


# Immutable Variables
GITHUB_TOKEN=os.getenv("TOKEN")
API_URL="https://api.github.com"
headers = {
    "Authorization": "token " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.v3+json"
}
REPO_PATH=os.getenv("PATH")
GITHUB_USER=os.getenv("USER")


# CLI parser
parser = argparse.ArgumentParser()
parser.add_argument("--name", "-n", type=str, dest="name", required=True)
parser.add_argument("--description","-d",type=str,dest="description",required=False)
parser.add_argument("--private", "-p", dest="is_private", action="store_true")


# Arguments
args = parser.parse_args()
repo_name = args.name
description=args.description
is_private = args.is_private


# API Parameters
if is_private and description:
    payload= '{"name": "' + repo_name + '", "description": "' + description + '", "private": true }'
elif description:
    payload= '{"name": "' + repo_name + '", "description": "' + description + '", "private": false }'
elif is_private:
    payload = '{"name": "' + repo_name + '", "private": true }'
else:
    payload = '{"name": "' + repo_name + '", "private": false }'


# Creating The Repository on GitHub
try:
    r = requests.post(API_URL + "/user/repos", data=payload, headers=headers)
    r.raise_for_status()
except requests.exceptions.RequestException as err:
    raise SystemExit(err)


# Adding The Repository locally
try:
    os.chdir(REPO_PATH)
    os.system("mkdir " + repo_name)
    os.chdir(REPO_PATH + repo_name)
    os.system("git init")
    os.system("git remote add origin git@github.com:" + GITHUB_USER + "/" + repo_name + ".git")
    os.system("echo '# " + repo_name + "' >> README.md")
    os.system("git add . && git commit -m 'Initial Commit' && git push origin master")
except FileExistsError as err:
    raise SystemExit(err)


    

