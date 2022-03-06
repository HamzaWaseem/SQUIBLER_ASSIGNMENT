## Online BookReader & REST API Using DRF
## Setup Project

1. Clone the project using following command
```
https://github.com/HamzaWaseem/SQUIBLER_ASSIGNMENT.git
```
2. Make sure you have python 3 installed in your system
-  Open terminal and run command 
```
python3 --version
```
-  If there is not python3 version in your system, please visit https://www.python.org/downloads/

3. Check if you have pip in you OS
-  pip --version or python3 -m pip --version
-  If it says no module named pip please visit https://pip.pypa.io/en/stable/installation/#get-pip-py


4Create Virtual Environment
```
python -m venv {{virtual_env}}
```

5. Activate Environment
```
source {{virtual_env}}/bin/activate
```


6. Run following command to install requirements
pip install -r requirements.txt 

7. Create superuser to view data in admin panel
create superuser
```
python manage.py createsuperuser
```

8. Run following commands for migrations
python manage.py makemigrations
python manage.py migrate

9. Run following command to run server
```
python manage.py runserver
```
10. API sample:

BOOKS API SAMPLE
http://127.0.0.1:8000/api/books/
{
    "title":"BookA",
    "description" : "Test description",
    "user" : "1"
}

USER API SAMPLE
http://127.0.0.1:8000/api/users/
{
    "username":"H1",
    "password" : "P10101010",
    "confirm_password" : "P10101010"
}

SECTION API SAMPLE
http://127.0.0.1:8000/api/sections/
{
    "book":"1",
    "heading": "Heading 1",
    "content": "test content",
    "parent_section" : "1"
}