#!/usr/bin/env python3

"""Check whether a domain is up using isup.me

Usage:
  isup <domain>...
  isup -h | --help
  isup --version

Options:
  -h, --help  
"""

__version__ = '1.1.1'

from docopt import docopt
import fancyio
import re
import sys
import threading
from urllib.request import urlopen

class IsupThread(threading.Thread):
    def __init__(self, domain):
        self.domain = domain
        super().__init__()
    
    def run(self):
        try:
            request = urlopen('http://www.isup.me/' + self.domain).read()
            self.progress = 0.8
            if type(request) != type(''):
                request = request.decode('utf-8')
            if "It's just you" in request:
                self.state = ' UP '
            else:
                self.state = 'DOWN'
        except:
            self.state = ' ?! '

def isup(domain):
    request = urlopen('http://www.isup.me/' + domain).read()
    if type(request) != type(''):
        request = request.decode('utf-8')
    return bool("It's just you" in request)

def main(domains):
    with fancyio.IO() as io:
        lines = []
        for domain in domains:
            line = fancyio.TaskLine(io, thread=IsupThread(domain), message=domain)
            line.start()
            lines.append(line)
        for line in lines:
            line.join()
            if line.prefix == ' UP ':
                line.prefix_formatter = io.terminal.green
            elif line.prefix == 'DOWN':
                line.prefix_formatter = io.terminal.red
            io.update()

if __name__ == '__main__':
    arguments = docopt(__doc__, version='isup ' + __version__)
    main(arguments['<domain>'])
