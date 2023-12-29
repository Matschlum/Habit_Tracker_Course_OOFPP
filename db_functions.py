''' 
This module contains the functions to add and delete objects from the db.

----------------------------------------
Description

This module is used for the functions that add new objects to the database, including the standard values.
Further the delete object function is located in this module.

-----
Functions

add_standard_habits_to_db
    This function is used to add the standard values from db_standard_entries.py to the database.

add_new_entry_to_db
    This function is used to actually perform the process of adding new objects to the database.
    It is used by the add_standard_habits_to_db function as well as via the GUI.

delete_entries_from_db
    This function receives a list of habit names and deletes the corresponding objects from the database.

'''

# ----------------------------------------
# Imports
# ----------------------------------------

# Standard library imports

# Related third party imports

# Import from other modules
from habit_classes import(
    Habit
)
from db_object_functions import(
    manage_active_passiv_status
)
from db_filter_functions import(
    filter_db_for_names
)

# ----------------------------------------
# Functions
# ----------------------------------------

# add_standard_habits_to_db()
def add_standard_habits_to_db(
    session,
    standard_name,
    standard_description,
    standard_period,
    standard_active_status
):
    ''' 
    This function is used to add the standard values to the database.

    ----------------------------------------
    Description

    This function uses lists for the key values from a habit object, name, description, periodicity and active status to create new objects.
    Therefore the lists will be validated. If the lists fulfill the requirements, the functions calls the add_new_entry_to_db function to add the values as objects to the db.

    ----------------------------------------
    Arguments (Parameters)

    session
        Session allwos the interaction with the database. It is passed
        to the check_due_date function.
    standard_name, standard_description, standard_period, standard_active_status
        These are lists containing the standarad values to be added to the database.

    ----------------------------------------
    Returns

    function_status_message / function_status_message_adding_entries
        This return values are used for the InputMessageWindow to show the user the status of the input.
    '''

    # Validation of the input lists to ensure correct object creation.
    if not all(isinstance(period, int)
               for period in standard_period):
        function_status_message = 120
        return function_status_message

    if not all(isinstance(active_status, bool)
               for active_status in standard_active_status):
        function_status_message = 121
        return function_status_message

    if not all(len(standard_values) == len(standard_name)
               for standard_values in [
                   standard_name,
                   standard_description,
                   standard_period,
                   standard_active_status
               ]):
        function_status_message = 122
        return function_status_message

    # Using the input lists to create new habit objects.
    function_status_message_adding_entries = []
    for counter in range(len(standard_name)):
        name = standard_name[counter]
        description = standard_description[counter]
        period = standard_period[counter]
        active_status = standard_active_status[counter]

        message_handler = add_new_entry_to_db(
            session,
            name,
            description,
            period,
            active_status
        )
        function_status_message_adding_entries.append((counter, message_handler))

    return function_status_message_adding_entries

# add_new_entry_to_db()
def add_new_entry_to_db(
    session,
    name: str,
    description: str,
    period: int,
    active_status: bool
):
    ''' 
    This function is used to create a new habit object and adds it to the database.

    ----------------------------------------
    Description

    This function uses input values to create an object of the habit class and adds the object to the database.
    Before creating the object, the function validates the input data to be suitable for an object.
    If the input values are not suitable, then no object is created, instead a status message is created and returned.

    ----------------------------------------
    Arguments (Parameters)

    session
        Session allwos the interaction with the database. It is passed
        to the check_due_date function.
    name, description, period, active_status
        These are values containing the needed values to create a habit object.

    ----------------------------------------
    Returns

    function_status_message
        This return value is used for the InputMessageWindow to show the user the status of the input.
    '''
    # Validation of the input to ensure correct object creation.
    function_status_message = []

    if not isinstance(period, int):
        function_status_message.append(113)
    if not isinstance(active_status, bool):
        function_status_message.append(112)
    if name is (None or ""):
        function_status_message.append(114)

    if function_status_message != []:
        return function_status_message

    if not isinstance(name, str):
        function_status_message.append(100)
        name = str(name)
    if not isinstance(description, str):
        function_status_message.append(101)
        description = str(description)
    
    # Using the input values to create new habit objects.
    check_name = (
        session.query(Habit)
        .filter_by(habit_name=name)
        .first()
    )
    if check_name is None:
        habit_entry = Habit(name, description, period, active_status)
        session.add(habit_entry)
        session.commit()
        manage_active_passiv_status(session=session, habit_object=habit_entry)
        function_status_message.append(0)
    else:
        function_status_message.append(1)
    return function_status_message


# delete_entries_from_db
def delete_entries_from_db(session, habit_names):
    ''' 
    This function is used to delete entries from the database.

    ----------------------------------------
    Description

    This function takes a list of habit names and searches for the corresponding objects.
    These objects are then deleted from the database.

    ----------------------------------------
    Arguments (Parameters)

    session
        Session allwos the interaction with the database. It is passed
        to the check_due_date function.
    habit_names
        A list of habit names, that are used to find objects from the habit class in the database.

    ----------------------------------------
    Returns

    None
    '''
    habit_entries = filter_db_for_names(session=session, names=habit_names)
    for entry in habit_entries:
        session.delete(entry)
    session.commit()