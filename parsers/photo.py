# -*- coding: utf8 -*-

__author__ = 'emil.guseynov'

from common.models import Photo
from common.tools import cook_soup_from_url, get_current_timestamp
import time

def get_photo_id(photo_soup):
    try:
        return photo_soup["href"][1:]
    except:
        print("Problem occured while getting photo id")

def get_owner_id(photo_soup):
    photo_id = get_photo_id(photo_soup)
    url = 'https://m.vk.com/%s' % photo_id

    try:
        owner_soup = cook_soup_from_url(url)
        return owner_soup.find_all('dd')[-1].contents[0]['href']
    except:
        print("Problem occured while getting owner id")


def get_owner_name(photo_soup):
    photo_id = get_photo_id(photo_soup)
    url = 'https://m.vk.com/%s' % photo_id

    try:
        owner_soup = cook_soup_from_url(url)
        return owner_soup.find_all('dd')[-1].contents[0].contents[0]
    except:
        print("Problem occured while getting owner name")


def get_publication_date(photo_soup):
    photo_id = get_photo_id(photo_soup)
    pos = photo_id.find('_') + 1
    url = 'https://m.vk.com/%s' % photo_id
    try:
        pub_soup = cook_soup_from_url(url)
        return pub_soup.find('span', class_='item_date').contents[0]
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
    url = 'https://m.vk.com/like?act=members&object=%s&tab=published' % photo_id
    try:
        reposted_soup = cook_soup_from_url(url)

        reposted_amount = ""
        span_str = reposted_soup.find('span', class_='slim_header_label')

        if span_str != None:
            span_str = span_str.contents[0]
        
            #fetch numbers
        
            for item in span_str.split():
                if item.isdigit():
                    reposted_amount = item

        return reposted_amount
    except:
        print("Problem occured while getting reposted amount")

def get_photo_link(photo_soup):
    try:
        return "https://vk.com/" + get_photo_id(photo_soup)
    except:
        print("Problem occured while getting photo link")


def get_photo_description(photo_soup):
    photo_id = get_photo_id(photo_soup)
    url = 'https://m.vk.com/%s' % photo_id
    try:
        desc_soup = cook_soup_from_url(url)
        res = desc_soup.find('div', class_='mv_description')
        if res != None:
            return res.contents[0]
        
        return ""
        
    except:
        print("Problem occured while getting photo description")



def parse_photo(photo_soup):

    photo_id = get_photo_id(photo_soup)

    owner_id = get_owner_id(photo_soup)
    owner_name = get_owner_name(photo_soup)

    publication_date = get_publication_date(photo_soup)
    
    likes_amount = get_likes_amount(photo_soup)
    photo_link = get_photo_link(photo_soup)
    photo_description = get_photo_description(photo_soup)
    timestamp = get_current_timestamp()
    reposted_amount = get_reposted_amount(photo_soup)
    photo_link = get_photo_link(photo_soup)

    photo = Photo(id=photo_id, link=photo_link, likes_amount=likes_amount,
                  reposted_amount=reposted_amount,
                  timestamp=timestamp, publication_date=publication_date,
                  description=photo_description, owner_id=owner_id, owner_name=owner_name)

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
            print(total_amount)
        except:
            print('whoops')
    print('-----------\nTotal photos: %d' % total_amount)