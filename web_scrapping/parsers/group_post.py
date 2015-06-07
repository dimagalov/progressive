# -*- coding: utf8 -*-

__author__ = 'dimagalov'

from common.models import Post
from common.tools import cook_soup_from_url, get_current_timestamp
from parsers.group import parse_group_page


def get_post_id(soup):
    return get_post_link(soup).split('_')[1]


def get_author_id(soup):
    return get_post_link(soup).split('wall')[1].split('_')[0][1:]


def get_post_author(soup):
    try:
        return parse_group_page("https://vk.com/public" + get_author_id(soup))
    except:
        print("Problem occured while getting post author")


def get_publication_date(soup):
    return soup.find("span", class_="wi_date").text


def get_likes_amount(soup):
    amount = str(soup.find("span", class_="v_like"))
    amount = amount.replace("<span class=\"num_delim\"> </span>", "")
    amount = amount.replace("<span class=\"v_like\">", "")
    amount = amount.replace("</span>", "")
    amount = amount.replace("<b>", "")
    amount = amount.replace("</b>", "")
    amount = amount.strip()
    return amount


def get_reposts_amount(soup):
    return "None"


def get_post_link(soup):
    return soup.find("link", rel="canonical")['href']


def parse_post(url):
    soup = cook_soup_from_url(url)

    post_id = get_post_id(soup)
    post_author = get_post_author(soup)
    timestamp = get_current_timestamp()
    publication_date = get_publication_date(soup)
    likes_amount = get_likes_amount(soup)
    reposts_amount = get_reposts_amount(soup)
    post_link = get_post_link(soup)

    post = Post(post_id, post_author, timestamp, publication_date,
                likes_amount, reposts_amount, post_link)
    print(post)

    return post
