import csv
import datetime

class GetTask:
    def __init__(self):
        self.data = open('work_log.csv', 'r')
        self.taskreader = csv.reader(self.data)
        self.rows = list(self.taskreader)

    def print_all(self):
        print(self.rows)

    def available_dates(self):
        list_available_dates = []
        for i in range(1, len(self.rows)):
            list_available_dates.append(self.rows[i][0])
        return list_available_dates

    def by_date(self, date):
        for i in range(1, len(self.rows)):
            if date == self.rows[i][0]:
                print (self.rows[i])

    def by_time_spent(self, time_spent):
        time_spent = str(time_spent)
        for i in range(1, len(self.rows)):
            if time_spent == self.rows[i][3]:
                print (self.rows[i])