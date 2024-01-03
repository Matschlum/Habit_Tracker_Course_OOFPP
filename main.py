'''
Starts the application.

----------------------------------------
Description

This module starts the application, if it is started as the main file
It sets up the database and creates a session, so that it is possible to
interact with the database (e.g. change values).
The program will ask if the standard entries should be added to the database
using a simple input line.
Afterwards the MainWindow instance will be created.

----------------------------------------
Note

For test purposes there is another region implemented to test the status of the
database during the development process.
'''

# ----------------------------------------
# Imports
# region ----------------------------------------

# Standard library imports

# Related third party imports

# Import from other modules
from db_setup import (
    start_db,
    start_db_session
)
from db_standard_entries import (
    standard_habit_name,
    standard_habit_active_status,
    standard_habit_description,
    standard_habit_period
)
from db_functions import (
    add_standard_habits_to_db
)
from habit_classes import (
    Habit,
    HabitHistory
)
from main_window import (
    MainWindow
)
from update_loop import (
    loop_for_update_due_date
)
# endregion

# ----------------------------------------
# Main
# region ----------------------------------------

if __name__ == "__main__":
    # Sets up the dababase and creates a session to it.
    engine = start_db(log=False)
    session = start_db_session(engine=engine)

    command_to_add_standard_values = input(
        "If you want to add the standard values type: yes\n"
    )
    if command_to_add_standard_values == "yes":
        status_add_standard_habits = add_standard_habits_to_db(
            session,
            standard_habit_name,
            standard_habit_description,
            standard_habit_period,
            standard_habit_active_status
        )

    # Creating an instance of the MainWindow (GUI)
    # to interact with the application.
    app = MainWindow(session=session)
    app.main_root.after(
        0,
        lambda: loop_for_update_due_date(
            session=session,
            main_window=app
        )
    )
    app.main_root.mainloop()

    # ----------------------------------------
    # CHECK and TEST SECTION
    # region ----------------------------------------

    # Check to see all entries in the database.
    all_habits = session.query(Habit).all()

    for habit in all_habits:
        print("Habit Name:", habit.habit_name)
        print("Description:", habit.habit_description)
        print("Period:", habit.habit_period)
        print("Active Status:", habit.habit_active_status)
        print("Tracking Status:", habit.habit_tracking_status)
        print("Creation Date:", habit.habit_creation_date)
        print("Start Date:", habit.habit_start_date)
        print("Current Streak:", habit.habit_current_streak)
        print("Highscore Streak:", habit.habit_highscore_streak)
        print("Total Fails:", habit.habit_total_fails)
        print("Next Due:", habit.habit_next_due)
        print("-------------------------")


    all_history_entries = session.query(HabitHistory).all()

    if all_history_entries:
        for entry in all_history_entries:
            print(f"Habit Name: {entry.habit_key}")
            print(f"Habit ID: {entry.habit_id}")
            print(f"Entry made: {entry.fail_or_completion_date_time}")
            print("-----------------------------")
    else:
        print("History empty")
    # endregion
# endregion
