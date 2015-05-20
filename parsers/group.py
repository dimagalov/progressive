# -*- coding: utf8 -*-

__author__ = 'dimagalov'

from common.models import Group
from common.tools import cook_soup_from_url, get_current_timestamp


def get_group_id(soup):
    try:
        info = soup.find("a", class_="anchor")["name"]
        return info.split('_')[0][4:].replace("-", "")
    except:
        print("Problem occured while getting group id")


def get_group_name(soup):
    try:
        return soup.find("h2", class_="op_header").text
    except:
        print("Problem occured while getting group name")


def get_subscribers_amount(soup):
    try:
        info = soup.find_all("a", class_="pm_item")
        for info_item in info:
            if info_item.text[:10] == "Подписчики":
                subscribers_amount = info_item.text[10:]
                return subscribers_amount.replace(" ", "").strip()
    except:
        print("Problem occured while getting subscribers amount")


def get_group_link(soup):
    try:
        return "https://vk.com/public" + get_group_id(soup)
    except:
        print("Problem occured while getting group link")


def parse_group_page(url):
    soup = cook_soup_from_url(url)

    group_id = get_group_id(soup)
    group_name = get_group_name(soup)
    timestamp = get_current_timestamp()
    subscribers_amount = get_subscribers_amount(soup)
    group_link = get_group_link(soup)

    group = Group(group_id, group_name, timestamp,
                  subscribers_amount, group_link)
    print(group)
