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
MonthsOfYear = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for x in MonthsOfYear:
    connectorDB.execute(f"SELECT COUNT(*) AS AccidentsPerYear FROM CarAccidentReport WHERE RegYear = \"{x}\";")

