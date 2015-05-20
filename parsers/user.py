# -*- coding: utf8 -*-

__author__ = 'dimagalov'

from common.models import User
from common.tools import cook_soup_from_url, get_current_timestamp


def get_user_id(soup):
    try:
        return soup.find("a", class_="anchor")["name"].split('_')[0][4:]
    except:
        print("Problem occured while getting user id")


def get_user_name(soup):
    try:
        return soup.find("h2", class_="op_header").text
    except:
        print("Problem occured while getting user name")


def get_friends_amount(soup):
    try:
        return "None"
    except:
        print("Problem occured while getting user friends amount")


def get_subscribers_amount(soup):
    try:
        info = soup.find_all("a", class_="pm_item")
        for info_item in info:
            if info_item.text[:10] == "Подписчики":
                friends_amount = info_item.text[10:].replace(" ", "").strip()
                return friends_amount
    except:
        print("Problem occured while getting subscribers amount")


def parse_user_page(url):
    soup = cook_soup_from_url(url)

    user_id = get_user_id(soup)
    user_name = get_user_name(soup)
    timestamp = get_current_timestamp()
    friends_amount = get_friends_amount(soup)
    subscribers_amount = get_subscribers_amount(soup)

    user = User(user_id, user_name, timestamp, friends_amount, subscribers_amount)
    print(user)
