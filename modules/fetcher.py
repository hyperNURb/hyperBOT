#!/usr/bin/env python
"""
fetcher.py - Jenni Fetcher Module
Copyright 2012, Ivan Tatic
"""

import re
import requests


def get_link_data(url):
    data = 'http://noembed.com/embed?url=' + url.strip()
    response = requests.get(data)
    if response.status_code == 200:
        return response.json()
    else:
        print 'Bad request'


def extract_link(input):
    return re.findall(r'http[s]?://[^\s<>"]+|www\.[^\s<>"]+', str(input))


def print_title(jenni, input):
    """Detects paste of YT link and returns title"""
    urls = extract_link(input)
    for url in urls:
        response = get_link_data(url)
        print response
        if 'error' in response:
            print 'Error fetching %s' % url
        else:
            if response['title'] and response['provider_name']:
                jenni.say("Whooa, I <3 %s : %s" % (response['provider_name'], response['title']))

print_title.rule = r'.*\s?http[s]?://[^\s<>"]+|www\.[^\s<>"]+'


if __name__ == '__main__':
    print __doc__
