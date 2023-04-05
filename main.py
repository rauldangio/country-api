import json
from argparse import ArgumentParser

import requests as re

URL = "https://restcountries.com/v3.1/all"
URL_NAME = "https://restcountries.com/v3.1/name/"


def reqWeb(url):
    try:
        req = re.get(url)
        if req.status_code == 200:
            return req.text
    except Exception as error:
        print(error)
    
    return None

def parsing(text):
    try:
        return json.loads(text) 
    except Exception as error:
        print(error)


def language(country):
    resp = re.get(URL_NAME + country)
    list_country = json.loads(resp.text)
    for country in list_country:
        print(f"{country['name']['common']} --> {country['languages']}")


def capital(country):
    resp = re.get(URL_NAME + country)
    list_country = json.loads(resp.text)
    for country in list_country:
        print(f"{country['name']['common']} --> {country['capital'][0]}")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-l", help="return the language of the country")
    parser.add_argument("-c", help="return the capital of the country")
    args = parser.parse_args()
    if(args.l):
        print("LANGUAGES")
        language(args.l)
        print()
        print("----------------------")
    if(args.c):
        print("CAPITAL")
        capital(args.c)
        print()
        print("----------------------")
    