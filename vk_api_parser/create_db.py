# -*- coding: utf8 -*-

__author__ = 'emil.guseynov'

from common.tools import get_current_timestamp
from common.tools import vk_api_authorization

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from common.models_db import get_base

Base = get_base()
engine = create_engine('sqlite:///vk.db')
Base.metadata.create_all(engine)