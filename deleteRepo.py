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
GITHUB_USER=os.getenv("USER")

# CLI parser
parser = argparse.ArgumentParser()
parser.add_argument("--repo", "-r", type=str, dest="repo", required=True)


# Arguments
args = parser.parse_args()
repo = args.repo


# Deleting The Repository
try:
    r = requests.delete(f"{API_URL}/repos/{GITHUB_USER}/{repo}", headers=headers)
    r.raise_for_status()
except requests.exceptions.RequestException as err:
    raise SystemExit(err)
