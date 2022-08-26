from database import engine
from orm import *

from sqlalchemy.orm import Session
from sqlalchemy import func

def get_retailer(retailgroup=None):
    with Session(engine) as session:
        if not retailgroup:
            result = session.query(Retailer.GROUPNAME, func.count(Debtor.ACCNO)).join(Debtor.retailer).group_by(Retailer.GROUPNAME).all()
        else:
            result = session.query(Retailer.GROUPNAME, func.count(Debtor.ACCNO)).join(Debtor.retailer, Debtor.retailgroup).filter(RetailGroup.GROUPNAME == retailgroup).group_by(Retailer.GROUPNAME).all()
    return (
        [row[0] for row in result],
        [row[1] for row in result])


def get_retailgroup():
    with Session(engine) as session:
            result = session.query(RetailGroup.GROUPNAME).all()
    return [row[0] for row in result]
