#!/usr/bin/python3
import urllib.request
if __name__ == "__main__":

    Rqst = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(Rqst) as response:
        the_page = response.read()
        print('Body response:')
        print("\t- type: {}".format(type(the_page)))
        print("\t- content: {}".format(the_page))
        print("\t- utf8 content: {}".format(the_page.decode('utf-8')))
