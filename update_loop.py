"""
Creates a loop function to check the status of the habits.

----- Description -----
This module adds a loop function and its corresponding functions to check the
status of the habits.
When the due date passed, the needed actions, like the reset of the tracking
status to False, the calculation of a new due date etc. will be performed.

----- Functions -----
loop_for_update_due_date:   This function calls the check of the due date and
                            itself after a specified period.
check_due_date:             This function compares the current date with the
                            due date of the habit. If the due date passed, then
                            it calls further check functions.
check_tracking_status:      This function checks the tracking status for habits
                            whith passed due dates. It calls a set of functions
                            depending on its status.
calculate_new_due_date:     This function is used to calculate the new due date
                            for the habits with passed due date. It adjusts the
                            database entry accordingly.
count_fails_up:             This function counts up the fails, when the due
                            date passed and the habit has not been marked as
                            complete (tracking_status = True)
"""

# ----------------------------------------
# Imports
# region ----------------------------------------

# Standard library imports
import datetime

# Related third party imports

# Import from other modules
from db_history_functions import create_new_history_entry
from db_object_functions import reset_current_streak, reset_tracking_status
from habit_classes import Habit

# endregion

# ----------------------------------------
# Functions
# region ----------------------------------------


# loop_for_update_due_date
def loop_for_update_due_date(session, main_window):
    """
    Loop function to check the status of the habits.

    ----- Description -----
    This functions calls itself to check the status of each habit that is
    currently tracked, and thus has a due date.

    ----- Arguments -----
    session (Session):          Containing the reference to the database
                                session.
    main_window (MainWindow):   The instance of the MainWindow.
    """
    check_due_date(session=session)
    main_window.update_data_in_table()
    timer_in_milliseconds = 300000  # 5min
    main_window.main_root.after(
        timer_in_milliseconds,
        lambda: loop_for_update_due_date(
            session=session, main_window=main_window
        ),
    )


# check_due_date
def check_due_date(session):
    """
    Checking if the due dates of the habits passed or not.

    ----- Description -----
    The function gets all entries in the database that have a due date.
    The objects are checked for the due date value. It is compared to today.
    If the due date passed, then the tracking status will be checked. Otherwise
    nothing else will happen.

    ----- Arguments -----
    session (Session):  Containing the reference to the database session.
    """
    current_date = datetime.date.today()
    habit_entries = (
        session.query(Habit)
        .filter(Habit.habit_next_due.isnot(None))
        .all()
    )
    for habit_entry in habit_entries:
        if habit_entry.habit_next_due < current_date:
            check_tracking_status(session, habit_entry)


# check_tracking_status
def check_tracking_status(session, habit_object: Habit):
    """
    Checks the status of habit_tracking_status for each object.

    ----- Description -----
    The function checks for each object if it has been marked as complete. If
    so, then the new date will be calculated and the status will be set to
    False again. If the tracking status is still False, then the count_fails_up
    function will be called. Further the current streak will be set to 0 using
    the reset function for this. Finally the next due date will be calculated.

    ----- Arguments -----
    session (Session):      Containing the reference to the database session.
    habit_object (Habit):   Attribute to contain the object to be modified by
                            the user.
    """
    if habit_object.habit_tracking_status is True:
        calculate_new_due_date(session, habit_object)
        reset_tracking_status(session, habit_object)
    else:
        count_fails_up(session, habit_object)
        reset_current_streak(session, habit_object)
        calculate_new_due_date(session, habit_object)
        create_new_history_entry(session=session, habit_object=habit_object)


# calculate_new_due_date
def calculate_new_due_date(session, habit_object: Habit):
    """
    Calculates the new due date based on the current due date and its
    periodicity.

    ----- Description -----
    This function calculates the next due date for habits that have a passed
    due date. Therefore it uses the current one and the periodicity
    (habit_period). The habit_next_due value will be changed in the database.

    ----- Arguments -----
    session (Session):      Containing the reference to the database session.
    habit_object (Habit):   Attribute to contain the object to be modified by
                            the user.

    ----- Note -----
    This function calculates the new next due date based on the current value.
    It would also be possible to use the current day as basis.
    The next due date as basis is used since it seems more correct according
    to the targets of the user to complete some tasks for example daily.
    This means that if the application will update the due date for a daily
    tracked habit x times if the user did not login for x days - leading to
    the point that the number of fails also will rise x times.
    """
    habit_object.habit_next_due += datetime.timedelta(
        days=habit_object.habit_period
    )
    session.commit()


# count_fails_up
def count_fails_up(session, habit_object: Habit):
    """
    Counting up the number of fails to complete the task in time.

    ----- Description -----
    This function counts up the number of fails each time the user does not
    complete the task in time.

    ----- Arguments -----
    session (Session):      Containing the reference to the database session.
    habit_object (Habit):   Attribute to contain the object to be modified by
    the user.
    """
    habit_object.habit_total_fails = habit_object.habit_total_fails + 1
    session.commit()

# endregion
