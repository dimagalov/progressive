# -*- coding: utf8 -*-

__author__ = 'dimagalov'

from common.tools import get_current_timestamp
from common.models import Wall
from common.tools import vk_api_authorization
from parsers.post import parse_post


def get_wall_link(id):
    return "https://vk.com/wall{}?own=1".format(id)


def parse_wall(id):

    ''' WARNING! parse_wall takes only id, not a screen name '''

    vk_api = vk_api_authorization()

    wall = vk_api.wall.get(owner_id=id)
    parsed_posts = [parse_post(post) for post in wall["items"]]

    parsed_wall = Wall(owner_id=id, posts=parsed_posts,
                       timestamp=get_current_timestamp(),
                       link=get_wall_link(id))

    return parsed_wall
