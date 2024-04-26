#!/usr/bin/python3
import sys
import requests

if __name__ == '__main__':

    url = sys.argv[1]
    DATA = {'email': sys.argv[2]}
    Rqst = requests.post(url, DATA)
    print(Rqst.text)
