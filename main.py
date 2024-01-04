"""
Starts the application.

----- Description -----
This module starts the application, if it is started as the main file
It sets up the database and creates a session, so that it is possible to
interact with the database (e.g. change values).
The program will ask if the standard entries should be added to the database
using a simple input line.
Afterwards the MainWindow instance will be created.
"""

# ----------------------------------------
# Imports
# region ----------------------------------------

# Standard library imports

# Related third party imports

# Import from other modules
from db_functions import add_standard_habits_to_db
from db_setup import start_db, start_db_session
from db_standard_entries import (
    standard_habit_active_status,
    standard_habit_description,
    standard_habit_name,
    standard_habit_period,
)
from main_window import MainWindow
from update_loop import loop_for_update_due_date

# endregion

# ----------------------------------------
# Main
# region ----------------------------------------

if __name__ == "__main__":
    # Sets up the dababase and creates a session to it.
    engine = start_db(log=False)
    session = start_db_session(engine=engine)

    input_for_standard_habits = input(
        "If you want to add the standard values type: yes\n"
    )
    if input_for_standard_habits == "yes":
        status_add_standard_habits = add_standard_habits_to_db(
            session,
            standard_habit_name,
            standard_habit_description,
            standard_habit_period,
            standard_habit_active_status,
        )

    # Creating an instance of the MainWindow (GUI) to interact with the
    # application.
    app = MainWindow(session=session)
    app.main_root.after(
        0, lambda: loop_for_update_due_date(session=session, main_window=app)
    )
    app.main_root.mainloop()

# endregion
