from databaseInitiator import *
from csvManipulation import *

dicMonths = {
    1:"Janeiro",
    2:"Fevereiro",
    3:"Março",
    4:"Abril",
    5:"Maio",
    6:"Junho",
    7:"Julho",
    8:"Agosto",
    9:"Setembro",
    10:"Outubro",
    11:"Novembro",
    12:"Dezembro"
}

# Usado para popular a base de dados. Executar apenas se for criada a base do zero.

# countRows = 0
# connectorDB.execute("BEGIN TRANSACTION;")
# for i in accidentReport:
#     countRows += 1 # 52843 total de Linhas
#     print(countRows)
#     connectorDB.execute(f"INSERT INTO CarAccidentReport (CrashID, RegMonth, RegYear, RegDay, RegWeekDay) VALUES({i.CrashID}, \"{i.RegMonth}\", \"{i.RegYear}\", \"{i.RegDay}\", \"{i.RegWeekDay}\");")

# connectorDB.execute("COMMIT;")

def AcidentesPorAno():
    years = connectorDB.execute("SELECT COUNT(1), RegYear FROM CarAccidentReport GROUP BY RegYear ORDER BY RegYear;")
    rows = years.fetchall()
    database.commit()

    for row in rows:
        print(f"No ano {row[1]}, foram registrados {row[0]} acidentes.")

def PercentualPorMes():
    connectorDB.execute("DROP TABLE IF EXISTS Total_Year;")
    database.commit()
    connectorDB.execute("DROP TABLE IF EXISTS Total_Month_Year;")
    database.commit()
    connectorDB.execute("CREATE TEMP TABLE Total_Year AS SELECT COUNT(1) AS TotalY, RegYear FROM CarAccidentReport GROUP BY RegYear ORDER BY RegYear;")
    database.commit()
    connectorDB.execute("CREATE TEMP TABLE Total_Month_Year AS SELECT COUNT(1) AS TotalM, RegYear, RegMonth FROM CarAccidentReport GROUP BY RegYear, RegMonth ORDER BY RegMonth;")
    database.commit()
    perc = connectorDB.execute("SELECT (CAST(tmy.TotalM AS REAL) / CAST(ty.TotalY AS REAL) * 100) AS Percentage, tmy.RegMonth, tmy.RegYear FROM Total_Month_Year tmy JOIN Total_Year ty ON tmy.RegYear = ty.RegYear ORDER BY tmy.RegYear;")

    rows = perc.fetchall()

    for row in rows:
        print(f"Ano: {row[2]} - Mês: {dicMonths[row[1]]} - Porcentagem de Acidentes: {round(row[0], 2)}%")


