from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from orm import *

engine = create_engine("sqlite+pysqlite:///./database/exo.db", echo=False, future=True)

statement = select(Debtor.ACCNO, Currency.CURRCODE).join(Debtor.debtor_currency).where(Debtor.ACCNO == 9901)

with Session(engine, future=True) as session:
    result = session.execute(statement).all()
    print(result)
