import csv
import datetime

class GetTask:
    def __init__(self):
        self.data = open('work_log.csv', 'r')
        self.taskreader = csv.reader(self.data)
        self.rows = list(self.taskreader)

    def print_all(self):
        print(self.rows)

    def by_date(self, date):
        for i in range(1, len(self.rows)):
            if date == self.rows[i][0]:
                print (self.rows[i])