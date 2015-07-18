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

    for attachment in post.attachments.get():
        attachment.post_id = post.id
        session.add(attachment)

    session.commit()
