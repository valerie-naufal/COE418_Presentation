# DB Project 1 - Presentation Demo

## Software Requirements
- MySQL DB
- MySQL WorkBench (optional)
- Linux operating system (ubuntu)
- Python 3.1

## Project Initialization
1. **Install venv (virtual environment library)** ```sudo apt-get install -y python3-virtualenv``` **(FOR UBUNTU)**
2. **Activate Virtual Environment** ```source venv/bin/activate``` **(INSIDE PROJECT DIRECTORY)**
3. **Run command** ```pip install -r requirements.txt```

## Demo File Structure
1. ```users.json``` JSON file containing list of students
2. ```utils.py``` Module created to be imported
3. ```insert_students.py``` Python demo to insert students into DB
4. ```get_students.py``` Python demo to retrieve students from DB
5. ```student.py``` Python class representing student entry 
6. ```main.py``` Python GUI using PySimpleGUI

>To activate GUI, run `python3 main.py`