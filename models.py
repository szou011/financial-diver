from database import engine
from orm import *

from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy import select

with Session(engine) as session:
    stmt = select(Debtor) 
    for row in session.execute(stmt):
        print(row)


