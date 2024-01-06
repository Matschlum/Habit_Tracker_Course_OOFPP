'''
This module is used to load sample data to the database.

----- Description -----
This module deletes all entries from the existing database and adds then the sample data.

----- Functions -----
add_sample_data_to_habits:    
add_sample_entries_to_history:
'''

# ----------------------------------------
# Imports
# region ----------------------------------------

# Standard library imports
import datetime
import sys
# Related third party imports

# Import from other modules
from db_functions import add_new_entry_to_db
from db_setup import start_db, start_db_session
from habit_classes import Habit, HabitHistory

# endregion

# ----------------------------------------
# Functions
# region ----------------------------------------

# add_sample_data_for_standard_habits
def add_sample_data_to_habits(session, data_lst):
    name = data_lst[0]
    description = data_lst[1]
    period = data_lst[2]
    active_status = data_lst[3]
    tracking_status = data_lst[4]
    creation_date = data_lst[5]
    start_date = data_lst[6]
    current_streak = data_lst[7]
    highscore = data_lst[8]
    total_fails = data_lst[9]
    next_due = data_lst[10]

    add_new_entry_to_db(session, name, description, period, active_status)

    habit_object = session.query(Habit).filter(Habit.habit_name == name).first()
    if habit_object:
        habit_object.habit_tracking_status = tracking_status
        habit_object.habit_creation_date = creation_date
        habit_object.habit_start_date = start_date
        habit_object.habit_current_streak = current_streak
        habit_object.habit_highscore_streak = highscore
        habit_object.habit_total_fails = total_fails
        habit_object.habit_next_due = next_due





# add_sample_entries_to_history
def add_sample_entries_to_history(data_lst):
    pass


# endregion

if __name__ == "__main__":
    # Security questions
    user_input = input("If you want to delete all current data and replace it with sample data type yes:   ")
    if user_input != "yes":
        print("Nothing changed")
        sys.exit()

    user_input_security = input("LAST WARNING: THIS WILL DELTE ALL DATA. Are you sure? If so type YES:   ")
    if user_input_security != "YES":
        print("Nothing changed")
        sys.exit()

    # Create session to database.
    engine = start_db(log=False)
    session = start_db_session(engine=engine)

    # ----------------------------------------
    # Delete all data in the database.
    # region ----------------------------------------
    session.query(Habit).delete()
    session.query(HabitHistory).delete()
    session.commit()
    # endregion

    # ----------------------------------------
    # Create sample entries
    # region ----------------------------------------

    habits_to_add = [
        ["Clean Apartment", "Clean everything", 7, True, True, datetime.date(2023, 10, 1), datetime.date(2023, 10, 1), 4, 4, 0, datetime.date(2099, 12, 1)],
        ["Do Sports", "Go to training", 2, False, False, datetime.date(2023, 10, 1), None, 0, 0, 0, None],
        ["Code in Python", "Work on Python skills", 1, True, True, datetime.date(2023, 10, 1), datetime.date(2023, 10, 1), 3, 17, 4, datetime.date(2099, 12, 1)],
        ["Learn Spanish", "Spanish classes or hw", 2, True, True, datetime.date(2023, 10, 1), datetime.date(2023, 10, 2), 2, 12, 1, datetime.date(2099, 12, 1)],
        ["Water plants", "Water plants", 7, True, False, datetime.date(2023, 10, 1), datetime.date(2023, 10, 3), 4, 4, 0, datetime.date(2099, 12, 1)],
    ]
    for habit in habits_to_add:
        add_sample_data_to_habits(session, habit)

    # Data testing
    habits = session.query(Habit).all()
    print("Data in database:")
    for habit in habits:
        print(f"Name: {habit.habit_name} - Period {habit.habit_period} - Active: {habit.habit_active_status} - Track: {habit.habit_tracking_status}")
        print(f"Cur St: {habit.habit_current_streak} - high: {habit.habit_highscore_streak} - fails: {habit.habit_total_fails}")
        print(f"Create: {habit.habit_creation_date} - Start: {habit.habit_start_date} - Next: {habit.habit_next_due}")
        print(f"Description: {habit.habit_description}")
        print("-----")

    #add_sample_entries_to_history()
