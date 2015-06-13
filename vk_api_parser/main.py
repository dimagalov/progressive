# -*- coding: utf8 -*-

__author__ = 'dimagalov'


from parsers.user import parse_user_pages
# from parsers.group import parse_group_pages

dimagalov = parse_user_pages("dimagalov")[0]
print(dimagalov)

for post in dimagalov.wall.posts:
    print(post)

# doner = parse_group_pages("topdonersuka")[0]
# print(doner)

# for post in doner.wall.posts:
#     print(post)
