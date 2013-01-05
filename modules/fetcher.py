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
    input = input.encode('utf-8')
    urls = extract_link(input)
    for url in urls:
        response = get_link_data(url)
        print response

        if 'error' in response:
            print 'Error fetching %s' % url
        else:
            if response['type'] == 'video':
                if response['title'] != url:
                    jenni.say("Interesting %s %s you got there: %s" % (response['provider_name'], response['type'], response['title']))

print_title.rule = r'.*\s*http[s]?://[^\s<>"]+|www\.[^\s<>"]+'


if __name__ == '__main__':
    print __doc__
