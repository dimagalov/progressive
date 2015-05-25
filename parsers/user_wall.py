# -*- coding: utf8 -*-

__author__ = 'dimagalov'

import time
from common.models import User_Wall
from parsers.post import parse_post
from common.tools import cook_soup_from_url, get_current_timestamp


def get_user(post):
    return post.author


def get_post_list(soup):
    try:
        links = soup.find_all('a', class_="anchor")
        for i in range(len(links)):
            links[i] = "https://vk.com/wall" + str(links[i]['name'])[4:]
        return links
    except:
        print("Problem occured while getting post list")


def get_user_posts(url):
    url = "//m.".join(url.split("//"))

    MAX_POSTS = 210

    if url.find('offset') == -1:
        url += '?offset='

    index = url.find('=') + 1
    total_amount = 0

    posts = []

    for temp_offset in range(0, MAX_POSTS, 10):
        offset = temp_offset
        if temp_offset != 0:
            offset -= 5

        url = url[:index] + str(offset)

        if offset % 45 == 0:
            time.sleep(1)

        try:
            soup = cook_soup_from_url(url)
            post_list = get_post_list(soup)

            for post in post_list:
                parsed_post = parse_post(post)
                posts.append(parsed_post)

            if len(post_list) == 0:
                break
            total_amount += len(post_list)
        except:
            print('Problem occured while parsing posts page')

    print('-----------\nTotal posts: %d' % total_amount)

    return posts


def get_wall_link(post):
    user_id = get_user(post).id
    return "https://vk.com/wall" + user_id


def parse_user_wall(url):
    posts = get_user_posts(url)
    user = get_user(posts[0])
    timestamp = get_current_timestamp()
    wall_link = get_wall_link(posts[0])

    user_wall = User_Wall(user, posts, timestamp, wall_link)
    print(user_wall)

    return user_wall
