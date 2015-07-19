from common.models_db import Post
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///vk.db')
db_session = sessionmaker()
db_session.configure(bind=engine)
session = db_session()


def delete_post(post_id):
    p = session.query(Post).filter_by(id=post_id).first()
    session.delete(p)
    session.commit()


def add_post(post):
    session.add(post)

    # for attachment in post.attachments.get():
    #     attachment.post_id = post.id
    #     session.add(attachment)

    '''
        Traceback (most recent call last):
          File "main.py", line 13, in <module>
            aggregator(get_users('users_club_22079806'))
          File "/Users/artem/Programming/progressive/vk_api_parser/aggregator/aggregator.py", line 36, in aggregator
            add_post(best_post)
          File "/Users/artem/Programming/progressive/vk_api_parser/database/query.py", line 21, in add_post
            for attachment in post.attachments.get():
        AttributeError: 'NoneType' object has no attribute 'get'
    '''

    session.commit()
