#!/usr/bin/python3
"""this script will take a URL and email address, sends a POST request to the passed URL with the email as a parameter, and will display response body."""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    r = requests.post(url, data={'email': email})
    print(r.text)
