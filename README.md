Property Rental System

Prerequisites: Python3, pip, pipenv
if (Installation Linux):
1. No "Python3" ? run: "sudo apt-get install python3.6"
2. No "pip" ? run: "sudo apt-get install python3-pip"
3. N/A

if (Windows10):
1. No "Python3" ? Download: "https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe"
2. Before you press "Install Now", click checkbox "Add Path 3.6 to PATH" to run in Command Prompt
3. Open Command Prompt (Easiest through search bar) and run python --version, outputs "Python 3.6.8" - working

BOTH:
4. Install "pipenv". run: "python3 -m pip install pipenv"
5. go to the project's directory where it contains the "requirements.txt" file. run: "cd .../PATH-TO-FILE/capstone-project-2166" (linux) -- Windows uses "\" instead of "/"
6. run: "pip install -r requirements.txt"
7. run: "cd src"
8. run: "python manage.py makemigrations"
9. run: "python manage.py migrate"
10. run: "python manage.py loaddata fixtures.json"
11. run: "python manage.py runserver --insecure" NOTE: staticfiles will not be served when DEBUG = False, since production web server takes care of these files. --insecure mode allows to access staticfiles during development. 
12. copy url given in the terminal and paste it in browser to open web application

#NOTE: if layout is plain, cd src (contains setting.py) and change the variable DEBUG = TRUE. Currently off to display 404 page
