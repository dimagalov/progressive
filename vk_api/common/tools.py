# -*- coding: utf8 -*-

__author__ = 'dimagalov'

import time
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


def open_url(url):
    request = Request(url)
    try:
        response = urlopen(request)
    except HTTPError as error:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', error.code)
    except URLError as error:
        print('We failed to reach a server.')
        print('Reason: ', error.reason)
    else:
        return response.read()


def cook_soup_from_url(url):
    try:
        html = open_url(url)
    except:
        print('Couldn\'t get html code of the page while cooking soup')
    else:
        try:
            soup = BeautifulSoup(html)
        except:
            print('Something went wrong when we were cooking your soup')
        else:
            return soup


def cook_soup_from_html(html):
    try:
        soup = BeautifulSoup(html)
    except:
        print('Something went wrong when we were cooking your soup')
    else:
        return soup


def get_current_timestamp():
    return int(time.time())
