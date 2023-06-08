import sqlite3

database = sqlite3.connect('pucpr_python_dataset/CarAccidentAUS.db')
connectorDB = database.cursor()

connectorDB.execute('''CREATE TABLE IF NOT EXISTS CarAccidentReport 
                    (CrashID INTEGER PK,
                    RegMonth TEXT,
                    RegYear TEXT,
                    RegDay TEXT,
                    RegWeekDay TEXT);''')

database.commit()