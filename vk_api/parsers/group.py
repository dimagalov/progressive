# -*- coding: utf8 -*-

__author__ = 'dimagalov'

from common.tools import vk_api_authorization
from common.models import Group
from common.tools import get_current_timestamp


def get_group_id(group):
    try:
        return str(group["id"])
    except:
        print("Problem occured while getting group id")


def get_group_name(group):
    try:
        return group["name"]
    except:
        print("Problem occured while getting group name")


def get_subscribers_amount(group):
    try:
        return group["members_count"]
    except:
        print("Problem occured while getting subscribers amount")


def get_group_verified(group):
    try:
        return group["verified"]
    except:
        print("Problem occured while getting group verification")


def get_group_link(group):
    try:
        return "https://vk.com/club" + get_group_id(group)
    except:
        print("Problem occured while getting group link")


def parse_group(group):
    id = get_group_id(group)
    name = get_group_name(group)
    timestamp = get_current_timestamp()
    subscribers_amount = get_subscribers_amount(group)
    verified = get_group_verified(group)
    link = get_group_link(group)

    parsed_group = Group(id=id, name=name, timestamp=timestamp, link=link,
                         subscribers_amount=subscribers_amount,
                         verified=verified)

    print(parsed_group)

    return parsed_group


def parse_group_pages(group_ids):
    vk_api = vk_api_authorization()

    groups = vk_api.groups.getById(
        group_ids=group_ids,
        fields="members_count,verified")

    parsed_groups = [parse_group(group) for group in groups]

    return parsed_groups
