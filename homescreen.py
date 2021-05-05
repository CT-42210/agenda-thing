import sys
import time
import os

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

def welcome():
    account_file = open("Account.txt","r")
    account_file_read = account_file.readlines()
    account_name = account_file_read[1]
    full_name = account_file_read[2:3]
    first_name = account_file_read[2]
    last_name = account_file_read[3]
    email = account_file_read[4]

    print("logging into account",account_name,"...")
    time.sleep(0.5)
    buffering()
    print("----------------------------------------------------")
    print("Welcome",first_name)
    account_file.close()
    homescreen_order()

def top_5_assingments():
    parent_dir = os.getcwd()
    created_dir = r"\Script files"
    script_dir = parent_dir + created_dir
    assignments_path = os.path.join(script_dir, "Assignments.txt")

    try:
        assignments_file = open(assignments_path, "r")
        top_five_lines = assignments_file.readlines()
        print("here are your top 5 assignments: \n")
        print(top_five_lines[1])
        print(top_five_lines[2])
        print(top_five_lines[3])
        print(top_five_lines[4])
        print(top_five_lines[5])
    except IndexError:
        print("You dont have 5 assignments!")

def top_five_lists():
    parent_dir = os.getcwd()
    created_dir = r"\Script files"
    script_dir = parent_dir + created_dir
    checklist_path = os.path.join(script_dir, "Checklists.txt")

    try:
        checklist_file = open(checklist_path, "r")
        top_five_lines = checklist_file.readlines()
        print("here are your top 5 checklists: \n")
        print(top_five_lines[1])
        print(top_five_lines[2])
        print(top_five_lines[3])
        print(top_five_lines[4])
        print(top_five_lines[5])
    except IndexError:
        print("You dont have 5 checklists!")

def buffering():
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)

def homescreen_order():
    settings_file = open('Settings.txt', 'r')
    lines_to_read_1 = [3]
    lines_to_read_2 = [4]
    lines_to_read_3 = [5]

    def assignment_handler():
        top_5_assingments()

    def checklists_handler():
        top_five_lists()

    def custom_handler():
        print("yay 3")

    handlers = {
        'assignments': assignment_handler,
        'checklists': checklists_handler,
        'custom text': custom_handler
    }

    with open('Settings.txt', 'r') as settings_file:
        for position, line in enumerate(settings_file):
            line = line.strip()
            if position in lines_to_read_1:
                if line in handlers:
                    handlers[line]()
                else:
                    print("Unknown choice", line)

    with open('Settings.txt', 'r') as settings_file:
        for position, line in enumerate(settings_file):
            line = line.strip()
            if position in lines_to_read_2:
                if line in handlers:
                    handlers[line]()
                else:
                    print("Unknown choice", line)

    with open('Settings.txt', 'r') as settings_file:
        for position, line in enumerate(settings_file):
            line = line.strip()
            if position in lines_to_read_3:
                if line in handlers:
                    handlers[line]()
                else:
                    print("Unknown choice", line)