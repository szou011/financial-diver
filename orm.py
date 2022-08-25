from schema import *

from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Debtor(Base):
    __table__ = debtor_account_table
    currency = relationship("Currency", back_populates='debtor')
    retailchannel= relationship("RetailChannel", back_populates='debtor')
    advertisinggroup= relationship("AdvertisingGroup", back_populates='debtor')
    retailer= relationship("Retailer", back_populates='debtor')
    retailgroup= relationship("RetailGroup", back_populates='debtor')
    creditstatus= relationship("CreditStatus", back_populates='debtor')
    debtor_transaction = relationship("DebtorTransaction", back_populates='debtor') 
    debtor_invoice_line = relationship('DebtorInvoiceLine', back_populates='debtor')
    sales_order = relationship('SalesOrder', back_populates='debtor')
    sales_order_line = relationship('SalesOrderLine', back_populates='debtor')


class Currency(Base):
    __table__ = currency_table
    debtor = relationship("Debtor", back_populates="currency")
    creditor = relationship("Creditor", back_populates='currency')
    debtor_transaction = relationship('DebtorTransaction', back_populates='currency')
    creditor_transaction = relationship('CreditorTransaction', back_populates='currency')
    debtor_allocation = relationship('DebtorAllocation', back_populates='currency')
    creditor_allocation = relationship('CreditorAllocation', back_populates='currency')
    debtor_invoice_line = relationship('DebtorInvoiceLine', back_populates='currency')
    sales_order = relationship('SalesOrder', back_populates='currency')
    creditor_invoice_line = relationship('CreditorInvoiceLine', back_populates='currency')
    gl_account = relationship('GLAccount', back_populates='currency')
    gl_transaction = relationship('GLTransaction', back_populates='currency')

class RetailChannel(Base):
    __table__ = debtor_group_table
    debtor = relationship("Debtor", back_populates="retailchannel")


class AdvertisingGroup(Base):
    __table__ = debtor_group2_table
    debtor = relationship("Debtor", back_populates="advertisinggroup")

class Retailer(Base):
    __table__ = debtor_group3_table
    debtor = relationship("Debtor", back_populates="retailer")

class RetailGroup(Base):
    __table__ = retail_group_table
    debtor = relationship("Debtor", back_populates="retailgroup")

class CreditStatus(Base):
    __table__ = credit_status_table
    debtor = relationship("Debtor", back_populates="creditstatus")
    creditor = relationship('Creditor', back_populates='creditstatus')

class Staff(Base):
    __table__ = staff_table
    debtor_transaction = relationship('DebtorTransaction', back_populates='staff')

class Narrative(Base):
    __table__ = narrative_table
    debtor_transaction = relationship('DebtorTransaction', back_populates='narrative')
    debtor_invoice_line = relationship('DebtorInvoiceLine', back_populates='narrative')
    sales_order = relationship('SalesOrder', back_populates='narrative')
    creditor_invoice_line = relationship('CreditorInvoiceLine', back_populates='narrative')
    gl_transaction = relationship('GLTransaction', back_populates='narrative')

class Branch(Base):
    __table__ = branch_table
    debtor_transaction = relationship('DebtorTransaction', back_populates='branch')
    creditor_transaction = relationship('CreditorTransaction', back_populates='branch')
    debtor_invoice_line = relationship('DebtorInvoiceLine', back_populates='branch')
    sales_order = relationship('SalesOrder', back_populates='branch')
    sales_order_line = relationship('SalesOrderLine', back_populates='branch')
    creditor_invoice_line = relationship('CreditorInvoiceLine', back_populates='branch')

class Period(Base):
    __table__ = period_status_table
    debtor_transaction = relationship('DebtorTransaction', back_populates='period')
    creditor_transaction = relationship('CreditorTransaction', back_populates='period')
    gl_transaction = relationship('GLTransaction', back_populates='period')

class DebtorTransaction(Base):
    __table__ = debtor_transaction_table
    debtor = relationship("Debtor", back_populates="debtor_transaction")
    branch = relationship('Branch', back_populates='debtor_transaction')
    currency = relationship('Currency', back_populates='debtor_transaction')
    gl_batch = relationship('GLBatch', back_populates='debtor_transaction')
    narrative = relationship('Narrative', back_populates='debtor_transaction')
    period = relationship('Period', back_populates='debtor_transaction')
    staff = relationship('Staff', back_populates='debtor_transaction')
    sales_order = relationship('SalesOrder', back_populates='debtor_transaction')
    debtor_invoice_line = relationship('DebtorInvoiceLine', back_populates='debtor_transaction')

class DebtorAllocation(Base):
    __table__ = debtor_allocation_table
    currency = relationship('Currency', back_populates='debtor_allocation')

class StockGroup(Base):
    __table__ = stock_group_table
    stock_item = relationship('StockItem', back_populates='stock_group')

class StockItem(Base):
    __table__ = stock_item_table
    stock_group = relationship('StockGroup', back_populates='stock_item')
    debtor_invoice_line = relationship('DebtorInvoiceLine', back_populates='stock_item')
    sales_order_line = relationship('SalesOrderLine', back_populates='stock_item')
    creditor_invoice_line = relationship('CreditorInvoiceLine', back_populates='stock_item')

class DebtorInvoiceLine(Base):
    __table__ = debtor_invoiceline_table
    debtor = relationship('Debtor', back_populates='debtor_invoice_line')
    branch = relationship('Branch', back_populates='debtor_invoice_line')
    currency = relationship('Currency', back_populates='debtor_invoice_line')
    debtor_transaction = relationship('DebtorTransaction', back_populates='debtor_invoice_line')
    narrative = relationship('Narrative', back_populates='debtor_invoice_line')
    stock_item = relationship('StockItem', back_populates='debtor_invoice_line')


class SalesOrder(Base):
    __table__ = sales_order_table
    debtor_transaction = relationship('DebtorTransaction', back_populates='sales_order')
    debtor = relationship('Debtor', back_populates='sales_order')
    branch = relationship('Branch', back_populates='sales_order')
    currency = relationship('Currency', back_populates='sales_order')
    narrative = relationship('Narrative', back_populates='sales_order')
    sales_order_line = relationship('SalesOrderLine', back_populates='sales_order')


class SalesOrderLine(Base):
    __table__ = sales_orderline_table
    debtor = relationship('Debtor', back_populates='sales_order_line')
    branch = relationship('Branch', back_populates='sales_order_line')
    sales_order = relationship('SalesOrder', back_populates='sales_order_line')
    stock_item = relationship('StockItem', back_populates='sales_order_line')

class CreditorGroup(Base):
    __table__ = creditor_group_table
    creditor = relationship('Creditor', back_populates='creditor_group')

class Creditor(Base):
    __table__ = creditor_account_table
    currency = relationship("Currency", back_populates='creditor')
    creditor_group = relationship('CreditorGroup', back_populates='creditor')
    creditstatus = relationship('CreditStatus', back_populates='creditor')
    creditor_invoice_line = relationship('CreditorInvoiceLine', back_populates='creditor')
    creditor_transaction = relationship('CreditorTransaction', back_populates='creditor')

class CreditorInvoiceLine(Base):
    __table__ = creditor_invoiceline_table
    creditor = relationship('Creditor', back_populates='creditor_invoice_line')
    branch = relationship('Branch', back_populates='creditor_invoice_line')
    currency = relationship('Currency', back_populates='creditor_invoice_line')
    creditor_transaction = relationship('CreditorTransaction', back_populates='creditor_invoice_line')
    narrative = relationship('Narrative', back_populates='creditor_invoice_line')
    stock_item = relationship('StockItem', back_populates='creditor_invoice_line')

class CreditorTransaction(Base):
    __table__ = creditor_transaction_table
    creditor_invoice_line = relationship('CreditorInvoiceLine', back_populates='creditor_transaction')
    creditor = relationship('Creditor', back_populates='creditor_transaction')
    branch = relationship('Branch', back_populates='creditor_transaction')
    currency = relationship('Currency', back_populates='creditor_transaction')
    period = relationship('Period', back_populates='creditor_transaction')

class CreditorAllocation(Base):
    __table__ = creditor_allocation_table
    currency = relationship('Currency', back_populates='creditor_allocation')

class GLAccount(Base):
    __table__ = gl_account_table
    currency = relationship('Currency', back_populates='gl_account')
    gl_subaccount = relationship('GLSubAccount', back_populates='gl_account')
    gl_transaction = relationship('GLTransaction', back_populates='gl_account')

class GLBatch(Base):
    __table__ = gl_batch_table
    debtor_transaction = relationship('DebtorTransaction', back_populates='gl_batch')
    gl_transaction = relationship('GLTransaction', back_populates='gl_batch')

class GLTransaction(Base):
    __table__ = gl_transaction_table
    gl_account = relationship('GLAccount', back_populates='gl_transaction')
    gl_batch = relationship('GLBatch', back_populates='gl_transaction')
    currency= relationship('Currency', back_populates='gl_transaction')
    narrative = relationship('Narrative', back_populates='gl_transaction')
    period = relationship('Period', back_populates='gl_transaction')

class GLSubAccount(Base):
    __table__ = gl_subaccount_table
    gl_account = relationship('GLAccount', back_populates='gl_subaccount')