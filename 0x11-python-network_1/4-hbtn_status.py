#!/usr/bin/python3
import requests

if __name__ == '__main__':

    Rqst = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(Rqst.text)))
    print("\t- content: {}".format(Rqst.text))
