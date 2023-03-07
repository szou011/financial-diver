from sqlalchemy import MetaData, Table, Column, Integer, String, Float, Date, DateTime, ForeignKey

metadata_obj = MetaData()

debtor_account_table = Table(
    "DR_ACCS",
    metadata_obj,
    Column("ACCNO", Integer, primary_key=True),
    Column("ACCGROUP", Integer, ForeignKey('DR_ACCGROUPS.ACCGROUP')),
    Column("CURRENCYNO", Integer, ForeignKey('CURRENCIES.CURRENCYNO')),
    Column("HEAD_ACCNO", Integer),
    Column("NAME", String),
)

currency_table = Table(
    "CURRENCIES",
    metadata_obj,
    Column("CURRENCYNO", Integer, primary_key=True),
    Column("CURRCODE", String),
    Column("CURRNAME", String),
)

debtor_group_table = Table(
    "DR_ACCGROUPS",
    metadata_obj,
    Column("ACCGROUP", Integer, primary_key=True),
    Column("GROUPNAME", String),
)

period_status_table = Table(
    "PERIOD_STATUS",
    metadata_obj,
    Column("SEQNO", Integer, primary_key=True),
    Column("PERIODNAME", String),
    Column("YEARAGE", Integer),
    Column("AGE", Integer),
)

debtor_transaction_table = Table(
    "DR_TRANS",
    metadata_obj,
    Column("SEQNO", Integer, primary_key=True),
    Column("ACCNO", Integer, ForeignKey('DR_ACCS.ACCNO')),
    Column("AMOUNT", Float),
    Column("CURRENCYNO", Integer, ForeignKey('CURRENCIES.CURRENCYNO')),
    Column("EXCHRATE", Float),
    Column("INVNO", String),
    Column("PERIOD_SEQNO", Integer, ForeignKey('PERIOD_STATUS.SEQNO')),
    Column("REF1", String),
    Column("REF2", String),
    Column("REF3", String),
    Column("SUBTOTAL", Float),
    Column("SALES_ACCNO", Integer, ForeignKey('DR_ACCS.ACCNO')),
    Column("TAXTOTAL", Float),
    Column("TRANSDATE", Date),
    Column("TRANSTYPE", Integer, ForeignKey('TRANS_TYPE.SEQNO')),
)

stock_item_table = Table(
    "STOCK_ITEMS",
    metadata_obj,
    Column("STOCKCODE", String, primary_key=True),
    Column("DESCRIPTION", String),
)

debtor_invoiceline_table = Table(
    "DR_INVLINES",
    metadata_obj,
    Column("SEQNO", Integer, primary_key=True),
    Column("HDR_SEQNO", Integer, ForeignKey('DR_TRANS.SEQNO')),
    Column("INVNO", String),
    Column("ORDERQTY", Integer),
    Column("STOCKCODE", String, ForeignKey('STOCK_ITEMS.STOCKCODE')),
    Column("DESCRIPTION", String),
    Column("CURRENCYNO", Integer, ForeignKey('CURRENCIES.CURRENCYNO')),
    Column("EXCHRATE", Float),
    Column("UNITPRICE", Float),
    Column("DISCOUNT", Float),
    Column("LINETOTAL", Float),
    Column("LINETOTAL_TAX", Float),
    Column("LINETOTAL_INCTAX", Float),
)

transaction_type_table = Table(
    "TRANS_TYPE",
    metadata_obj,
    Column("SEQNO", Integer, primary_key=True),
    Column("TRANSACTION_TYPE", String),
    )