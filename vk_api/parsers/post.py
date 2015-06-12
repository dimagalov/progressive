# -*- coding: utf8 -*-

__author__ = 'dimagalov'

from common.models import Post
from common.tools import get_current_timestamp


def get_post_id(post):
    try:
        return post["id"]
    except:
        print("Problem occured while getting post id")


def get_post_owner_id(post):
    try:
        return post["owner_id"]
    except:
        print("Problem occured while getting post owner id")


def get_post_author_id(post):
    try:
        return post["from_id"]
    except:
        print("Problem occured while getting post author id")


def get_post_publication_date(post):
    try:
        return post["date"]
    except:
        print("Problem occured while getting post publication date")


def get_post_text(post):
    try:
        return post["text"]
    except:
        print("Problem occured while getting post text")


def get_post_likes_amount(post):
    try:
        return post["likes"]["count"]
    except:
        print("Problem occured while getting post likes amount")


def get_post_reposts_amount(post):
    try:
        return post["reposts"]["count"]
    except:
        print("Problem occured while getting post reposts amount")


def get_post_type(post):
    try:
        return post["post_type"]
    except:
        print("Problem occured while getting post type")


def get_post_link(post):
    try:
        return "https://vk.com/wall{}_{}".format(
            str(get_post_owner_id(post)), str(get_post_id(post)))
    except:
        print("Problem occured while getting post link")


def get_post_attachments(post):
    try:
        return post["attachments"]
    except:
        print("Problem occured while getting post attachments")


def parse_post(post):
    id = get_post_id(post)
    owner_id = get_post_owner_id(post)
    author_id = get_post_author_id(post)
    timestamp = get_current_timestamp()
    publication_date = get_post_publication_date(post)
    text = get_post_text(post)
    likes_amount = get_post_likes_amount(post)
    reposts_amount = get_post_reposts_amount(post)
    post_type = get_post_type(post)
    link = get_post_link(post)
    attachments = get_post_attachments(post)

    parsed_post = Post(id=id, owner_id=owner_id, author_id=author_id,
                       timestamp=timestamp, publication_date=publication_date,
                       text=text, likes_amount=likes_amount,
                       reposts_amount=reposts_amount, post_type=post_type,
                       link=link, attachments=attachments)

    print(parsed_post)

    return parsed_post
