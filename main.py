''' Starts the habit tracker application

-----
Description

tbd

-----
Note
For developing purposes there is a section below the main window,
called CHECK. This is used during the developing to test and show
data in the command line. It has no other influence to the module.
'''

# ----------------------------------------
# Imports
# ----------------------------------------

# Standard library imports

# Related third party imports

# Import from other modules
from db_setup import(
    start_db,
    start_db_session
)
from db_standard_entries import(
    standard_habit_name,
    standard_habit_active_status,
    standard_habit_description,
    standard_habit_period
)
from db_functions import(
    add_standard_habits_to_db
)
from habit_classes import(
    Habit
)
from main_window import(
    MainWindow
)
from update_loop import(
    loop_for_update_due_date
)

# ----------------------------------------
# Main
# ----------------------------------------

if __name__ == "__main__":
    # DB setup
    engine = start_db(log=False)
    session = start_db_session(engine=engine)

    # Standard Habits
    status_add_standard_habits = add_standard_habits_to_db(
        session,
        standard_habit_name,
        standard_habit_description,
        standard_habit_period,
        standard_habit_active_status
    )

    app = MainWindow(session=session)
    app.main_root.after(0, lambda: loop_for_update_due_date(session=session, root=app.main_root))
    app.main_root.mainloop()


    # ----------------------------------------
    # CHECK and TEST SECTION
    # ----------------------------------------

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