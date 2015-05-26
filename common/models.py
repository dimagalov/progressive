# -*- coding: utf8 -*-

__author__ = 'dimagalov'


class User:
    def __init__(self, id="", name="", timestamp="",
                 friends_amount="", subscribers_amount="", link=""):
        self.id = id
        self.name = name
        self.timestamp = timestamp
        self.friends_amount = friends_amount
        self.subscribers_amount = subscribers_amount
        self.link = link

    def __str__(self):
        return ("User id: {}\n".format(self.id) +
                "User name: {}\n".format(self.name) +
                "Amount of friends: {}\n".format(str(self.friends_amount)) +
                "Amount of subscribers: " +
                "{}\n".format(str(self.subscribers_amount)) +
                "User link: {}\n".format(self.link))


class Group:
    def __init__(self, id="", name="", timestamp="",
                 subscribers_amount="", link=""):
        self.id = id
        self.name = name
        self.timestamp = timestamp
        self.subscribers_amount = subscribers_amount
        self.link = link

    def __str__(self):
        return ("Group id: {}\n".format(self.id) +
                "Group name: {}\n".format(self.name) +
                "Amount of subscribers: " +
                "{}\n".format(str(self.subscribers_amount)) +
                "Group link: {}\n".format(self.link))


class Video:
    def __init__(self, id="", name="", owner_id="", owner_name="",
                 timestamp="", publication_date="", length="", views_amount="",
                 likes_amount="", link="", description=""):
        self.id = id
        self.name = name
        self.owner_id = owner_id
        self.owner_name = owner_name
        self.timestamp = timestamp
        self.publication_date = publication_date
        self.length = length
        self.views_amount = views_amount
        self.likes_amount = likes_amount
        self.link = link
        self.description = description

    def __str__(self):
        return ("Video id: {}\n".format(self.id) +
                "Video name: {}\n".format(self.name) +
                "Video owner id: {}\n".format(self.owner_id) +
                "Video owner name: {}\n".format(self.owner_name) +
                "Publication date: {}\n".format(self.publication_date) +
                "Video length: {}\n".format(self.length) +
                "Views amount: {}\n".format(str(self.views_amount)) +
                "Likes amount: {}\n".format(str(self.likes_amount)) +
                "Link: {}\n".format(self.link) +
                "Description: {}\n".format(self.description))


class Post:
    def __init__(self, id="", author=User(), timestamp="", publication_date="",
                 likes_amount="", reposts_amount="", link=""):
        self.id = id
        self.author = author
        self.timestamp = timestamp
        self.publication_date = publication_date
        self.likes_amount = likes_amount
        self.reposts_amount = reposts_amount
        self.link = link

    def __str__(self):
        return ("Post id: {}\n".format(self.id) +
                "Post author name: {}\n".format(self.author.name) +
                "Post author id: {}\n".format(self.author.id) +
                "Publication date: {}\n".format(self.publication_date) +
                "Likes amount: {}\n".format(str(self.likes_amount)) +
                "Reposts amount: {}\n".format(str(self.reposts_amount)) +
                "Link: {}\n".format(self.link))


class User_Wall:
    def __init__(self, user=User(), posts=[], timestamp="", link=""):
        self.user = user
        self.posts = posts
        self.timestamp = timestamp
        self.link = link

    def __str__(self):
        return ("User id: {}\n".format(self.user.id) +
                "User name: {}\n".format(self.user.name) +
                "Amount of posts: {}\n".format(str(len(self.posts))) +
                "Wall link: {}\n".format(self.link))


class Group_Wall:
    def __init__(self, group=Group(), posts=[], timestamp="", link=""):
        self.group = group
        self.posts = posts
        self.timestamp = timestamp
        self.link = link

    def __str__(self):
        return ("Group id: {}\n".format(self.group.id) +
                "Group name: {}\n".format(self.group.name) +
                "Amount of posts: {}\n".format(str(len(self.posts))) +
                "Wall link: {}\n".format(self.link))


class Photo:
    def __init__(self, id="", owner_id="", owner_name="", timestamp="", publication_date="", \
                                                            likes="", reposts="", link="", desc=""):
        self.id = id
        self.owner_name = owner_name
        self.owner_id = owner_id
        self.timestamp = timestamp
        self.publication_date = publication_date
        self.likes_amount = likes
        self.reposted_amount = reposts
        self.link = link
        self.description = desc

    def __str__(self):
        return ("Photo id: {}\n".format(self.id) +
                "Photo owner id: {}\n".format(self.owner_id) +
                "Photo owner name: {}\n".format(self.owner_name) +
                "Publication date: {}\n".format(self.publication_date) +
                "Likes amount: {}\n".format(str(self.likes_amount)) +
                "Reposted amount: {}\n".format(str(self.reposted_amount)) +
                "Link: {}\n".format(self.link) +
                "Description: {}\n".format(self.description))
