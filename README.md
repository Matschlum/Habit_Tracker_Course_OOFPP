# Habit_Tracker_Course_OOFPP
  
## General
This application is an easy habit tracker application, allowing the usser to create habits that should be tracked.  
### Content
This application consists out of different .py-files to run the application, a unittest file, a script to add sample data for 5 habits, a .md-file to describe the error codes and this README.md  
### Python Version
This application is written with Python Version 3.11.  
### Libraries
Build-in libraries used:  
* datetime
* os
* sys
* tkinter
* typing
* unittest
  
Third party imports  
* sqlalchemy (Version 2.0.23)
  
### Comments
This application is written under the premise to use comments rarely.  
Main purpose of the comments is to structure the code, to make it more readable.  
Note that each function and class have its name as a comment just above the definition. This is because Visual Studio 2022 has been used to write this application. VS allows the user to collapse classes and functions to make it easier to navigate within one module. However collapsing a function means that you only can read “def …” (or in case of a class “class …”), without VS showing you the name.  
## Module / file overview
Required modules/files:  
* create_new_change_habit_window	Class to create new habits / change existing ones (GUI)
* db_filter_functions				Functions to filter within the database				
* db_functions						Functions to add / remove / change habits			
* db_history_functions				Functions to add / remove habit history				
* db_object_functions				Functions to adjust single attributes from a habit	
* db_setup							Functions to setup the database						
* db_standard_entries				Lists with information for standard habits			
* habit_history_window				Class to show the history of habits (GUI)
* main								Main file that has to be executed
* main_window						Class to show the main window of the application (GUI)
* pop_up_windows					Class for the highscore and the error code window (GUI)
* update_loop						Functions to update the status of the habits regularly
  
Further modules:  
* add_sample_data					Used to add sample data for 5 habits
* function_testing					Used to test the main functions regarding the database
  
Further files:  
* error_code.md						Contains a list of all warnings, error messages etc.
* habit_tracker.db					Database - will be created if not existing
* LICENSE.txt						License information.
* README.md							Readme file
   
Find furhter information in the documentation for each module.  
## Installation
Installation guide line:
1. Make sure Python is installed.  
2. Make sure sqlalchemy is installed. You can use pip install sqlalchemy.
3. Download the files from github.
4. Extract the files to a directory of your choice.

## Run instructions
### Run main application
1. Open your console
2. Navigate to the directory where you placed the files.
3. Use:		python main.py
  
Note: The application will start with a request in the console. If you type anything else than yes (for example: YES), then the app will not try to add the standard habits again.  
Afterwards you can use the GUI.  
### Run function testing
1. Open your console
2. Navigate to the directory where you placed the files.
3. Use:		python -m unittest function_testing.py
### Run sample data
1. Open your console
2. Navaigate to the directory where you placed the files.
3. Use:		python add_sample_data.py
  
Note: This will delete the all entries from the database and add the specified sample data.  
## Problems to run the application
* Check the version of Python - try to use 3.11
* Check the version of SQLAlchemy - try to use version 2.0.23
  
## Additional information on how to use the application
### GUI
The GUI is very simple.  
You can scroll down in the tables you see in all windows, although it does not show a scroll bar.  
The texts might not fit always in the space - try to make the windows bigger.  
### Usage
This application should be quite self-explanatory.  
A hint: If you mark more than one habit in the main window and click on the change habit button, it will open a window for each marked habit!  
## Adjusting the application
This is a quick guide to adjust two things in the code: The standard habits and the periodicity.  
### Add, modifiy or remove standard habits
To add, adjust, remove standard habits:  
1. Open db_standard_entries.py
2. Adjust the lists as you like, but use the right data type in the lists. This will be controlled by the function that adds the data into the database.
  
To remove standard habits completlty:  
1. Open main.py
2. Delete the code in the region	Adding standard habits.
3. Additionally you should delete: the import of the db_standard_entries in main.py.
4. You can then delete the entire file db_standard_entries.py
  
To remove the request if you want to add standard habits:  
1. Open main.py
2. Delete the lines in the region   Adding standard habits.:
    input_for_standard_habits = input(  
        "If you want to add the standard values type: yes\n"  
    )  
### Periodicity: add choices or make it free of choice
Adding a new choice for the periodicity:  
1. Open create_new_change_habit_window.py
2. Go to the region:        Defining the basic attributes for entry fields, buttons and methods.
3. Add the name of your new periodicity to the list:    self.period_option_lst
4. Create a new elif statement (C&P a statement above) and enter your numbers.
   Example: "Every other week" / 14:
        elif self.habit_object.habit_period == 14:  
            self.period_variable.set(self.period_option_lst[3])  
5. Go to the function:      convert_period_to_integer
6. Add a new elif statement before the else: (C&P a statement above) and enter your numbers.

Adding the filter option:  
1. Open main_window.py
2. Go to the region:        Creating all widgets for the subframe_top_buttons
3. Add a new button for the filter (C&P an existing one and rename it).
   For the command-function lambda: self.click_show_period(7) pass the number you want.  
   Example: "Every other week" -> lambda: self.click_show_period(14)  
4. Go to the region:        Place the widgets into the frames.
5. Add your new button to the list second_row_widgets.
  
Note: Adding new filters to the main window may has a negative impact on the layout. Adjust it accordingly.  
  
Changing the system to a free of choice:  
Have a look at the habit_history_window.py file and try to understand how it works there.  
This can be rebuild in the same manner in the main_window.  
The create_new_change_habit_window.py then has to be adjusted as well.  
The entry incl. its validation should replace the list of choices.  
Note: It is not recommended to do this if you did not understand how it works in the habit_history_window.py  
## Styling guidelines
The style of this code tries to follow the suggestions made by  
PEP 8 - Style Guide for Python Code  
https://peps.python.org/pep-0008/  
https://realpython.com/python-pep8/  
PEP 257 - Docstring Conventions  
https://peps.python.org/pep-0257/  
https://realpython.com/documenting-python-code/#docstrings-background  
  
To comply with these guidelines, this code has been formatted using the following tools:  
* isort
* black
* pylint
* pycodestyle
* mypy
  
The function_testing and the add_sample_data are not formatted in that way.  
## Final words
Ok - I know. Passive is written passive with an e at the end. Sorry!!! It is a bit a mess.  
There are probably other mistakes.  
If you find mistakes in the docstrings, comments etc. let me know by opening an issue in github. :)  
### Further development and availability
After course evaluation this application will not be developed further.  
Only during the course it will be public available. Afterwards it will be taken down.  