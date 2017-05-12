import csv


class GetTask:
    def __init__(self, filename):
        self.filename = filename
        self.data = open(filename, 'r')
        self.task_reader = csv.DictReader(self.data, delimiter=',')
        self.rows = list(self.task_reader)

    def print_all(self):
        return (self.rows)

    def available_dates(self):
        for row in self.rows[:]:
            print(row['Date'])

    def by_date(self, date):
        print("\nTask by date created\n")
        for row in self.rows[:]:
            check_date = row['Date']
            if check_date == date:
                return row

    def by_time_spent(self, time_spent):
        print("\nTask by time spent\n")
        print(self.rows[0])
        time_spent = str(time_spent)
        for i in range(1, len(self.rows)):
            if time_spent == self.rows[i][3]:
                print (self.rows[i], '\n')

    def exact_match(self, string):
        string_list = string.split()
        output = []
        for a in range(len(string_list)):
            for i in range(len(self.rows)):
                if string_list[a] in self.rows[i][i]:
                    output.append(self.rows[i])
                else: print('no matches')
        print(output)

james = GetTask("Jim_work_log.csv")

james.available_dates()
james.by_date('05/12/2017')

#test = james.print_all()