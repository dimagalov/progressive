# -*- coding: utf8 -*-

__author__ = 'dimagalov'

from common.tools import vk_api_authorization


def parse_user(user_id):
    return


def parse_users(user_ids):
    vk_api = vk_api_authorization()

    users = vk_api.users.get(
        user_ids=user_ids,
        fields=[
            ])

    for user_id in user_ids:
        users += [parse_user(user_id)]
    return users
