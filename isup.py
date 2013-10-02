#!/usr/bin/env python3

"""Check whether a domain is up using isup.me

Usage:
  isup <domain>...
  isup -h | --help
  isup --version

Options:
  -h, --help  
"""

from docopt import docopt
import re
import sys
from urllib.request import urlopen

def isup(domain):
    try:
        request = urlopen("http://www.isup.me/" + domain).read()
        if type(request) != type(''):
            request = request.decode('utf-8')
        return bool("It's just you" in request)
    except:
        return False

def main(domains):
    for domain in domains:
        print('[....] ' + domain, end='\r')
        print('[ UP ]' if isup(domain) else '[DOWN]')

if __name__ == '__main__':
    arguments = docopt(__doc__, version='isup 1.0.0')
    main(arguments['<domain>'])
