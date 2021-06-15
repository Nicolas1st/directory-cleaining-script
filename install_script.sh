#! /usr/bin/bash


mkdir ~/.python_scripts
mv directory_cleaning_script.py ~/.python_scripts
echo "alias initdir='python3 ~/.python_scripts/directory_cleaning_script.py initdir'" >> ~/.bashrc
echo "alias storestate='python3 ~/.python_scripts/directory_cleaning_script.py store'" >> ~/.bashrc
echo "alias cleanup='python3 ~/.python_scripts/directory_cleaning_script.py cleanup'" >> ~/.bashrc
