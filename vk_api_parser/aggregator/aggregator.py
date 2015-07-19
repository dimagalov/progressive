# -*- coding: utf8 -*-

__author__ = 'a.khachatryan'

from parsers.wall import parse_wall
from database.query import add_post, delete_post
from time import time

def get_users(filename):
    f = open('base/' + filename, 'r')
    lines = f.readlines()
    results = []
    for line in lines:
        args = line.split()
        for arg in args:
            if str(arg).find('id') != -1:
                results.append(str(arg)[str(arg).find('id') + 2:])
                break
    return results

def aggregator(users):
    last_time = int(time())
    best_post = None
    best_post_delay = 10 # sec
    max_old_post = 24 * 60 * 60 # 3 hour
    used_posts = []

    while (1):
        for user in users:
            posts = parse_wall(user).posts
            for post in posts:
                if post.id not in used_posts and int(time()) - int(post.publication_date) < max_old_post:
                   if best_post is None or post.likes_amount > best_post.likes_amount:
                        best_post = post
            if best_post != None and int(time()) - last_time > best_post_delay:
                add_post(best_post)
                print ("new best post id:", best_post.id)
                used_posts.append(best_post.id)
                last_time = int(time())
                best_post = None

