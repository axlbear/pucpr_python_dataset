from databaseInitiator import *
from csvManipulation import *

# Usado para popular a base de dados. Executar apenas se for criada a base do zero.

# countRows = 0
# connectorDB.execute("BEGIN TRANSACTION;")
# for i in accidentReport:
#     countRows += 1 # 52843 total de Linhas
#     print(countRows)
#     connectorDB.execute(f"INSERT INTO CarAccidentReport (CrashID, RegMonth, RegYear, RegDay, RegWeekDay) VALUES({i.CrashID}, \"{i.RegMonth}\", \"{i.RegYear}\", \"{i.RegDay}\", \"{i.RegWeekDay}\");")

# connectorDB.execute("COMMIT;")

def AccidentsPerYear():
    years = connectorDB.execute("SELECT COUNT(1), RegYear FROM CarAccidentReport GROUP BY RegYear ORDER BY RegYear;")
    rows = years.fetchall()

    for row in rows:
        print(f"No ano {row[1]}, foram registrados {row[0]} acidentes.")

    database.commit()

connectorDB.executescript("""
--DROP TABLE IF EXISTS Total_Year;
--DROP TABLE IF EXISTS Total_Month_Year;
CREATE TEMP TABLE Total_Year AS SELECT COUNT(1) AS TotalY, RegYear FROM CarAccidentReport GROUP BY RegYear ORDER BY RegYear;
CREATE TEMP TABLE Total_Month_Year AS SELECT COUNT(1) AS TotalM, RegYear, RegMonth FROM CarAccidentReport GROUP BY RegYear, RegMonth ORDER BY RegMonth;
SELECT (CAST(tmy.TotalM AS REAL) / CAST(ty.TotalY AS REAL) * 100) AS Percentage, tmy.RegMonth, tmy.RegYear FROM Total_Month_Year tmy JOIN Total_Year ty ON tmy.RegYear = ty.RegYear ORDER BY tmy.RegYear;
""")

rows = connectorDB.fetchall()

try:
    for row in rows:
        print(row)
except Exception as error:
    print(error)
