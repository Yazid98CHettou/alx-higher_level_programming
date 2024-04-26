#!/usr/bin/python3
import sys
import urllib.request
if __name__ == "__main__":
    url = sys.argv[1]
    Rqst = urllib.request.Request(url)
    with urllib.request.urlopen(Rqst) as response:
        print(dict(response.headers).get("X-Request-Id"))
