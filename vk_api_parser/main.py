# -*- coding: utf8 -*-

__author__ = 'dimagalov'

#from database.query import add_post
from parsers.wall import parse_wall

res = parse_wall(53083705)
print (res)