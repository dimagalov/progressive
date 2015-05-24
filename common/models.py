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

class Photo:
    def __init__(self, id="", name="", owner_id="", owner_name="", timestamp="", publication_date="", length="", \
                 views_amount="", likes_amount="", reposted_amount="", link="", description=""):
        self.id = id
        self.name = name
        self.owner_id = owner_id
        self.owner_name = owner_name
        self.timestamp = timestamp
        self.publication_date = publication_date
        self.views_amount = views_amount
        self.likes_amount = likes_amount
        self.reposted_amount = reposted_amount
        self.link = link
        self.description = description

    def __str__(self):
        return ("Photo id: {}\n".format(self.id) +
                "Photo name: {}\n".format(self.name) +
                "Photo owner id: {}\n".format(self.owner_id) +
                "Photo owner name: {}\n".format(self.owner_name) +
                "Publication date: {}\n".format(self.publication_date) +
                "Views amount: {}\n".format(str(self.views_amount)) +
                "Likes amount: {}\n".format(str(self.likes_amount)) +
                "Reposted amount: {}\n".format(str(self.reposted_amount)) +
                "Link: {}\n".format(self.link) +
                "Description: {}\n".format(self.description))
