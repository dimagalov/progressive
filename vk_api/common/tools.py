# -*- coding: utf8 -*-

__author__ = 'dimagalov'

import vk
import time
import datetime
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


def get_current_timestamp():
    return int(time.time())


def timestamp_to_date(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


def vk_api_authorization():
    app_id, login, password = 4949093, input(), input()
    vk_api = vk.API(app_id, login, password)
    return vk_api
