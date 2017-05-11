import csv
import datetime

class NewTask:
    # create new tasks with name, timestamp and notes
    def __init__(self, task_name, task_notes, time_spent):
        self.task_name = task_name
        self.task_notes = task_notes
        self.time_spent = time_spent
        self.time_stamp = datetime.datetime.now().strftime('%m/%d/%Y')
        with open('work_log.csv', 'a') as csvfile:
            fieldnames = ['Date', 'Task Name', 'Task Notes', 'Time Spent']
            taskwriter = csv.writer(csvfile, fieldnames=fieldnames)
            taskwriter.writerow({
                'Date' : self.time_stamp,
                'Task Name' : task_name,
                'Task Notes' : task_notes,
                'Time Spent' : time_spent
            })
