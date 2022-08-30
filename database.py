from sqlalchemy import create_engine

from orm import *

engine = create_engine("sqlite+pysqlite:////Users/StephenZ/WPy64_3950/scripts/source/financial-diver/database/exo.db", echo=False, future=True)
