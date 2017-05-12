import csv
import re


class GetTask:
    def __init__(self, filename):
        self.filename = filename
        self.data = open(filename, 'r')
        self.task_reader = csv.DictReader(self.data, delimiter=',')
        self.rows = list(self.task_reader)

    def print_all(self):
        return (self.rows)

    def available_dates(self):
        output = []
        for row in self.rows[:]:
            if row['Date'] not in output:
                output.append(row['Date'])
            else:
                continue
        return output

    def by_date(self, date):
        output = []
        for row in self.rows[:]:
            check_date = row['Date']
            if check_date == date:
                output.append(row)
        return output

    def av_times(self):
        output = []
        for row in self.rows[:]:
            if row['Time Spent'] not in output:
                output.append(row['Time Spent'])
            else:
                continue
        return output

    def by_time_spent(self, time_spent):
        time_spent = str(time_spent)
        output = []
        for row in self.rows[:]:
            check_time = row['Time Spent']
            if check_time == time_spent:
                output.append(row)
        return output

    def exact_match(self, string):
        output = []
        for row in self.rows[:]:
            if string in row['Task Name']:
                output.append(row)
            if string in row['Task Notes']:
                output.append(row)
        return output

    def pattern_match(self, pattern):
        output = []
        for row in self.rows[:]:
            task_search = re.search(r'\b' + pattern + r'\b', row['Task Name'], re.I|re.VERBOSE)
            notes_search = re.search(r'\b' + pattern + r'\b', row['Task Notes'], re.I|re.VERBOSE)
            if task_search or notes_search:
                output.append(row)
        return output

