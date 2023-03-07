from schema import *

from sqlalchemy.orm import DeclarativeBase 
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class Debtor(Base):
    __table__ = debtor_account_table

    id = debtor_account_table.c.ACCNO
    name = debtor_account_table.c.NAME 
    head_account_id = debtor_account_table.c.HEAD_ACCNO

    currency = relationship("Currency", back_populates='debtor')
    retail_channel = relationship("RetailChannel", back_populates='debtor')

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, currency={self.currency.currency_code}, retail_channel={self.retail_channel.name})"


class Currency(Base):
    __table__ = currency_table

    currency_code = currency_table.c.CURRCODE
    currency_name = currency_table.c.CURRNAME

    debtor = relationship('Debtor')



class RetailChannel(Base):
    __table__ = debtor_group_table

    name = debtor_group_table.c.GROUPNAME

    debtor = relationship('Debtor')


class DebtorTransaction(Base):
    __table__ = debtor_transaction_table

    head_account_id = debtor_transaction_table.c.ACCNO
    sales_account_id = debtor_transaction_table.c.SALES_ACCNO
    amount = debtor_transaction_table.c.AMOUNT

    debtor_transaction_head_account = relationship('Debtor', foreign_keys=head_account_id)
    debtor_transaction_sales_account = relationship('Debtor', foreign_keys=sales_account_id)




