### Directory Ceaining Script


## Description
Simple script for moving  new contents of a directory away
After the initalization there will be 2 files created in the target directory:
* .good_files - json file containing files that will not be removed anywhere
* .not_needed_files - directory containing directories named with the current time containing moved files


## Using
* To initialize the script for the target directory: $ initdir
* To store the new "proper" directory state: $ storestate
* To clean up the directory: $ cleanup


## Requirements
* python3
* bash


## Installing the script on Linux:
1) Download the files from the repo and put them into one directory
2) Run the command following command: $ bash install_script.sh
