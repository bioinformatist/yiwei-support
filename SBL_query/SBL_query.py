#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup
from optparse import OptionParser

def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("--domain", dest = "domain",
                        help = "待查询的ISP Domain Name")

    (options, args) = parser.parse_args()

    html = urlopen('https://www.spamhaus.org/sbl/listings/' + options.domain)
    bs_obj = BeautifulSoup(html, 'html.parser')
    ip_list = bs_obj.findAll(width="210")

    for x in ip_list:
        print(x.text)

if __name__ == "__main__":
    main()