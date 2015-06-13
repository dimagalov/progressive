# -*- coding: utf8 -*-

__author__ = 'dimagalov'

from common.tools import get_current_timestamp
from common.tools import vk_api_authorization


class Photo:
    def __init__(self, id=0, owner_id=0, timestamp="", publication_date="",
                 likes_amount=0, link="", description=""):
        self.id = id
        self.owner_id = owner_id
        self.timestamp = timestamp
        self.publication_date = publication_date
        self.likes_amount = likes_amount
        self.link = link
        self.description = description

    def __str__(self):
        return ("Photo id: {}\n".format(str(self.id)) +
                "Photo owner id: {}\n".format(str(self.owner_id)) +
                "Publication date: {}\n".format(self.publication_date) +
                "Likes amount: {}\n".format(str(self.likes_amount)) +
                "Link: {}\n".format(self.link) +
                "Description: {}\n".format(self.description))


class Audio:
    def __init__(self, id=0, owner_id=0, artist="", title="", timestamp="",
                 duration=0, link="", lyrics_id=0, album_id=0, genre_id=0):
        self.id = id
        self.artist = artist
        self.title = title
        self.owner_id = owner_id
        self.timestamp = timestamp
        self.duration = duration
        self.link = link
        self.lyrics_id = lyrics_id
        self.album_id = album_id
        self.genre_id = genre_id

    def __str__(self):
        return ("Audio id: {}\n".format(str(self.id)) +
                "Audio owner id: {}\n".format(str(self.owner_id)) +
                "Artist: {}\n".format(self.artist) +
                "Title: {}\n".format(self.title) +
                "Duration: {}\n".format(str(self.duration)) +
                "Link: {}\n".format(self.link) +
                "Lyrics id: {}\n".format(str(self.lyrics_id)) +
                "Album id: {}\n".format(str(self.album_id)) +
                "Genre id: {}\n".format(str(self.genre_id)))


class Video:
    def __init__(self, id=0, title="", owner_id=0, timestamp="",
                 publication_date="", duration=0, views_amount=0,
                 likes_amount=0, link="", description=""):
        self.id = id
        self.owner_id = owner_id
        self.title = title
        self.timestamp = timestamp
        self.description = description
        self.duration = duration
        self.link = link
        self.publication_date = publication_date
        self.views_amount = views_amount
        self.likes_amount = likes_amount

    def __str__(self):
        return ("Video id: {}\n".format(str(self.id)) +
                "Video owner id: {}\n".format(str(self.owner_id)) +
                "Title: {}\n".format(self.title) +
                "Duration: {}\n".format(str(self.duration)) +
                "Publication date: {}\n".format(self.publication_date) +
                "Views amount: {}\n".format(str(self.views_amount)) +
                "Likes amount: {}\n".format(str(self.likes_amount)) +
                "Link: {}\n".format(self.link) +
                "Description: {}\n".format(self.description))


class Link:
    def __init__(self, url="", title="", description="", image_src="",
                 timestamp=""):
        self.url = url
        self.title = title
        self.timestamp = timestamp
        self.description = description
        self.image_src = image_src

    def __str__(self):
        return ("Link url: {}\n".format(self.url) +
                "Title: {}\n".format(self.title) +
                "Description: {}\n".format(self.description) +
                "Image src: {}\n".format(self.image_src))


class Attachments:
    def __init__(self, list_of_attachments=[]):
        self.amount = 0
        self.list_of_attachments = []

        for attachment in list_of_attachments:
            timestamp = get_current_timestamp()

            if attachment["type"] == "photo":
                self.amount += 1

                photo = attachment["photo"]

                id = photo["id"]
                owner_id = photo["owner_id"]
                publication_date = photo["date"]
                description = photo["text"]

                link = "https://vk.com/photo{}_{}".format(
                    str(owner_id), str(id))

                vk_api = vk_api_authorization()

                values = {
                    "photos": "{}_{}".format(
                        str(owner_id), str(id)),
                    "extended": 1
                }

                extended_info = vk_api.method("photos.getById", values)[0]
                likes_amount = extended_info["likes"]["count"]

                parsed_photo = Photo(
                    id=id, owner_id=owner_id, timestamp=timestamp,
                    publication_date=publication_date, description=description,
                    link=link, likes_amount=likes_amount)

                self.list_of_attachments.append(parsed_photo)

            elif attachment["type"] == "posted_photo":
                self.amount += 1
                photo = attachment["posted_photo"]

                id = photo["id"]
                owner_id = photo["owner_id"]
                link = photo["photo_604"]

                parsed_photo = Photo(id=id, owner_id=owner_id, link=link)

                self.list_of_attachments.append(parsed_photo)

            elif attachment["type"] == "audio":
                self.amount += 1
                audio = attachment["audio"]

                id = audio["id"]
                artist = audio["artist"]
                title = audio["title"]
                owner_id = audio["owner_id"]
                duration = audio["duration"]
                link = audio["url"]
                lyrics_id = audio["lyrics_id"]
                album_id = audio["album_id"]
                genre_id = audio["genre_id"]

                parsed_audio = Audio(
                    id=id, owner_id=owner_id, timestamp=timestamp,
                    artist=artist, title=title, duration=duration, link=link,
                    lyrics_id=lyrics_id, album_id=album_id, genre_id=genre_id)

                self.list_of_attachments.append(parsed_audio)

            elif attachment["type"] == "video":
                self.amount += 1
                video = attachment["video"]

                id = video["id"]
                owner_id = video["owner_id"]
                title = video["title"]
                description = video["description"]
                duration = video["duration"]
                link = "https://vk.com/video{}_{}".format(
                    str(owner_id), str(id))
                publication_date = video["date"]
                views_amount = video["views"]

                likes_amount = -1

                parsed_video = Video(
                    id=id, owner_id=owner_id, timestamp=timestamp,
                    title=title, duration=duration, link=link,
                    description=description, publication_date=publication_date,
                    views_amount=views_amount, likes_amount=likes_amount)

                self.list_of_attachments.append(parsed_video)

            elif attachment["type"] == "link":
                self.amount += 1
                link = attachment["link"]

                url = link["url"]
                title = link["title"]
                description = link["description"]
                image_src = link["image_src"]

                parsed_link = Link(url=url, title=title,
                                   description=description,
                                   image_src=image_src)

                self.list_of_attachments.append(parsed_link)

            else:
                pass

    def __str__(self):
        result = ""
        for attachment in self.list_of_attachments:
            result += "\nType: {}\n".format(str(type(attachment)))
            result += "{}\n".format(str(attachment))
        return result


class Post:
    def __init__(self, id=0, owner_id=0, author_id=0, timestamp="",
                 publication_date="", text="", likes_amount=0,
                 reposts_amount=0, post_type="", link="",
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
