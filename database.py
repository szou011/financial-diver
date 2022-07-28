from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///./database/exo.db", echo=False, future=True)


with engine.connect() as conn:
    result = conn.execute(text("""
        SELECT GLTRANS.ACCNO, 
GLTRANS.SUBACCNO, 
                GLTRANS.TRANSDATE, 
                GLTRANS.CHQNO, 
                GLTRANS.BATCHNO,
                GLTRANS.INVNO, 
                GLTRANS.DETAILS, 
                GLTRANS.AMOUNT, 
                GLTRANS.FCAMOUNT, 
                CURRENCIES.CURRCODE,
                PERIOD_STATUS.PERIODNAME, 
                GLTRANS.SOURCE, 
                GLTRANS.SOURCE_ACCNO, 
                DR_ACCS.NAME
FROM GLTRANS GLTRANS
      LEFT OUTER JOIN DR_ACCS DR_ACCS ON 
     (DR_ACCS.ACCNO = GLTRANS.SOURCE_ACCNO)
      LEFT OUTER JOIN PERIOD_STATUS ON 
     (PERIOD_STATUS.SEQNO = GLTRANS.PERIOD_SEQNO)
      LEFT OUTER JOIN CURRENCIES ON 
     (CURRENCIES.CURRENCYNO = GLTRANS.CURRENCYNO)
WHERE ( GLTRANS.ACCNO = 41367 )
AND ( GLTRANS.PERIOD_SEQNO >= 572 )
AND ( GLTRANS.PERIOD_SEQNO <= 600 )
       AND (( GLTRANS.SOURCE = 'd' ) OR ( GLTRANS.SOURCE = 'B' ))
        """))
        

    for row in result:
        print(f"ACCNO: {row.ACCNO}  NAME: {row.NAME} AMOUNT: {row.AMOUNT} ")

    