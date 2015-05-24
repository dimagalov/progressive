# -*- coding: utf8 -*-

__author__ = 'emil.guseynov'

from common.models import Photo
from common.tools import cook_soup_from_url, get_current_timestamp
import time

from bs4 import BeautifulSoup

def get_photo_id(photo_soup):
    try:
        return photo_soup["href"][1:]
    except:
        print("Problem occured while getting photo id")


def get_photo_name(photo_soup):
    try:
        return photo_soup.find("div", class_="photo_row_info_name").a.string.strip()
    except:
        print("Problem occured while getting photo name")


def get_owner_id(photo_soup):
    try:
        return "https://vk.com" + photo_soup.find("a", class_="mem_link")["href"]
    except:
        print("Problem occured while getting owner id")


def get_owner_name(photo_soup):
    try:
        return photo_soup.find("a", class_="mem_link").string
    except:
        print("Problem occured while getting owner name")


def get_publication_date(photo_soup):
    try:
        return photo_soup.find("span", class_="photo_row_info_date rel_date_needs_update").string
    except:
        print("Problem occured while getting publication date")


def get_views_amount(photo_soup):
    try:
        amount_info = str(photo_soup.find("span", class_="photo_row_info_views"))
        amount_info = amount_info.replace("<span class=\"num_delim\"> </span>", "")
        amount_info = amount_info.replace("<span class=\"photo_row_info_views\">", "")
        amount_info = amount_info.replace("</span>", "")
        amount_info = amount_info.strip()
        return amount_info
    except:
        print("Problem occured while getting views amount")


def get_likes_amount(photo_soup):
    photo_id = get_photo_id(photo_soup)
    url = 'https://m.vk.com/like?act=members&object={}'.format(photo_id)
    try:
        likes_soup = cook_soup_from_url(url)
        
        #fetch numbers

        likes_list = likes_soup.find('h4', class_='slim_header').contents
        likes_amount = ""
        for string in likes_list:
            try:
                for item in string.split():
                    if item.isdigit():
                        likes_amount += item
            except:
                pass

        return likes_amount

    except:
        print("Problem occured while getting likes amount")

def get_reposted_amount(photo_soup):
    photo_id = get_photo_id(photo_soup)
    url = 'https://m.vk.com/like?act=members&object={}&tab=published'.format(photo_id)
    try:
        reposted_soup = cook_soup_from_url(url)
        span_str = reposted_soup.find('span', class_='slim_header_label').contents[0]
        #fetch numbers
        reposted_amount = ""
        for item in span_str.split():
            if item.isdigit():
                reposted_amount = item
        return reposted_amount
    except:
        print("Problem occured while getting likes amount")

def get_photo_link(photo_soup):
    try:
        return "https://vk.com/" + get_photo_id(photo_soup)
    except:
        print("Problem occured while getting photo link")


def get_photo_description(photo_soup):
    try:
        return "None"
    except:
        print("Problem occured while getting photo description")


def parse_photo(photo_soup):
    
    photo_id = get_photo_id(photo_soup)
    '''
    photo_name = get_photo_name(photo_soup)
    owner_id = get_owner_id(photo_soup)
    owner_name = get_owner_name(photo_soup)
    
    publication_date = get_publication_date(photo_soup)
    
    views_amount = get_views_amount(photo_soup)
    likes_amount = get_likes_amount(photo_soup)
    photo_link = get_photo_link(photo_soup)
    photo_description = get_photo_description(photo_soup)

    photo = Photo(photo_id, photo_name, owner_id, owner_name, timestamp, publication_date, views_amount, likes_amount, photo_link, photo_description)
    '''
    
    
    timestamp = get_current_timestamp()
    likes_amount = get_likes_amount(photo_soup)
    reposted_amount = get_reposted_amount(photo_soup)
    photo_link = get_photo_link(photo_soup)
    photo = Photo(id=photo_id, link=photo_link, likes_amount=likes_amount, \
                        reposted_amount=reposted_amount, timestamp=get_current_timestamp())
    
    return photo


def get_photo_list(soup):
    try:
        return soup.find_all('a', class_="thumb_item al_photo")
    except:
        print("Problem occured while getting photo list")


def parse_photo_page(url):
    
    '''
    #html_doc = requests.get('http://m.vk.com/album53083705_00?_fm=photos').text
    #html_doc = requests.get('http://m.vk.com/album53083705_00?offset=24#photos').text
    #soup = BeautifulSoup(html_doc)
    #print(html_doc)
    '''
    MAX_PICS = 4024

    if url.find('offset') == -1:
        url += '?offset='

    pos = url.find('=') + 1
    total_amount = 0

    for i in range(0, MAX_PICS, 24):
        url = url[:pos] + str(i)

        if i % 96 == 0:
            time.sleep(1)

        try:

            soup = cook_soup_from_url(url)
            photo_list = get_photo_list(soup)
            
            for photo in photo_list:
                parsed_photo = parse_photo(photo)
                print(parsed_photo)

            total_amount += len(photo_list)
        except:
            print('whoops')
    print('-----------\nTotal photos: %d' % total_amount)