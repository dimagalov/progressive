# -*- coding: utf8 -*-

__author__ = 'dimagalov'


# from parsers.user import parse_user_pages
from parsers.group import parse_group_pages

# durov = parse_user_pages("durov")[0]
# print(durov)

# for post in durov.wall.posts:
#     print(post)

doner = parse_group_pages("topdonersuka")[0]
print(doner)

for post in doner.wall.posts:
    print(post)
