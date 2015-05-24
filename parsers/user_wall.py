# -*- coding: utf8 -*-

__author__ = 'dimagalov'

from common.models import User_Wall
from parsers.post import parse_post
from common.tools import cook_soup_from_url, get_current_timestamp


def get_user(soup):
    pass


def get_user_posts(soup):
    pass


def parse_user_wall(url):
    soup = cook_soup_from_url(url)

    print(soup.prettify())

    return

    user = get_user(soup)
    posts = get_user_posts(soup)

    user_wall = User_Wall(user, posts)
    print(user_wall)

    return User_Wall()
