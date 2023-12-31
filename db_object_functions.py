'''
This module contains functions to handle the database objects.

----------------------------------------
Description
----------------------------------------

The functions in this module are for adjusting single or multiple values on existing database objects.
For creating and deleting objects see the module db_functions.
The module is divided into two regions. All functions that handle the objects indirectly are in the first region.
Functions that are used to modify values from the objects are in the second region.

----------------------------------------
Functions
----------------------------------------
from region 1 (indirect):

change_active_passiv_status
    This function is used to switch the status of a habit from being tracked to not or vice versa.

manage_active_passiv_status
    In this function the status of the habit (tracked/not tracked) is used to decide how to proceed with it

manage_passiv_habits
    This function is used to call the reset functions for a passiv habit.

from region 2 (object):

switch_active_passiv_status
    This function switches the status between being activly tracked or just passiv.

setup_active_habits
    This function sets the start date and the next due date for active habits, when activated.

reset...
    The set of reset functions is used to reset a specific value back to the standard, like the current streaks to zero.

set_tracking_status_to_true
    The function is used to set the tracking status to the value True.

streak_calculator
    This function is used to calculate the current and highscore streak and adjusts the values of the object.

'''
# ----------------------------------------
# Imports
# region ----------------------------------------

# Standard library imports
import datetime

# Import from other modules
from db_filter_functions import(
    filter_db_for_names
)
from db_history_functions import(
    create_new_history_entry
)

# endregion

# ----------------------------------------
# Indirect functions
# region ----------------------------------------

# change_active_passiv_status
def change_active_passiv_status(session, names):
    ''' 

    tbd

    '''

    habit_entries = filter_db_for_names(session=session, names=names)

    for habit_entry in habit_entries:
        switch_active_passiv_status(session, habit_entry)
        manage_active_passiv_status(session=session, habit_object=habit_entry)

# manage_active_passiv_status
def manage_active_passiv_status(session, habit_object):
    '''
    
    tbd

    '''
    if habit_object.habit_active_status is True:
        setup_active_habits(session=session, habit_object=habit_object)
    else:
        manage_passiv_habits(session=session, habit_object=habit_object)

# manage_passiv_habits
def manage_passiv_habits(session, habit_object):
    ''' 

    tbd
        
    '''
    reset_start_date(session=session, habit_object=habit_object)
    reset_next_due(session=session, habit_object=habit_object)
    reset_total_fails(session=session, habit_object=habit_object)
    reset_current_streak(session=session, habit_object=habit_object)
    reset_tracking_status(session=session, habit_object=habit_object)


# manage_tracking_status
def manage_tracking_status(session, names):
    '''
    '''
    function_status_message = [] 
    habit_entries = filter_db_for_names(session=session, names=names)
    for habit_entry in habit_entries:
        if (habit_entry.habit_active_status is True
            and habit_entry.habit_tracking_status is False
        ):
            set_tracking_status_to_true(session=session, habit_object=habit_entry)
            streak_calculator(session=session, habit_object=habit_entry)
        elif habit_entry.habit_active_status is False:
            function_status_message.append(200)
    if function_status_message != []:
        return function_status_message
    else:
        return None
# endregion

# ----------------------------------------
# Object functions
# region ----------------------------------------

# switch_active_passiv_status
def switch_active_passiv_status(session, habit_object):
    '''
    '''
    habit_object.habit_active_status = not habit_object.habit_active_status
    session.commit()

# setup_active_habits
def setup_active_habits(session, habit_object):
    '''
    
    tbd

    '''
    if habit_object.habit_start_date is None:
        habit_object.habit_start_date = datetime.date.today()
    if habit_object.habit_next_due is None:
        habit_object.habit_next_due = habit_object.habit_start_date + datetime.timedelta(days=habit_object.habit_period)
    session.commit()

# reset_current_streak
def reset_current_streak(session, habit_object):
    '''
    '''
    habit_object.habit_current_streak = 0
    session.commit()

# reset_tracking_status
def reset_tracking_status(session, habit_object):
    '''
    '''
    habit_object.habit_tracking_status = False
    session.commit()

# reset_start_date
def reset_start_date(session, habit_object):
    '''
    '''
    habit_object.habit_start_date = None
    session.commit()

# reset_next_due
def reset_next_due(session, habit_object):
    '''
    '''
    habit_object.habit_next_due = None
    session.commit()

# reset_total_fails
def reset_total_fails(session, habit_object):
    '''
    '''
    habit_object.habit_total_fails = 0
    session.commit()

# set_tracking_status_to_true
def set_tracking_status_to_true(session, habit_object):
    '''
    '''
    habit_object.habit_tracking_status = True
    session.commit()
    create_new_history_entry(session=session, habit_object=habit_object)

# streak_calculator
def streak_calculator(session, habit_object):
    '''
    '''
    habit_object.habit_current_streak = habit_object.habit_current_streak + 1
    if habit_object.habit_current_streak > habit_object.habit_highscore_streak:
        habit_object.habit_highscore_streak = habit_object.habit_current_streak
    session.commit()
# endregion
