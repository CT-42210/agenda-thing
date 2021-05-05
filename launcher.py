import sys
import time
import os
import setup
import homescreen

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
    true_strings = ['setup completion =\n', ' true\n', ' Version 0.2']
    false_strings = ['setup completion = false \n', '\n', ' Version 0.2']

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
                break
            elif readline(lines) == False:
                print('not installed. installing...')
                setup.setup()
                break
            else:
                pass

    setup_file.close()

path = os.getcwd()
name = "setup.txt"

for root, dirs, files in os.walk(path):
    if name in files:
        install_checker()
        break
    else:
        setup.setup()
        break

