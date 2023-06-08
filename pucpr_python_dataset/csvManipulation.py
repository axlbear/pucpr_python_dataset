import csv

class Report:
    def __init__(self, CrashID, RegMonth, RegYear, RegDay, RegWeekDay):
        self.CrashID = CrashID
        self.RegMonth = RegMonth
        self.RegYear = RegYear
        self.RegDay = RegDay
        self.RegWeekDay = RegWeekDay

accidentReport = []

with open('car_accident_AUS.csv', 'r') as CSVfile:
    reader = csv.DictReader(CSVfile)

    for row in reader:
        accident = Report(int(row['CrashID']), row['RegMonth'], int(row['RegYear']), row['RegDay'], row['RegWeekDay'])
        accidentReport.append(accident)

# Teste para as informações adicionadas a Lista accidentReport
# for i in accidentReport:
#     print(f"{i.CrashID} - {i.RegMonth} - {i.RegYear} - {i.RegDay} - {i.RegWeekDay}")