import os

from create_tasks import Task
from get_tasks import GetTask


my_log = Task()
emp_log = GetTask()
by_date = emp_log.by_date
by_time = emp_log.by_time_spent
by_exact = emp_log.exact_match
by_pattern = emp_log.pattern_match


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def end_app():
    choice = input("Would you like to run app again or quit? 1: Run Again, 2: Quit  ")
    if choice == '1':
        app()
    else:
        quit()


def add_task():
    task_name = input("Task Name:  ")
    task_notes = input("Task Notes: ")
    time_spent = input("Time Spent in Minutes:  ")
    my_log.new_task(task_name, task_notes, time_spent)
    clear()
    print("Your new task for has been created!")


def output(task_getter):
    for log in task_getter:
        print("\nDate: {} \n Task Name: {} \n Task Notes: {} \n Time Spend: {} \n\n".format(log['Date'],
                                                                                            log['Task Name'],
                                                                                            log['Task Notes'],
                                                                                            log['Time Spent']))


def app():
    clear()
    start = input("Please select what you would like to do: "
                  "1: Add to Work Log, 2: Review Work Log  ")
    if start == '1':
        add_task()
        while True:
            again = input("Would you like to add another task? 1: Yes, 2: No ")
            if again == '1':
                add_task()
            else:
                end_app()

    if start == '2':
        # run get_tasks
        first_action = input("Would you like to search your logs by: 1: Date, 2: Time Spent, 3: Exact Search,"
                             " 4: Pattern Match  ")
        if first_action == '1':
            print("Here are the available dates of logs to choose from:\n")
            available_dates = emp_log.available_dates()
            for date in available_dates:
                print(date)
            while True:
                chosen_date = input("\nWhich date would your like to search by? Please use exact formatting as shown:  ")
                if chosen_date in available_dates:
                    logs_by_date = by_date(chosen_date)
                    print("\nShowing all logs for {} date".format(chosen_date))
                    output(logs_by_date)
                    end_app()
                else:
                    print("\nPlease select a date provided. Please ensure the format MM/DD/YYYY is used.")

        if first_action == '2':
            print("Here are the available times in minutes of logs to choose from:\n")
            available_times = emp_log.av_times()
            for time in available_times:
                print(time, 'Minutes')
            while True:
                chosen_time = input("\nPlease enter which time duration you would like to search by:  ")
                if chosen_time in available_times:
                    logs_by_time = by_time(chosen_time)
                    output(logs_by_time)
                    end_app()
                else:
                    print("\nPlease select a time provided. Please ensure that only numbers are used. i.e '60'.")

        if first_action == '3':
            while True:
                search_query = input("\nPlease enter the exact query you would like to search:  ")
                exact_search = by_exact(search_query)
                if exact_search:
                    output(exact_search)
                    again = input("\nWould you like to try another Exact Search Query? 1: Yes, 2: No ")
                    if again == '1':
                        continue
                    else:
                        end_app()
                else:
                    print("\nNo logs found for that the query {}".format(search_query))
                    again = input("\nWould you like to try another Exact Search Query? 1: Yes, 2: No ")
                    if again == '1':
                        continue
                    else:
                        end_app()

        if first_action == '4':
            while True:
                pattern_query = input("Please enter the pattern query you would like to search:  ")
                pattern_search = by_pattern(pattern_query)
                if pattern_search:
                    output(pattern_search)
                    again = input("\nWould you like to try another Pattern Search Query? 1: Yes, 2: No ")
                    if again == '1':
                        continue
                    else:
                        end_app()
                else:
                    print("No logs found for that the query {}".format(pattern_query))
                    again = input("\nWould you like to try another Pattern Search Query? 1: Yes, 2: No ")
                    if again == '1':
                        continue
                    else:
                        end_app()

        else:
            pass
app()
