# -*- coding: utf8 -*-

__author__ = 'dimagalov'

from common.tools import vk_api_authorization
from parsers.post import parse_post


def get_wall(vk_api, id):
    if id.isdigit():
        return vk_api.wall.get(owner_id=id)
    else:
        return vk_api.wall.get(domain=id)


def parse_wall(id):
    vk_api = vk_api_authorization()

    wall = get_wall(vk_api, id)
    parsed_wall = [parse_post(post) for post in wall]

    return parsed_wall
