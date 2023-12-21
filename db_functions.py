''' This module contains the basic functions for the DB

-----
Description

tbd

-----
Functions

tbd

'''

# ----------------------------------------
# Imports
# ----------------------------------------

# Standard library imports

# Related third party imports

# Import from other modules
from habit_classes import (
    Habit
)
from db_object_functions import (
    manage_active_passiv_status
)

# ----------------------------------------
# First level functions
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
    
    tbd

    '''

    # Data validation
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

    # Enter data to db
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
    
    tbd

    '''
    # Data validation
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
    
    # Create a habit object.
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