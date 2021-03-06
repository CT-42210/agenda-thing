import sys
import time
import os
import setup
import homescreen
import assignments
import checklists
import settings

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

def bypass():
    bypass = input("The install verification file failed. do you want to install the program, or do you want to pass? \n type [1] to pass and launch the program, type [2] to reinstall \n")

    if bypass == "1":
        homescreen.welcome()
    elif bypass == "2":
        setup.setup()
    else:
        print("input error. stoping...")
        time.sleep(1)
        sys.exit()

def install_checker():
    setup_file = open('setup.txt', 'r')
    true_strings = ['setup completion =\n', ' true\n', ' Version 0.3']
    false_strings = ['setup completion = false \n', '\n', ' Version 0.3']

    lines = setup_file.readline()

    def readline(lines):
        if lines in true_strings:
            return True
        if lines in false_strings:
            return False
        else:
            return "err"

    with open('setup.txt', 'r') as setup_file:
        for lines in setup_file:
            if readline(lines) == True:
                print('installed. launching...')
                homescreen.welcome()
                usr_input()
                break
            elif readline(lines) == False:
                print('not installed. installing...')
                setup.setup()
                break
            else:
                pass

    setup_file.close()

def usr_input():

    def assignment_handler():
        assignments.assignments()

    def checklists_handler():
        checklists.checklists()

    def settings_handler():
        settings.settings()

    print("what do you want to do?")
    question = input(" \n type [a] to open your assignments page, \n type [c] to open your checklist page, \n type [s] to edit your settings. \n \n $")

    handlers = {
        'a': assignment_handler,
        'c': checklists_handler,
        's': settings_handler
    }

    if question in handlers:
        handlers[question]()
    else:
        print("Unknown choice", question)




path = os.getcwd()
name = "setup.txt"

for root, dirs, files in os.walk(path):
    if name in files:
        install_checker()
        break
    else:
        setup.setup()
        break

