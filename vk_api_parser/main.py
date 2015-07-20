# -*- coding: utf8 -*-

__author__ = 'dimagalov'

# from database.query import add_post
# from parsers.wall import parse_wall

# res = parse_wall(53083705)
# print (res)

from aggregator.aggregator import get_users, aggregator
from database.query import delete_all


delete_all() # проблемы с повторным добавлением уже существующего, пока не оч ясно, как чинить

aggregator(get_users('users_club_22079806'), log = 1)