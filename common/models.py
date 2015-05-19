# -*- coding: utf8 -*-

__author__ = 'dimagalov'


class Video:
    def __init__(self, id="", name="", owner_id="", owner_name="", timestamp="", publication_date="", length="", views_amount="", likes_amount="", link="", description=""):
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
