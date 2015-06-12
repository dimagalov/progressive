# -*- coding: utf8 -*-

__author__ = 'dimagalov'

# from common.models import Photo
# from common.tools import timestamp_to_date

# from common.tools import vk_api_authorization


# def parse_photo_page(user_id):
#     vk_api = vk_api_authorization()
#     photos = vk_api.photos.get(owner_id=user_id, album_id="wall", extended=0)
#     print(photos)

# from common.models import Photo
# import vk_api
# import datetime

# def get_date(timestamp):
#     return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

# def parse_photo_page(screen_name):
#     login, password = 'dimagalov@gmail.com', 'Zee7eeneD5ucr4qu'
#     vk = vk_api.VkApi(login, password)
#     vk.authorization()


#     tools = vk_api.VkTools(vk)


#     user_info = vk.method('users.get', {'user_ids': screen_name})
#     owner_name = user_info[0]['first_name'] + ' ' + user_info[0]['last_name']
#     user_id = str(user_info[0]['id'])

#     posts = tools.get_all('wall.get', 1, {'owner_id': user_id}, limit_count = 25)
#     total_photos = 0
#     prefix = 'https://vk.com/%s?w=wall%s{}' % (screen_name, user_id + '_')

#     for post in posts['items']:
#         if 'attachments' in post.keys() and post['attachments'][0]['type'] == 'photo':
#             photo = Photo(id=post['id'], likes=post['likes']['count'], reposts=post['reposts']['count'], \
#                                     owner_id=post['owner_id'], owner_name=owner_name, desc=post['text'],
#                                                 link=prefix.format(post['id']), publication_date=get_date(post['date']))
#             total_photos += 1
#             print(photo)

#     print(total_photos)
