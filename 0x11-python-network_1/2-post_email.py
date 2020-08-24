#!/usr/bin/python3
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv
"""Takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
"""


if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}
    data = urlencode(values)
    data = data.encode('ascii')
    req = Request(url, data)
    with urlopen(req) as response:
        read = response.read()
        print(read.decode("UTF-8"))
