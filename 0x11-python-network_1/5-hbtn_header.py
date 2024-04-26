#!/usr/bin/python3
import sys
import requests

if __name__ == '__main__':

    url = sys.argv[1]
    Rqst = requests.get(url)
    print(Rqst.headers.get("X-Request-Id"))
