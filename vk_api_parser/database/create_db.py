from common.models_db import Base
from database.config import engine
Base.metadata.create_all(engine)
