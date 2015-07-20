from common.models_db import Post
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc


engine = create_engine('sqlite:///vk.db')
db_session = sessionmaker()
db_session.configure(bind=engine)
session = db_session()


def delete_post(post_id):
    p = session.query(Post).filter_by(id=post_id).first()
    session.delete(p)
    session.commit()

def delete_all():
    try:
        num_rows_deleted = session.query(Post).delete()
        session.commit()
    except:
        session.rollback()

def add_post(post):
    session.merge(post)

    for attachment in post.attachments.get():
        attachment.post_id = post.id
        session.merge(attachment)

    session.commit()


def get_best_posts(number):
    try:
        number = int(number)
    except:
        number = 0
    return session.query(Post).order_by(desc('timestamp')).limit(number).all()
