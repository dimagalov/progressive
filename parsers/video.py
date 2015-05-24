# -*- coding: utf8 -*-

__author__ = 'dimagalov'

import time
from common.models import Video
from common.tools import cook_soup_from_url, get_current_timestamp


def get_video_id(video_soup):
    try:
        return video_soup["data-vid"]
    except:
        print("Problem occured while getting video id")


def get_video_name(video_soup):
    try:
        info = video_soup.find("div", class_="video_row_info_name")
        return info.a.string.strip()
    except:
        print("Problem occured while getting video name")


def get_owner_id(video_soup):
    try:
        return ("https://vk.com" +
                video_soup.find("a", class_="mem_link")["href"])
    except:
        print("Problem occured while getting owner id")


def get_owner_name(video_soup):
    try:
        return video_soup.find("a", class_="mem_link").string
    except:
        print("Problem occured while getting owner name")


def get_publication_date(video_soup):
    try:
        return video_soup.find("span", class_="video_row_info_date " +
                               "rel_date_needs_update").string
    except:
        print("Problem occured while getting publication date")


def get_video_length(video_soup):
    try:
        return video_soup.find("div", class_="video_row_duration " +
                                             "video_row_count").string
    except:
        print("Problem occured while getting video length")


def get_views_amount(video_soup):
    try:
        amount = str(video_soup.find("span", class_="video_row_info_views"))
        amount = amount.replace("<span class=\"num_delim\"> </span>", "")
        amount = amount.replace("<span class=\"video_row_info_views\">", "")
        amount = amount.replace("</span>", "")
        amount = amount.strip()
        return amount
    except:
        print("Problem occured while getting views amount")


def get_likes_amount(video_soup):
    try:
        return "None"
    except:
        print("Problem occured while getting likes amount")


def get_video_link(video_soup):
    try:
        return "https://vk.com/video" + get_video_id(video_soup)
    except:
        print("Problem occured while getting video link")


def get_video_description(video_soup):
    try:
        return "None"
    except:
        print("Problem occured while getting video description")


def parse_video(video_soup):
    video_id = get_video_id(video_soup)
    video_name = get_video_name(video_soup)
    owner_id = get_owner_id(video_soup)
    owner_name = get_owner_name(video_soup)
    timestamp = get_current_timestamp()
    publication_date = get_publication_date(video_soup)
    video_length = get_video_length(video_soup)
    views_amount = get_views_amount(video_soup)
    likes_amount = get_likes_amount(video_soup)
    video_link = get_video_link(video_soup)
    video_description = get_video_description(video_soup)

    video = Video(video_id, video_name, owner_id, owner_name, timestamp,
                  publication_date, video_length, views_amount, likes_amount,
                  video_link, video_description)
    return video


def get_video_list(soup):
    try:
        return soup.find_all('div', class_="video_row clear_fix")
    except:
        print("Problem occured while getting video list")


def parse_video_page(url):
    MAX_VIDS = 4200

    if url.find('offset') == -1:
        url += '?offset='

    pos = url.find('=') + 1
    total_amount = 0

    for offset in range(0, MAX_VIDS, 21):
        url = url[:pos] + str(offset)

        if offset % 84 == 0:
            time.sleep(1)

        try:
            soup = cook_soup_from_url(url)
            video_list = get_video_list(soup)

            for video in video_list:
                parsed_video = parse_video(video)
                print(parsed_video)

            if len(video_list) == 0:
                break

            total_amount += len(video_list)
        except:
            print('Problem occured while parsing photo page')
    print('-----------\nTotal videos: %d' % total_amount)
