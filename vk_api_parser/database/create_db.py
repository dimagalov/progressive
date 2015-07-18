from common.models_db import Base
from config import engine
Base.metadata.create_all(engine)
