#!/usr/bin/env python3
import re
import sys
from urllib.request import urlopen

def isup(domain):
    request = urlopen("http://www.isup.me/" + domain).read()
    if type(request) != type(''):
        request = request.decode('utf-8')
    return domain + " " + ("UP" if "It's just you" in request else "DOWN")

def main(cmd, args):
    if len(args):
        for d in args:
            print(isup(d))
    else:
        print("usage: " + cmd + " domain1 [domain2 .. domainN]")

if __name__ == '__main__':
    main(sys.argv[0], sys.argv[1:] if len(sys.argv) > 1 else [])
