"""
This module contains the functions needed to create and delete history entries.

----- Functions -----
create_new_history_entry:   Creating entries in the database table
                            habithistory.
delete_history_entries:     Deleting entries from the database table
                            habithistory.
"""

# ----------------------------------------
# Imports
# region ----------------------------------------

# Standard library imports
import datetime

# Related third party imports

# Import from other modules
from habit_classes import HabitHistory

# endregion

# ----------------------------------------
# Functions
# region ----------------------------------------


# create_new_history_entry
def create_new_history_entry(session, habit_object):
    """
    This function creates new entries in the database table habithistory.

    ----- Description -----
    The function takes the related habit object as input and creates based on
    the current time and status of the habit new entries in the database.

    ----- Arguments -----
    session (Session):      Containing the reference to the database session.
    habit_object (Habit):   Habit object that is related to the history entry,
                            which will be created.
    """
    date_and_time_of_history_entry = datetime.datetime.now()

    history_entry = HabitHistory(
        habit_key=habit_object.habit_name,
        fail_or_completion_date_time=date_and_time_of_history_entry,
        corresponding_due_date=habit_object.habit_next_due,
        type_of_completion=habit_object.habit_tracking_status,
    )
    session.add(history_entry)
    session.commit()


# delete_history_entries
def delete_history_entries(session, habit_object):
    """
    This function deletes history entries related to a specific habit object.

    ----- Description -----
    The function takes the related habit object as input and deletes all
    corresponding entries in the table habithistory.

    ----- Arguments -----
    session (Session):      Containing the reference to the database session.
    habit_object (Habit):   Habit object that is related to the history
                            entries, which will be deleted.
    """
    history_entries_to_be_deleted = (
        session.query(HabitHistory)
        .filter(HabitHistory.habit_key == habit_object.habit_name)
        .all()
    )
    for entry in history_entries_to_be_deleted:
        session.delete(entry)
    session.commit()

# endregion
