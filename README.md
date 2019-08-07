#Property Rental System

##Prerequisites: Python3, pip, pipenv
###If installing on a Linux machine:

1. `Python3` not installed? run: `sudo apt-get install python3.6` in the terminal
2. `pip` not installed? run: `sudo apt-get install python3-pip`

###If installing on a Windows machine: 

1. `Python3` not installed? Download at: "https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe"
2. Upon starting installation, click checkbox "Add Path 3.6 to PATH" to run in Command Prompt
3. Open Command Prompt (Easiest through search bar) and run `python --version`, the output should be `Python 3.6.8` if the installation was successful

###The following steps apply for both Linux and Windows machines:

4. Install `pipenv` by running `python3 -m pip install pipenv`
5. Go to the root directory of the project folder. run `cd .../.../capstone-project-216`  (Linux)  (The directory which contains `requirements.txt`)
   - Windows uses "\\" instead of "/"
6. run: `pip install -r requirements.txt`
7. run: `cd src`
8. run: `python manage.py makemigrations`
9. run: `python manage.py migrate`
10. run: `python manage.py loaddata fixtures.json`
11. run: `python manage.py runserver --insecure` 
    - NOTE: staticfiles will not be served when `DEBUG = False`, since production web server takes care of these files. `--insecure` mode allows to access staticfiles during development. 
12. Copy url given in the terminal and paste it in browser to open web application
    - e.g. http://127.0.0.1:8000/ or something like that

*Note: if the layout is plain, `cd src` and within `settings.py`, change  `DEBUG=FALSE` into  `DEBUG = TRUE`. It is currently set to off to display the 404 page.*

