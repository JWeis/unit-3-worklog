import csv
import datetime


class Task:
    # create new tasks with name, timestamp and notes
    def __init__(self):
        self.fieldnames = ['Date', 'Task Name', 'Task Notes', 'Time Spent']
        with open('work_log.csv', 'a') as csvfile:
            self.task_writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            #self.task_writer.writeheader()

    def new_task(self, task_name, task_notes, time_spent):
        created_date = datetime.datetime.now().strftime('%m/%d/%Y')
        with open('work_log.csv', 'a') as csvfile:
            self.task_writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            self.task_writer.writerow({
                'Date': created_date,
                'Task Name': task_name,
                'Task Notes': task_notes,
                'Time Spent': time_spent})

    def update_task(self, task, old_field, new_field):
        with open('work_log.csv', '+') as csvfile:
            get_task = task
            

    def del_task(self):
        pass