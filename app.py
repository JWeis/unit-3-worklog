from create_tasks import Task
from get_tasks import GetTask


def app():
    start = input("Welcome Please select what you would like to do: 1: Add New Employee Work Log, 2: Review Work Log")
    if start == '1':
        print("To add a new employee word log please enter their name")
        emp_name = input("Employee Name (letters only please):  ")
        new_work_log = Task(emp_name)
        print("Your work log for {} has been created!".format(emp_name))
        tasks = input("Would you like to add a task to {} work log?: 1: Yes, 2: No".format(emp_name))
        if tasks == "1":
            task_name = input("Task Name:  ")
            task_notes = input("Task Notes: ")
            time_spent = input("Time Spent in Minutes:  ")
            new_work_log.new_task(task_name, task_notes, time_spent)
    if start == '2':
        # run get_tasks
        work_log = input("What is the name of the employee?  ")
        emp_csv = work_log+'_work_log.csv'
        emp_log = GetTask(emp_csv)
        print("You now have {} work log. ".format(work_log))
        first_action = input("would you like to get all logs for {}? 1: Yes, 2: No  ".format(work_log))
        if first_action == '1':
            print(emp_log.print_all())


app()