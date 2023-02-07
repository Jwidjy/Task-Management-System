#=====Importing Libraries===========
from datetime import date, datetime
today = date.today()

#=====Functions=====
def reg_user():
    # User input for new username, password, confirm password
    with open("user.txt", "a+") as user_file:
        while True:
            new_user = input("Enter new username: ")

            # Checks if new username exists in user.txt
            if new_user in login_credentials:
                print("Username exists already. Please enter new username.")
                continue

            new_pass = input("Enter new password: ")
            confirm_pass = input("Confirm new password: ")

            # If passwords match, add to user.txt file. If not, prompt again
            if new_pass == confirm_pass:
                user_file.write(f"\n{new_user}, {new_pass}")
                login_credentials[new_user] = new_pass
                print("\nSuccessfully added new user.")
                break
            else:
                print("Password doesn't match. Please try again.")
                continue

def add_task():
    with open("tasks.txt", "a+") as user_file:
        # User prompt for username assignee, checks if username exists in 
        # register, then prompts for task title, description, due date, then 
        # write to tasks.txt file
        while True:
            task_user = input("Enter username assigned to this task: ")
            if task_user in login_credentials:
                break
            else:
                print("Username not found in register. Please try again.")
        task_title = input("Enter title of this task: ")
        task_desc = input("Enter description of this task: ")

        # Ensures correct date format is inputted
        while True:
            try:
                task_date = input("Enter due date of the task (e.g. 10 Oct 2019): ")    

                (task_date != datetime.strptime(task_date, "%d %b %Y")
                .strptime(task_date, "%d %b %Y"))
                    
            except ValueError:
                    print("\nDate formatted incorrectly.\n")
            else:
                break
        
        today_formatted = todays_date()
        task_completion = "No"

        user_file.write(
            f"\n{task_user}, {task_title}, {task_desc}, {today_formatted}, "
            f"{task_date}, {task_completion}"
        )
        print("\nSuccessfully added new task.\n")

def view_all():
    with open("tasks.txt", "r") as user_file:
        # For each line in user_file, split into list elements, then assign
        # appropriate index values to respective categories, & format like Output 2
        for each_line in user_file:
            stripped = each_line.split(", ")
            print(
                f"{'-' * 50}\n\n"
                f"Task:                 {stripped[1]}\n"
                f"Assigned to:          {stripped[0]}\n"
                f"Date assigned:        {stripped[3]}\n"
                f"Due date:             {stripped[4]}\n"
                f"Task complete?        {stripped[5]}\n"
                f"Task description:\n"
                f"  {stripped[2]}\n\n"
                f"{'-' * 50}"
            )

def view_mine():
    with open("tasks.txt", "r") as user_file:
        lines = user_file.readlines()
        # Establish dicts for tasks, & for edit_task menu options for later
        task_dict = {}
        edit_task = {}

        # Assign tasks with number via enumerate()
        for index, task in enumerate(lines, start=1):
            task_dict[index] = task
            
            # Only print tasks assigned to user
            stripped = task.split(", ")
            if stripped[0] == login_user:
                edit_task[index] = stripped
                print(
                    f"{'-' * 50}\n\n"
                    f"Task number:          {index}\n"
                    f"Task:                 {stripped[1]}\n"
                    f"Assigned to:          {stripped[0]}\n"
                    f"Date assigned:        {stripped[3]}\n"
                    f"Due date:             {stripped[4]}\n"
                    f"Task complete?        {stripped[5]}\n"
                    f"Task description:\n"
                    f"  {stripped[2]}\n\n"
                    f"{'-' * 50}"
                )

        vm_task_options(lines, edit_task)

def vm_task_options(lines, edit_task):
    while True:
        vm_taskprompt = input(
            "\nEnter task number to select specific task, or enter '-1' to return "
            "to the main menu:\n"
        )

        # Checks to see if user-specific task exists in dict
        if int(vm_taskprompt) in edit_task:
            while True:
                menu = input(
                    "\nSelect one of the following options below:"
                    "\n1 - Mark task as complete"
                    "\n2 - Edit the task"
                    "\n3 - Go back"
                    "\n: "
                )

                # Mark task as complete route
                if menu == "1": 
                    with open("tasks.txt", "r") as output_file:
                        lines = output_file.readlines()
                    with open("tasks.txt", "w") as output_file:
                        output = ""
                        for each_line in lines:
                            stripped = each_line.split(", ")

                            # Ensures correct line is being edited
                            if edit_task[int(vm_taskprompt)] == stripped:
                                stripped[5] = "Yes\n"

                                # Write back to tasks.txt file
                                for each_element in stripped:
                                    output += (f"{each_element}, ")
                            else:
                                for each_element in stripped:
                                    output += (f"{each_element}, ")
                            output = output.rstrip(", ")
                        output_file.write(output)
                        print("\nSuccessfuly marked as complete.")

                # Edit task route
                elif menu == "2": 
                    # Open file to read updated version & enumerate
                    with open("tasks.txt", "r") as output_file:
                        lines = output_file.readlines()
                    task_dict = {}
                    edit_task = {}
                    for index, task in enumerate(lines, start=1):
                        task_dict[index] = task
                        
                        stripped = task.split(", ")
                        if stripped[0] == login_user:
                            edit_task[index] = stripped

                    # Validates if task has already been completed or not
                    while True:
                        if edit_task[int(vm_taskprompt)][5] == "Yes\n" or\
                            edit_task[int(vm_taskprompt)][5] == "Yes":
                            print(
                                "\nApologies, but this task has already been "
                                "completed."
                            )
                            break
                        options = input(
                            "\nSelect one of the following options below:"
                            "\n1 - Change assignee"
                            "\n2 - Change due date"
                            "\n3 - Go back"
                            "\n: "
                        )         

                        # Change assignee route
                        if options == "1": 
                            # Open file to read updated version
                            with open("tasks.txt", "r") as user_file:
                                lines = user_file.readlines()
                            with open("tasks.txt", "w") as output_file:
                                output = ""
                                for each_line in lines:
                                    stripped = each_line.split(", ")

                                    # Ensures correct line is being edited
                                    if edit_task[int(vm_taskprompt)] == stripped:
                                        while True:
                                            new_assignee = input(
                                                "\nEnter new assignee username: "
                                            )
                                            if new_assignee not in login_credentials:
                                                print("\nUsername not in register.")
                                            else:
                                                break
                                        
                                        # Updates value to variables
                                        stripped[0] = new_assignee
                                        edit_task[int(vm_taskprompt)][0] = new_assignee

                                        # Write back to tasks.txt file
                                        for each_element in stripped:
                                            output += (f"{each_element}, ")
                                    else:
                                        for each_element in stripped:
                                            output += (f"{each_element}, ")
                                    output = output.rstrip(", ")
                                output_file.write(output)
                                print("\nSuccessfully changed assignee.")    

                        # Change due date route
                        if options == "2": 
                            # Open file to read updated version
                            with open("tasks.txt", "r") as user_file:
                                lines = user_file.readlines()
                            with open("tasks.txt", "w") as output_file:
                                output = ""
                                for each_line in lines:
                                    stripped = each_line.split(", ")

                                    # Ensures correct line is being edited
                                    if edit_task[int(vm_taskprompt)] == stripped:

                                        # Ensures correct date format is inputted
                                        while True:
                                            try:
                                                new_due_date = input(
                                                    "\nEnter new due date (Example "
                                                    "- 01 Dec 2022): ")                                               
                                                
                                                (new_due_date != 
                                                datetime.strptime(new_due_date, "%d %b %Y")
                                                .strptime(new_due_date, "%d %b %Y"))
                                                    
                                            except ValueError:
                                                    print("\nDate formatted incorrectly.")
                                                
                                            else:
                                                break
                                        
                                        # Updates value
                                        stripped[4] = new_due_date
                                        edit_task[int(vm_taskprompt)][4] = new_due_date

                                        # Write back to tasks.txt file
                                        for each_element in stripped:
                                            output += (f"{each_element}, ")
                                    else:
                                        for each_element in stripped:
                                            output += (f"{each_element}, ")
                                    output = output.rstrip(", ")
                                output_file.write(output)
                                print("\nSuccessfully changed due date.")                                

                        if options == "3":
                            break

                elif menu == "3":
                    break 

                else:
                    print("\nSelection not recognised. Please try again.")

        elif vm_taskprompt == "-1":
            break

        else:
            print("Task number not found. Please try again.")

def todays_date():
    # Format today's date such that it prints out something like: 10 Oct 2019
    today_formatted = today.strftime(f"%d %b %Y") # 10 Oct 2019
    return today_formatted

def genrep_task():
    with open("tasks.txt", "r") as task_file:
        lines = task_file.readlines()
        counter = 0
        completed = 0
        uncompleted = 0
        overdue = 0
        today_date = todays_date()
        for each_line in lines:
            # Total number of tasks
            counter += 1
            split = each_line.split(", ")

            # Total number of completed & uncompleted tasks
            if split[5] == "Yes\n" or split[5] == "Yes":
                completed += 1
            else:
                uncompleted += 1

            # Total number of tasks that haven't been complicated & overdue
            due_date = datetime.strptime(split[4], "%d %b %Y")
            today_date = datetime.now()
        
            if (today_date > due_date and split[5] == "No\n") or \
                    (today_date > due_date and split[5] == "No"):
                overdue += 1
            
            # Percentage of tasks that are incomplete
            inc_percent = round(uncompleted / counter * 100)
            inc_percent = f"{inc_percent}%"

            # Percentage of tasks that are overdue
            over_percent = round(overdue / counter * 100)
            over_percent = f"{over_percent}%"

    with open ("task_overview.txt", "w") as task_file:
        task_file.write(
            f"Task Overview\n\n"
            f"Total number of tasks registered:             {counter}\n"
            f"Total number of completed tasks:              {completed}\n"
            f"Total number of uncompleted tasks:            {uncompleted}\n"
            f"Total number of incomplete, overdue tasks:    {overdue}\n"
            f"Percentage of tasks that are incomplete:      {inc_percent}\n"
            f"Percentage of tasks that are overdue:         {over_percent}\n"
        )

def genrep_user():
    with open("tasks.txt", "r") as task_file:
        lines = task_file.readlines()
        total = 0
        counter = 0
        completed = 0
        uncompleted = 0
        overdue = 0
        for each_line in lines:
            # Total number of tasks
            total += 1
            split = each_line.split(", ")

            # Checks if the user matches with the username assigned to task
            if split[0] == login_user:
                
                # Total number of tasks assigned to user
                counter += 1

                # Percentage of total number of tasks assigned to user
                total_perc = round(counter / total * 100)
                total_perc = f"{total_perc}%"

                # Total number of completed & uncompleted tasks
                if split[5] == "Yes\n" or split[5] == "Yes":
                    completed += 1
                else:
                    uncompleted += 1

                # Percentage of completed tasks assigned to user
                comp_perc = round(completed / counter * 100)
                comp_perc = f"{comp_perc}%"

                # Percentage of uncompleted tasks assigned to user
                uncomp_perc = round(uncompleted / counter * 100)
                uncomp_perc = f"{uncomp_perc}%"

                # Percentage of tasks uncompleted & overdue
                due_date = datetime.strptime(split[4], "%d %b %Y")
                today_date = datetime.now()
            
                if (today_date > due_date and split[5] == "No\n") or \
                        (today_date > due_date and split[5] == "No"):
                    overdue += 1
                over_perc = round(overdue / counter * 100)
                over_perc = f"{over_perc}%"                
            
    with open ("user_overview.txt", "w") as task_file:
        task_file.write(
            f"User Overview\n\n"
            f"Total number of tasks assigned to user:                   {counter}\n"
            f"Percentage of total tasks assigned to user:               {total_perc}\n"
            f"Percentage of user-assigned completed tasks:              {comp_perc}\n"
            f"Percentage of user-assigned uncompleted tasks:            {uncomp_perc}\n"
            f"Percentage of user-assigned uncompleted & overdue tasks:  {over_perc}\n"
        )

def disp_stat():
    with open("task_overview.txt", "r") as task_file:
        lines = task_file.readlines()
        print(f"{'-' * 80}\n")
        for each_line in lines:
            print(each_line, end="")
        print(f"\n{'-' * 80}")

    with open("user_overview.txt", "r") as user_file:
        lines = user_file.readlines()
        print(f"{'-' * 80}\n")
        for each_line in lines:
            print(each_line, end="")
        print(f"\n{'-' * 80}")

#=====Login Section=====
# Establish a dictionary for login credentials
login_credentials = {}

with open("user.txt", "r") as user_file:
    user_file = user_file.read()

    user_lines = user_file.split("\n")                 # Splits each sentence into list elements

    for each_user in user_lines:
        username, password = each_user.split(", ")     # Splits each element into username & password

        login_credentials[username] = password         # Adds username & password to the dictionary

    while True:
        login_user = input("Enter your username: ")    # Prompt user input for login username & password
        login_pass = input("Enter your password: ")

        # If user inputs correct credentials, break this loop and continue
        if login_user in login_credentials and \
                login_credentials[login_user] == login_pass:
            break
        
        #If user inputs correct username but incorrect password, display appropriate message & ask again
        elif login_user in login_credentials and \
                login_credentials[login_user] != login_pass:
            print("Incorrect password. Please try again.")

        #If user inputs incorrect username, display appropriate message & ask again
        else:
            print("Invalid username. Please try again.")

#=====Menu Options=====
while True:
    # Present menu to user and converts user input to lower case. Display 
    # different menu options depending on if admin or not.
    if login_user == "admin":
        menu = input(
            "\nSelect one of the following options below:"
            "\nr - Registering a user"
            "\na - Adding a task"
            "\nva - View all tasks"
            "\nvm - View my task"
            "\ngr - Generate reports"
            "\nds - Display statistics"
            "\ne - Exit"
            "\n: ").lower()

    else:
        menu = input(
            "\nSelect one of the following options below:"
            "\na - Adding a task"
            "\nva - View all tasks"
            "\nvm - View my task"
            "\ne - Exit"
            "\n: ").lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()

    elif menu == 'gr':
        genrep_task()
        genrep_user()
        print("\nSuccessfully generated reports.")

    elif menu == 'ds':
        disp_stat()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please try again")
        continue