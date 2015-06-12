# -*- coding: utf8 -*-

__author__ = 'dimagalov'

import vk_api
import time
from datetime import datetime
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
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


def captcha_handler(captcha):
    key = input("Enter Captcha {0}: ".format(captcha.get_url())).strip()
    return captcha.try_again(key)


def vk_api_authorization():
    app_id, login, password = 4949093, "+79652475643", "lalka228"
    vk = vk_api.VkApi(login=login, password=password, app_id=app_id,
                      captcha_handler=captcha_handler)

    try:
        vk.authorization()
    except vk_api.AuthorizationError as error_message:
        print(error_message)
        return

    return vk
