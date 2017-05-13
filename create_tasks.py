import csv
import datetime


class Task:
    # create new tasks with name, timestamp and notes
    def __init__(self, employee_name):
        self.employee_name = employee_name
        self.fieldnames = ['Date', 'Task Name', 'Task Notes', 'Time Spent']
        with open(employee_name + '_work_log.csv', 'a') as csvfile:
            self.task_writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            self.task_writer.writeheader()

    def new_task(self, task_name, task_notes, time_spent):
        created_date = datetime.datetime.now().strftime('%m/%d/%Y')
        with open(self.employee_name + '_work_log.csv', 'a') as csvfile:
            self.task_writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            self.task_writer.writerow({
                'Date': created_date,
                'Task Name': task_name,
                'Task Notes': task_notes,
                'Time Spent': time_spent})

    def update_task(self):
        pass

    def del_task(self):
        pass