'''
        self.habit_key = habit_key
        self.fail_or_completion_date_time = fail_or_completion_date_time
        self.corresponding_due_date = corresponding_due_date
        self.type_of_completion = type_of_completion
'''

# ----------------------------------------
# Imports
# region ----------------------------------------

# Standard library imports
import datetime
# Related third party imports

# Import from other modules
from habit_classes import (
    HabitHistory
)
# endregion

# create_new_history_entry
def create_new_history_entry(session, habit_object):
    date_and_time_of_history_entry = datetime.datetime.now()
    corresponding_due_date = habit_object.habit_next_due
    type_of_completion = habit_object.habit_tracking_status

    history_entry = HabitHistory(
        habit_key=habit_object.habit_name,
        fail_or_completion_date_time=date_and_time_of_history_entry,
        corresponding_due_date=corresponding_due_date,
        type_of_completion=type_of_completion
    )
    session.add(history_entry)
    session.commit()

# delete_history_entries
def delete_history_entries(session, habit_object):
    history_entries_to_be_deleted = session.query(HabitHistory).filter(HabitHistory.habit_key == habit_object.habit_name).all()
    for entry in history_entries_to_be_deleted:
        session.delete(entry)
    session.commit()
