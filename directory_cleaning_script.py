import os
import json
from sys import argv
from datetime import datetime


def store_state():
    dir_contents = json.dumps(os.listdir())
    with open('.goodfiles', 'w') as f:
        f.write(dir_contents)


def init_dir():
    
    # .goodfiles is created beforehand to store this filename in the file
    os.system('touch .goodfiles')
    os.system('mkdir .not_needed_files')
    store_state()


def clean_folder():

    # when there is not previous state stored
    if '.goodfiles' not in os.listdir():
        print('No record of the state in which the folder is considered to be clean')
        print('Creating the record')
        init_dir()
        exit()

    files = os.listdir()
    todays_junk_folder_name = datetime.now().strftime('%H:%M:%S_on_%A,_%B_the_%dth,_%Y')
    os.system(f'mkdir {todays_junk_folder_name}')
        

    with open('.goodfiles', 'r') as f:
        good_files = json.loads(f.read())  

    for file in files:

        if file not in good_files:
            os.system(f'mv {file} {todays_junk_folder_name}')

    os.system(f"mv {todays_junk_folder_name} .not_needed_files")
    

if __name__ == "__main__":

    if len(argv) < 2:
        print("""
        Supply the arguments
        init_dir - to store the state of current directory
        cleanup - to get rid of clutter
        """)
        exit()

    if argv[1] == 'initdir':
        init_dir()

    elif argv[1] == 'store':
        store_state()

    elif argv[1] == 'cleanup':
        clean_folder()

    else:
        print('Unknown argument')
