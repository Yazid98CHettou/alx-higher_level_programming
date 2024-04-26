#!/usr/bin/python3
import sys
import urllib.parse
import urllib.request
if __name__ == "__main__":

    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    DATA = urllib.parse.urlencode(value).encode('ascii')

    Rqst = urllib.request.Request(url, DATA)
    with urllib.request.urlopen(Rqst) as response:
        print(response.read().decode('utf-8'))
