from sqlalchemy import create_engine

from orm import *

engine = create_engine("sqlite+pysqlite:///./database/exo.db", echo=False, future=True)
