# -*- coding: utf8 -*-

__author__ = 'dimagalov'


class Photo:
    def __init__(self, id="", owner_id="", owner_name="", timestamp="",
                 publication_date="", likes="", reposts="", link="", desc=""):
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


class Attachments:
    def __init__(self, amount=0, list_of_attachments=[]):
        pass


class Post:
    def __init__(self, id=0, owner_id=0, author_id=0, timestamp="",
                 publication_date="", text="", likes_amount="",
                 reposts_amount="", post_type="", link="",
                 attachments=Attachments()):
        self.id = id
        self.owner_id = owner_id
        self.author_id = author_id
        self.timestamp = timestamp
        self.publication_date = publication_date
        self.text = text
        self.likes_amount = likes_amount
        self.reposts_amount = reposts_amount
        self.post_type = post_type
        self.link = link
        self.attachments = attachments

    def __str__(self):
        return ("Post id: {}\n".format(str(self.id)) +
                "Post type: {}\n".format(self.post_type) +
                "Post owner id: {}\n".format(str(self.owner_id)) +
                "Post author id: {}\n".format(str(self.author_id)) +
                "Publication date: {}\n".format(self.publication_date) +
                "Text:\n{}\n".format(self.text) +
                "Attachments:\n{}\n".format(str(self.attachments)) +
                "Likes amount: {}\n".format(str(self.likes_amount)) +
                "Reposts amount: {}\n".format(str(self.reposts_amount)) +
                "Link: {}\n".format(self.link))


class Wall:
    def __init__(self, owner_id=0, posts=[], timestamp="", link=""):
        self.owner_id = owner_id
        self.posts = posts
        self.timestamp = timestamp
        self.link = link

    def __str__(self):
        return ("    Owner id: {}\n".format(str(self.owner_id)) +
                "    Amount of posts: {}\n".format(str(len(self.posts))) +
                "    Wall link: {}\n".format(self.link))


class User:
    def __init__(self, id=0, first_name="", last_name="", timestamp="",
                 friends_amount=0, subscribers_amount=0, link="",
                 verified=0, sex=0, bdate="", country="", city="",
                 wall=Wall()):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.timestamp = timestamp
        self.friends_amount = friends_amount
        self.subscribers_amount = subscribers_amount
        self.verified = verified
        self.link = link
        self.sex = sex
        self.bdate = bdate
        self.country = country
        self.city = city
        self.wall = wall

    def __str__(self):
        return ("User id: {}\n".format(str(self.id)) +
                "User name: {} {}\n".format(self.first_name, self.last_name) +
                "User sex: {} (1 - female, 2 - male)\n".format(str(self.sex)) +
                "Birthday: {}\n".format(self.bdate) +
                "Country: {}\n".format(self.country) +
                "City: {}\n".format(self.city) +
                "Amount of friends: {}\n".format(str(self.friends_amount)) +
                "Amount of subscribers: " +
                "{}\n".format(str(self.subscribers_amount)) +
                "User verified: {}\n".format(str(self.verified)) +
                "User link: {}\n".format(self.link) +
                "User wall:\n\n{}".format(str(self.wall)))


class Group:
    def __init__(self, id=0, name="", timestamp="",
                 subscribers_amount=0, link="", verified=0,
                 type="", description="", wall=Wall()):
        self.id = id
        self.name = name
        self.timestamp = timestamp
        self.subscribers_amount = subscribers_amount
        self.link = link
        self.verified = verified
        self.type = type
        self.description = description
        self.wall = wall

    def __str__(self):
        return ("Group id: {}\n".format(str(self.id)) +
                "Group name: {}\n".format(self.name) +
                "Amount of subscribers: " +
                "{}\n".format(str(self.subscribers_amount)) +
                "Group verified: {}\n".format(str(self.verified)) +
                "Type: {}\n".format(self.type) +
                "Description:\n{}\n".format(self.description) +
                "Group link: {}\n".format(self.link) +
                "Group wall:\n{}".format(str(self.wall)))
