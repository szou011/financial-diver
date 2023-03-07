from sqlalchemy import create_engine

from schema import *

engine = create_engine("sqlite+pysqlite:///./database/demo.db", echo=False, future=True)

