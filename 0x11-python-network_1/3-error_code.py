#!/usr/bin/python3
"""this code will take  a URL, send a request to the URL and display the body of the response (decoded in utf-8)."""

import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]

    own_request = request.Request(url)
    try:
        with request.urlopen(own_request) as response:
            print(response.read().decode("ascii"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
