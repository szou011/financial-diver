from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///./database/exo.db", echo=False, future=True)


with engine.connect() as conn:
    result = conn.execute(text("""
        SELECT DR_ACCS.ACCGROUP, COUNT(DR_ACCS.ACCNO) TOTAL 
FROM DR_ACCS DR_ACCS
GROUP BY DR_ACCS.ACCGROUP
        """))

                                               
    acc_group = []
    group_count = []

    for row in result:
        acc_group.append(row.ACCGROUP)
        group_count.append(row.TOTAL)


print(acc_group)
print(group_count)