from sqlalchemy import MetaData, Table, Column, Integer, String, Float, Date, DateTime, ForeignKey

exo_metadata = MetaData()

debtor_account_table = Table(
    "DR_ACCS",
    exo_metadata,
    Column("ACCGROUP", Integer, ForeignKey('DR_ACCGROUPS.ACCGROUP')),
    Column("ACCGROUP2", Integer, ForeignKey('DR_ACCGROUP2S.ACCGROUP')),
    Column("ACCNO", Integer, primary_key=True),
    Column("ALPHACODE", String),
    Column("CURRENCYNO", Integer, ForeignKey('CURRENCIES.CURRENCYNO')),
    Column("HEAD_ACCNO", Integer),
    Column("ISACTIVE", String),
    Column("NAME", String),
    Column("STOPCREDIT", String),
    Column("X_DRACCGROUP3", Integer, ForeignKey('X_DR_ACCGROUP3S.ACCGROUP')),
    Column("X_RETAILGROUP", Integer, ForeignKey('X_RETAILGROUP.GROUPNO')),
    Column("CREDITSTATUS", Integer, ForeignKey('CREDIT_STATUSES.STATUSNO')),
)

currency_table = Table(
    "CURRENCIES",
    exo_metadata,
    Column("CURRENCYNO", Integer, primary_key=True),
    Column("CURRCODE", String),
    Column("CURRNAME", String),
)

debtor_group_table = Table(
    "DR_ACCGROUPS",
    exo_metadata,
    Column("ACCGROUP", Integer, primary_key=True),
    Column("GROUPNAME", String),
)

debtor_group2_table = Table(
    "DR_ACCGROUP2S",
    exo_metadata,
    Column("ACCGROUP", Integer, primary_key=True),
    Column("GROUPNAME", String),
)

debtor_group3_table = Table(
    "X_DR_ACCGROUP3S",
    exo_metadata,
    Column("ACCGROUP", Integer, primary_key=True),
    Column("GROUPNAME", String),
    Column("REBATE_LOGISTICS", Float),
    Column("REBATE_MKTG", Float),
    Column("REBATE_REMIT", Float),
    Column("REBATE_VOLUME", Float),
    Column("SETT_DISC", Float),
)

credit_status_table = Table(
    "CREDIT_STATUSES",
    exo_metadata,
    Column("STATUSNO", Integer, primary_key=True),
    Column("STATUSDESC", String),
    Column("ACTIVE_DR", String),
    Column("ACTIVE_CR", String),
)

retail_group_table = Table(
    "X_RETAILGROUP",
    exo_metadata,
    Column("GROUPNO", Integer, primary_key=True, unique=True),
    Column("GROUPNAME", String),
)

staff_table = Table(
    "STAFF",
    exo_metadata,
    Column("STAFFNO", Integer, primary_key=True),
    Column("NAME", String),
)

narrative_table = Table(
    "NARRATIVES",
    exo_metadata,
    Column("SEQNO", Integer, primary_key=True),
    Column("NARRATIVE", String),
)

branch_table = Table(
    "BRANCHES",
    exo_metadata,
    Column("BRANCHNO", Integer, primary_key=True),
    Column("BRANCHNAME", String),
)

period_status_table = Table(
    "PERIOD_STATUS",
    exo_metadata,
    Column("LEDGER", String),
    Column("MINGLSEQNO", Integer),
    Column("MINORDLINESEQNO", Integer),
    Column("MINORDSEQNO", Integer),
    Column("MINSTOCKSEQNO", Integer),
    Column("MINTRANSEQNO", Integer),
    Column("MINTRANLINESEQNO", Integer),
    Column("PERIODNAME", String),
    Column("SEQNO", Integer, primary_key=True),
    Column("STARTDATE", Date),
    Column("STOPDATE", Date),
)

debtor_transaction_table = Table(
    "DR_TRANS",
    exo_metadata,
    Column("ACCNO", Integer, ForeignKey('DR_ACCS.ACCNO')),
    Column("ALLOCATED", Integer),
    Column("ALLOCATEDBAL", Float),
    Column("AMOUNT", Float),
    Column("ANALYSIS", String),
    Column("BATCHNO", Integer),
    Column("BRANCH_ACCNO", Integer),
    Column("BRANCHNO", Integer, ForeignKey('BRANCHES.BRANCHNO')),
    Column("CURRENCYNO", Integer, ForeignKey('CURRENCIES.CURRENCYNO')),
    Column("CUSTORDERNO", String),
    Column("EXCHRATE", Float),
    Column("GLBATCHNO", Integer, ForeignKey('GLBATCH.BATCHNO')),
    Column("GLCODE", Integer),
    Column("GLPOSTED", String),
    Column("INVNO", String),
    Column("NARRATIVE_SEQNO", Integer, ForeignKey('NARRATIVES.SEQNO')),
    Column("ORD_REF", String),
    Column("PERIOD_SEQNO", Integer, ForeignKey('PERIOD_STATUS.SEQNO')),
    Column("PHYS_STAFF", Integer, ForeignKey('STAFF.STAFFNO')),
    Column("POSTTIME", DateTime),
    Column("REF1", String),
    Column("REF2", String),
    Column("REF3", String),
    Column("SEQNO", Integer, primary_key=True),
    Column("SESSION_ID", Integer),
    Column("SO_SEQNO", Integer, ForeignKey('SALESORD_HDR.SEQNO')),
    Column("SUBTOTAL", Float),
    Column("TAXINC", String),
    Column("TAXRATE", Float),
    Column("TAXTOTAL", Float),
    Column("TRANSDATE", Date),
    Column("TRANSTYPE", Integer),
    Column("X_RA_CLAIMREF", String),
)

debtor_allocation_table = Table(
    "DR_ALLOCATIONS",
    exo_metadata,
    Column("SEQNO", Integer, primary_key=True),
    Column("ALLOCNO", Integer, primary_key=True),
    Column("TRANS_SEQNO", Integer),
    Column("AMOUNT", Float),
    Column("CURRENCY", Integer, ForeignKey('CURRENCIES.CURRENCYNO')),
    Column("TAKENUP", String),
    Column("EXCHRATE", Float),
)

stock_group_table = Table(
    "STOCK_GROUPS",
    exo_metadata,
    Column("GROUPNO", Integer, primary_key=True),
    Column("GROUPNAME", String),
)

stock_item_table = Table(
    "STOCK_ITEMS",
    exo_metadata,
    Column("STOCKCODE", String, primary_key=True),
    Column("DESCRIPTION", String),
    Column("STOCKGROUP", Integer, ForeignKey('STOCK_GROUPS.GROUPNO')),
)

debtor_invoiceline_table = Table(
    "DR_INVLINES",
    exo_metadata,
    Column("ACCNO", Integer, ForeignKey('DR_ACCS.ACCNO')),
    Column("ANALYSIS", String),
    Column("BRANCHNO", Integer, ForeignKey('BRANCHES.BRANCHNO')),
    Column("CURRENCYNO", Integer, ForeignKey('CURRENCIES.CURRENCYNO')),
    Column("DESCRIPTION", String),
    Column("DRINVLINEID", Integer),
    Column("EXCHRATE", Float),
    Column("HDR_SEQNO", Integer, ForeignKey('DR_TRANS.SEQNO')),
    Column("INVNO", String),
    Column("LINE_SOURCE", Integer),
    Column("LINETOTAL", Float),
    Column("LINETOTAL_INCTAX", Float),
    Column("LINETOTAL_TAX", Float),
    Column("NARRATIVE_SEQNO", Integer, ForeignKey('NARRATIVES.SEQNO')),
    Column("QUANTITY", Integer),
    Column("SEQNO", Integer, primary_key=True),
    Column("STOCKCODE", String, ForeignKey('STOCK_ITEMS.STOCKCODE')),
    Column("TAXRATE", Float),
    Column("TRANSDATE", Date),
    Column("UNITPRICE", Float),
)

sales_order_table = Table(
    "SALESORD_HDR",
    exo_metadata,
    Column("ACCNO", Integer, ForeignKey('DR_ACCS.ACCNO')),
    Column("BRANCHNO", Integer, ForeignKey('BRANCHES.BRANCHNO')),
    Column("CREATE_DATE", Date),
    Column("CURRENCYNO", Integer, ForeignKey('CURRENCIES.CURRENCYNO')),
    Column("CUSTORDERNO", String),
    Column("EXCHRATE", Float),
    Column("FINALISATION_DATE", Date),
    Column("NARRATIVE_SEQNO", Integer, ForeignKey('NARRATIVES.SEQNO')),
    Column("ORDERDATE", Date),
    Column("ORDTOTAL", Float),
    Column("REFERENCE", String),
    Column("SEQNO", Integer, primary_key=True),
    Column("STATUS", Integer),
    Column("SUBTOTAL", Float),
    Column("TAXTOTAL", Float),
)

sales_orderline_table = Table(
    "SALESORD_LINES",
    exo_metadata,
    Column("ACCNO", Integer, ForeignKey('DR_ACCS.ACCNO')),
    Column("ANALYSIS", String),
    Column("BRANCHNO", Integer, ForeignKey('BRANCHES.BRANCHNO')),
    Column("DESCRIPTION", String),
    Column("DUEDATE", Date),
    Column("HDR_SEQNO", Integer, ForeignKey('SALESORD_HDR.SEQNO')),
    Column("LINETOTAL", Float),
    Column("ORD_QUANT", Integer),
    Column("SEQNO", Integer, primary_key=True),
    Column("SOLINEID", Integer),
    Column("STOCKCODE", String, ForeignKey('STOCK_ITEMS.STOCKCODE')),
    Column("TAXRATE", Float),
    Column("UNITPRICE", Float),
)

creditor_group_table = Table(
    "CR_ACCGROUPS",
    exo_metadata,
    Column("ACCGROUP", Integer, primary_key=True),
    Column("GROUPNAME", String),
)

creditor_account_table = Table(
    "CR_ACCS",
    exo_metadata,
    Column("ACCNO", Integer, primary_key=True),
    Column("NAME", String),
    Column("CURRENCYNO", Integer, ForeignKey('CURRENCIES.CURRENCYNO')),
    Column("CREDITSTATUS", Integer, ForeignKey('CREDIT_STATUSES.STATUSNO')),
    Column("ACCGROUP", Integer, ForeignKey('CR_ACCGROUPS.ACCGROUP')),
)

creditor_invoiceline_table = Table(
    "CR_INVLINES",
    exo_metadata,
    Column("ACCNO", Integer, ForeignKey('CR_ACCS.ACCNO')),
    Column("BRANCHNO", Integer, ForeignKey('BRANCHES.BRANCHNO')),
    Column("CRINVLINEID", Integer),
    Column("CURRENCYNO", Integer, ForeignKey('CURRENCIES.CURRENCYNO')),
    Column("DESCRIPTION", String),
    Column("EXCHRATE", Float),
    Column("GLACCNO", Integer),
    Column("HDR_SEQNO", Integer, ForeignKey('CR_TRANS.SEQNO')),
    Column("INVNO", String),
    Column("LINETOTAL", Float),
    Column("LINETOTAL_TAX", Float),
    Column("NARRATIVE_SEQNO", Integer, ForeignKey('NARRATIVES.SEQNO')),
    Column("QUANTITY", Integer),
    Column("SEQNO", Integer, primary_key=True),
    Column("STOCKCODE", String, ForeignKey('STOCK_ITEMS.STOCKCODE')),
    Column("TAXRATE", Float),
    Column("UNITPRICE", Float),
)

creditor_transaction_table = Table(
    "CR_TRANS",
    exo_metadata,
    Column("ACCNO", Integer, ForeignKey('CR_ACCS.ACCNO')),
    Column("ALLOCATED", Integer),
    Column("ALLOCATEDBAL", Integer),
    Column("AMOUNT", Float),
    Column("ANALYSIS", String),
    Column("BRANCHNO", Integer, ForeignKey('BRANCHES.BRANCHNO')),
    Column("CURRENCYNO", Integer, ForeignKey('CURRENCIES.CURRENCYNO')),
    Column("EXCHRATE", Float),
    Column("GLCODE", Integer),
    Column("GLPOSTED", String),
    Column("IMAGE_URL", String),
    Column("INVNO", String),
    Column("PERIOD_SEQNO", Integer, ForeignKey('PERIOD_STATUS.SEQNO')),
    Column("POSTTIME", DateTime),
    Column("REF1", String),
    Column("REF2", String),
    Column("REF3", String),
    Column("SEQNO", Integer, primary_key=True),
    Column("SESSION_ID", Integer),
    Column("SUBTOTAL", Float),
    Column("TAXRATE", Float),
    Column("TAXTOTAL", Float),
    Column("TRANSDATE", Date),
    Column("TRANSTYPE", Integer),
)

creditor_allocation_table = Table(
    "CR_ALLOCATIONS",
    exo_metadata,
    Column("SEQNO", Integer, primary_key=True),
    Column("ALLOCNO", Integer, primary_key=True),
    Column("TRANS_SEQNO", Integer),
    Column("AMOUNT", Float),
    Column("CURRENCY", Integer, ForeignKey('CURRENCIES.CURRENCYNO')),
    Column("TAKENUP", String),
    Column("EXCHRATE", Float),
)

gl_account_table = Table(
    "GLACCS",
    exo_metadata,
    Column("ACCNO", Integer, primary_key=True),
    Column("NAME", String),
    Column("ISACTIVE", String),
    Column("CURRENCYNO", Integer, ForeignKey('CURRENCIES.CURRENCYNO')),
)

gl_batch_table = Table(
    "GLBATCH",
    exo_metadata,
    Column("BATCHNO", Integer, primary_key=True),
    Column("NARRATIVE", String),
    Column("AUTO_REVERSE", String),
    Column("REVERSAL_OF_BATCHNO", Integer),
    Column("REVERSED_IN_BATCHNO", Integer),
)

gl_transaction_table = Table(
    "GLTRANS",
    exo_metadata,
    Column("ACCNO", Integer, ForeignKey('GLACCS.ACCNO')),
    Column("AMOUNT", Float),
    Column("BATCHNO", Integer, ForeignKey('GLBATCH.BATCHNO')),
    Column("CHQNO", String),
    Column("CURRENCYNO", Integer, ForeignKey('CURRENCIES.CURRENCYNO')),
    Column("DETAILS", String),
    Column("FCAMOUNT", Float),
    Column("INITIALS", String),
    Column("INVNO", String),
    Column("NARRATIVE_SEQNO", Integer, ForeignKey('NARRATIVES.SEQNO')),
    Column("PERIOD_SEQNO", Integer, ForeignKey('PERIOD_STATUS.SEQNO')),
    Column("POSTTIME", DateTime),
    Column("SEQNO", Integer, primary_key=True),
    Column("SESSION_ID", Integer),
    Column("SOURCE", String),
    Column("SOURCE_ACCNO", Integer),
    Column("SOURCE_INVLINEID", Integer),
    Column("SUBACCNO", Integer),
    Column("TRANSDATE", Date),
)

gl_subaccount_table = Table(
    "GLSUBACCS",
    exo_metadata,
    Column("ACCNO", Integer, ForeignKey('GLACCS.ACCNO')),
    Column("SUBACCNO", Integer),
    Column("FULLACCOUNT", String, primary_key=True),
    Column("NAME", String),
)
