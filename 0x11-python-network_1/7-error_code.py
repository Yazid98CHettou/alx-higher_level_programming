#!/usr/bin/python3
import sys
import requests
if __name__ == "__main__":

    url = sys.argv[1]
    Rqst = requests.get(url)
    if Rqst.status_code >= 400:
        print("Error code: {}".format(Rqst.status_code))
    else:
        print(Rqst.text)
