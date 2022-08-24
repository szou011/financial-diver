from schema import *

from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Debtor(Base):
    __table__ = debtor_account_table
    debtor_currency = relationship("Currency", back_populates='debtor')

class Currency(Base):
    __table__ = currency_table
    debtor = relationship("Debtor", back_populates="debtor_currency")
    creditor = relationship("Creditor", back_populates='creditor_currency')

class RetailChannel(Base):
    __table__ = debtor_group_table


class AdvertisingGroup(Base):
    __table__ = debtor_group2_table

class Retailer(Base):
    __table__ = debtor_group3_table

class RetailGroup(Base):
    __table__ = retail_group_table

class CreditStatus(Base):
    __table__ = credit_status_table

class Staff(Base):
    __table__ = staff_table

class Narrative(Base):
    __table__ = narrative_table

class Branch(Base):
    __table__ = branch_table

class Period(Base):
    __table__ = period_status_table

class DebtorTransaction(Base):
    __table__ = debtor_transaction_table

class DebtorAllocation(Base):
    __table__ = debtor_allocation_table

class StockGroup(Base):
    __table__ = stock_group_table

class StockItem(Base):
    __table__ = stock_item_table

class DebtorInvoiceLine(Base):
    __table__ = debtor_invoiceline_table

class SalesOrder(Base):
    __table__ = sales_order_table

class SalesOrderLine(Base):
    __table__ = sales_orderline_table

class CreditorGroup(Base):
    __table__ = creditor_group_table

class Creditor(Base):
    __table__ = creditor_account_table
    creditor_currency = relationship("Currency", back_populates='creditor')

class CreditorInvoiceLine(Base):
    __table__ = creditor_invoiceline_table

class CreditorTransaction(Base):
    __table__ = creditor_transaction_table

class CreditorAllocation(Base):
    __table__ = creditor_allocation_table

class GLAccount(Base):
    __table__ = gl_account_table

class GLBatch(Base):
    __table__ = gl_batch_table

class GLTransaction(Base):
    __table__ = gl_transaction_table

class GLSubAccount(Base):
    __table__ = gl_subaccount_table