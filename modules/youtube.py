#!/usr/bin/env python
"""
youtube.py - Jenni Twitter Module
Copyright 2012, Ivan Tatic
"""

import re
import web

rYTlink = re.compile(r'.*\s?(https?://)?(www\.)?(youtube\.(\w*)/watch\?v=|youtu.be/)([-\w]+)(\s)*')
rYTtitle = r'<title>(.+)</title>'


def get_yt_data(vid):
    data = 'https://gdata.youtube.com/feeds/api/videos/' + vid + '?v=2'
    response = web.get(data)
    return response


def get_yt_title(jenni, input):
    """Detects paste of YT link and returns title"""
    vid = rYTlink.match(input).group(5)
    if vid:
        data = get_yt_data(vid)
        title = re.search(rYTtitle, data)
        jenni.say(title.group(1))

get_yt_title.rule = r'.*\s?(https?://)?(www\.)?(youtube\.(\w*)/watch\?v=|youtu.be/)([-\w]+)'


if __name__ == '__main__':
    print __doc__
