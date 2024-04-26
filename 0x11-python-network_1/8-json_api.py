#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":

    Letter = "" if len(sys.argv) == 1 else sys.argv[1]
    pylod = {"q": Letter}
    Rqst = requests.post("http://0.0.0.0:5000/search_user", data=pylod)
    try:
        response = Rqst.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
