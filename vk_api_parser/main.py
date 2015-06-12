# -*- coding: utf8 -*-

__author__ = 'dimagalov'


from parsers.user import parse_user_pages
# from parsers.group import parse_group_pages

durov = parse_user_pages("durov")[0]
print(durov)

for post in durov.wall.posts:
    print(post)

# parse_group_pages("topdonersuka, off__wos, baneks")
