# -*- coding: utf8 -*-

__author__ = 'dimagalov'

from common.models import Video
from common.tools import cook_soup_from_url, get_current_timestamp


def get_video_id(video_soup):
    return video_soup["data-vid"]


def get_video_name(video_soup):
    return video_soup.find("div", class_="video_row_info_name").a.string.strip()


def get_owner_id(video_soup):
    return "https://vk.com" + video_soup.find("a", class_="mem_link")["href"]


def get_owner_name(video_soup):
    return video_soup.find("a", class_="mem_link").string


def get_publication_date(video_soup):
    return video_soup.find("span", class_="video_row_info_date rel_date_needs_update").string


def get_video_length(video_soup):
    return video_soup.find("div", class_="video_row_duration video_row_count").string


def get_views_amount(video_soup):
    amount_info = str(video_soup.find("span", class_="video_row_info_views"))
    amount_info = amount_info.replace("<span class=\"num_delim\"> </span>", "")
    amount_info = amount_info.replace("<span class=\"video_row_info_views\">", "")
    amount_info = amount_info.replace("</span>", "")
    amount_info = amount_info.strip()
    return amount_info


def get_likes_amount(video_soup):
    return -1


def get_video_link(video_soup):
    return "https://vk.com/video" + get_video_id(video_soup)


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

    video = Video(video_id, video_name, owner_id, owner_name, timestamp, publication_date, video_length, views_amount, likes_amount, video_link)
    return video


def get_video_list(soup):
    return soup.find_all('div', class_="video_row clear_fix")


def parse_video_page(url):
    soup = cook_soup_from_url(url)
    video_list = get_video_list(soup)

    for video in video_list:
        parsed_video = parse_video(video)
        print(parsed_video)
