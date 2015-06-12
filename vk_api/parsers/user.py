# -*- coding: utf8 -*-

__author__ = 'dimagalov'

from common.tools import vk_api_authorization
from common.models import User
from common.tools import get_current_timestamp


def get_user_id(user):
    try:
        return str(user["id"])
    except:
        print("Problem occured while getting user id")


def get_user_name(user):
    try:
        return user["first_name"] + " " + user["last_name"]
    except:
        print("Problem occured while getting user name")


def get_friends_amount(vk_api, user):
    try:
        id = int(get_user_id(user))
        friends = vk_api.friends.get(user_id=id)
        return friends["count"]
    except:
        print("Problem occured while getting user friends amount")


def get_subscribers_amount(user):
    try:
        return user["followers_count"]
    except:
        print("Problem occured while getting subscribers amount")


def get_user_link(user):
    try:
        return "https://vk.com/id" + get_user_id(user)
    except:
        print("Problem occured while getting user link")


def parse_user(vk_api, user):
    id = get_user_id(user)
    name = get_user_name(user)
    timestamp = get_current_timestamp()
    friends_amount = get_friends_amount(vk_api, user)
    subscribers_amount = get_subscribers_amount(user)
    link = get_user_link(user)

    parsed_user = User(id=id, name=name, timestamp=timestamp,
                       friends_amount=friends_amount, link=link,
                       subscribers_amount=subscribers_amount)

    print(parsed_user)

    return parsed_user


def parse_user_pages(user_ids):
    vk_api = vk_api_authorization()

    users = vk_api.users.get(
        user_ids=user_ids,
        fields=["followers_count"])

    parsed_users = [parse_user(vk_api, user) for user in users]

    return parsed_users
