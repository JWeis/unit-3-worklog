from create_tasks import Task
from get_tasks import GetTask


def end_app():
    choice = input("Would you like to run app again or quit? 1: Run Again, 2: Quit")
    if choice == '1':
        app()
    else:
        quit()


def app():
    global COUNT
    start = input("Welcome Please select what you would like to do: "
                      "1: Add New Employee Work Log, 2: Review Work Log  ")
    if start == '1':
        print("To add a new employee word log please enter their name")
        emp_name = input("Employee Name (letters only please):  ")
        new_work_log = Task(emp_name)
        print("Your work log for {} has been created!".format(emp_name))
        tasks = input("Would you like to add a task to {} work log?: 1: Yes, 2: No  ".format(emp_name))
        if tasks == "1":
            task_name = input("Task Name:  ")
            task_notes = input("Task Notes: ")
            time_spent = input("Time Spent in Minutes:  ")
            new_work_log.new_task(task_name, task_notes, time_spent)
            print("Your new task for {} has been created!".format(emp_name))

            end_app()

    if start == '2':
        # run get_tasks
        work_log = input("What is the name of the employee?  ")
        emp_csv = work_log+'_work_log.csv'
        emp_log = GetTask(emp_csv)
        print("You now have {} work log. ".format(work_log))
        first_action = input("Would you like to search {} logs by: 1: Date, 2: Time Spent, 3: Exact Search,"
                             " 4: Pattern Match  ".format(work_log))
        if first_action == '1':
            print("Here are the available dates of logs to choose from:")
            available_dates = emp_log.available_dates()
            print(available_dates)
            chosen_date = input("Which date would your like to search by? Please use exact formatting as shown:  ")
            logs_by_date = emp_log.by_date(chosen_date)
            for log in logs_by_date:
                print("\nDate: {} \n\n Task Name: {} \n Task Notes: {} \n Time Spend: {} \n\n".format(log['Date'],
                                                                                                    log['Task Name'],
                                                                                                    log['Task Notes'],
                                                                                                    log['Time Spent']))
        if first_action == '2':
            print("Here are the available dates of logs to choose from:")
            available_times = emp_log.av_times()
            print(available_times)
            chosen_time = input("Which duration of time would your like to search by? "
                                "Please use exact formatting as shown:  ")
            logs_by_time = emp_log.by_time_spent(chosen_time)
            for log in logs_by_time:
                print("\nDate: {} \n\n Task Name: {} \n Task Notes: {} \n Time Spend: {} \n\n".format(log['Date'],
                                                                                                      log['Task Name'],
                                                                                                      log['Task Notes'],
                                                                                                      log['Time Spent']))
        if first_action == '3':
            search_query = input("Please enter the exact query you would like to search:  ")
            exact_search = emp_log.exact_match(search_query)
            for log in exact_search:
                print("\nDate: {} \n\n Task Name: {} \n Task Notes: {} \n Time Spend: {} \n\n".format(log['Date'],
                                                                                                      log['Task Name'],
                                                                                                      log['Task Notes'],
                                                                                                      log['Time Spent']))
        if first_action == '4':
            pattern_query = input("Please enter the exact query you would like to search:  ")
            pattern_search = emp_log.pattern_match(pattern_query)
            for log in pattern_search:
                print("\nDate: {} \n\n Task Name: {} \n Task Notes: {} \n Time Spend: {} \n\n".format(log['Date'],
                                                                                                      log['Task Name'],
                                                                                                      log['Task Notes'],
                                                                                                      log['Time Spent']))
app()
