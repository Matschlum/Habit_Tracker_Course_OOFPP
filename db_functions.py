'''
This module contains the functions used to add, delete or change habits.

----- Description -----
In this module are functions to add and delete habits to/from the database as well as to change habit objects.

----- Functions -----
add_standard_habits_to_db:      This function is used to add the standard values to the database. It works with the add_new_entry_to_db function.
add_new_entry_to_db:            This function is adding new habits to the database.
delete_entries_from_db:         It is used to delete entries from the database, including the corresponding history entries.
modify_existing_object_in_db:   After modifing some values of an existing habit, this function changes the values of the objects.
'''

# ----------------------------------------
# Imports
# region ----------------------------------------

# Standard library imports

# Related third party imports

# Import from other modules
from db_filter_functions import filter_db_for_names
from db_history_functions import delete_history_entries
from db_object_functions import manage_active_passiv_status
from habit_classes import Habit

# endregion

# ----------------------------------------
# Functions
# region ----------------------------------------

# add_standard_habits_to_db
def add_standard_habits_to_db(
    session,
    standard_name,
    standard_description,
    standard_period,
    standard_active_status
):
    '''

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
        function_status_message_adding_entries.append((
            counter,
            message_handler
        ))

    return function_status_message_adding_entries


# add_new_entry_to_db
def add_new_entry_to_db(
    session,
    name: str,
    description: str,
    period: int,
    active_status: bool
):
    '''
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

    '''
    habit_entries = filter_db_for_names(session=session, names=habit_names)
    for entry in habit_entries:
        delete_history_entries(session=session, habit_object=entry)
        session.delete(entry)
    session.commit()

# modify_existing_object_in_db
def modify_existing_object_in_db(session, original_object, name, description, period, active_status):
    function_status_messages = []
    if original_object.habit_name != name:
        check_name = (
            session.query(Habit)
            .filter_by(habit_name=name)
            .first()
        )
        if check_name is None:
            original_object.habit_name = name
            function_status_messages.append(301)
        else:
            function_status_messages.append(1)
            return function_status_messages
    else:
        function_status_messages.append(401)

    if original_object.habit_description != description:
        original_object.habit_description = description
        function_status_messages.append(302)
    else:
        function_status_messages.append(402)

    if original_object.habit_period != period:
        original_object.habit_period = period
        function_status_messages.append(303)
    else:
        function_status_messages.append(403)

    if original_object.habit_active_status != active_status:
        original_object.habit_active_status = active_status
        function_status_messages.append(304)
    else:
        function_status_messages.append(404)

    session.commit()
    return function_status_messages
# endregion
