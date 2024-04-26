#!/usr/bin/python3
import sys
import urllib.error
import urllib.request
if __name__ == "__main__":

    url = sys.argv[1]
    Rqst = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(Rqst) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
