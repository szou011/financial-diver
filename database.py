from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///./database/exo.db", echo=True, future=True)


with engine.connect() as conn:
    result = conn.execute(text("SELECT ACCNO, NAME FROM DR_ACCS"))

    for row in result:
        print(f"ACCNO: {row.ACCNO}  NAME: {row.NAME}")

    