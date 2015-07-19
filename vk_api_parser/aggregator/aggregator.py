# -*- coding: utf8 -*-

__author__ = 'a.khachatryan'

from parsers.wall import parse_wall

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

def aggregator(users):
    print(parse_wall(users[0]))