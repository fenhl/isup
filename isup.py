#!/usr/bin/env python3

"""Check whether a domain is up using isup.me

Usage:
  isup <domain>...
  isup -h | --help
  isup --version

Options:
  -h, --help  
"""

__version__ = '1.1.0'

from docopt import docopt
import re
import sys
from urllib.request import urlopen

def isup(domain):
    request = urlopen('http://www.isup.me/' + domain).read()
    if type(request) != type(''):
        request = request.decode('utf-8')
    return bool("It's just you" in request)

def main(domains):
    for domain in domains:
        print('[....] ' + domain, end='\r')
        try:
            print('[ UP ]' if isup(domain) else '[DOWN]')
        except:
            print('[ ?! ]')

if __name__ == '__main__':
    arguments = docopt(__doc__, version='isup ' + __version__)
    main(arguments['<domain>'])
