from common.models_db import Post
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///sqlalchemy.db')
db_session = sessionmaker()
db_session.configure(bind=engine)
session = db_session()


def delete_post(post_id):
    p = session.query(Post).filter_by(id=post_id).first()
    session.delete(p)
    session.commit()


def add_post(post):
    #print(post)
    '''
    session.add(post)
    for attachment in post.attachments.list_of_attachments:
        attachment.post_id = post.id
        session.add(attachment)

    session.commit()
    '''
    #print (post.attachments)
    pass