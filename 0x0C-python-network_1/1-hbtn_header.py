#!/usr/bin/python3
"""
Write a python script that prints the X-Request-Id variable after getting a url
"""
from urllib import request
import sys


if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    with request.urlopen(req) as response:
        print(response.info()['X-Request-Id'])
