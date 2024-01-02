"""
This module contains the filters to finde objects within the database.

----- Description -----
There are two different filter types in the module:
The first type is used to filter for objects according to selectable filter
settings.
The second type is used to filter for specific objects according to their name
or highscore.

----- Functions - only if not empty -----
filter_habits:                      Used to filter habits according to the
                                    settings in the main window.
filter_db_for_names:                Filter to find habits, mainly used to link
                                    the selection in the table with the habit
                                    object.
search_for_highscore_in_db:         Used to find the highscore value in the
                                    database.
filter_for_highscore_objects_in_db: Used to filter for the highscore value.
filter_for_history_entries:         Filters for history entries according to
                                    the settings in the window.
"""
# ----------------------------------------
# Imports
# region ----------------------------------------

# Standard library imports
import datetime
from typing import Optional

# Related third party imports
from sqlalchemy import and_ as sqla_and_

# Import from other modules
from habit_classes import Habit, HabitHistory

# endregion

# ----------------------------------------
# Functions
# region ----------------------------------------


# filter_habits
def filter_habits(
    session, period_filter: Optional[int] = None, active_filter: int = 0
) -> list[Habit]:
    """
    Filtering habits based on filter options.

    ----- Description -----
    This function filters the database for habits based on different filter
    options. The options are passed as parameters.

    ----- Arguments -----
    session (Session):      Containing the reference to the database session.
    period_filter (int):    Integer that represents the periodicity filter,
                            default: None.
    active_filter (int):    Integer that represents one of the three states
                            (active, passiv, all), default: 0 (all)

    ----- Returns -----
    table_content (list):   Returning a list containg objects of the habit
    class.
    """
    if period_filter in (1, 2, 7) and active_filter == 0:
        table_content = (
            session.query(Habit)
            .filter(
                sqla_and_(
                    Habit.habit_period == period_filter,
                    Habit.habit_active_status == True,
                )
            )
            .all()
        )
    elif period_filter in (1, 2, 7) and active_filter == 1:
        table_content = (
            session.query(Habit)
            .filter(
                sqla_and_(
                    Habit.habit_period == period_filter,
                    Habit.habit_active_status == False,
                )
            )
            .all()
        )
    elif period_filter in (1, 2, 7) and active_filter == 2:
        table_content = (
            session.query(Habit)
            .filter(Habit.habit_period == period_filter)
            .all()
        )
    elif period_filter not in (1, 2, 7) and active_filter == 0:
        table_content = (
            session.query(Habit)
            .filter(Habit.habit_active_status == True)
            .all()
        )
    elif period_filter not in (1, 2, 7) and active_filter == 1:
        table_content = (
            session.query(Habit)
            .filter(Habit.habit_active_status == False)
            .all()
        )
    else:
        table_content = session.query(Habit).all()
    return table_content


# filter_db_for_names
def filter_db_for_names(session, names: list) -> list[Habit]:
    """
    Filtering the table habit in the database for habit names.

    ----- Description -----
    This function filters the habit table in the database for habit names, the
    unique key. It returns then the corresponding habit objects.

    ----- Arguments -----
    session (Session):  Containing the reference to the database session.
    names (list):       A list of habit names.

    ----- Returns -----
    entries (list): Returning a list of habit objects.
    """
    entries = session.query(Habit).filter(Habit.habit_name.in_(names)).all()
    return entries


# search_for_highscore_in_db
def search_for_highscore_in_db(session) -> int:
    """
    Function to search for the highest value in the highscore column in the
    database.

    ----- Description -----
    This function searches for the highest value in the column
    habit_highscore_streak in the database and returns this value.

    ----- Arguments -----
    session (Session):  Containing the reference to the database session.

    ----- Returns -----
    highscore_value (int): Returning an integer, representing the highscore.
    """
    highscore_value = (
        session.query(Habit.habit_highscore_streak)
        .order_by(Habit.habit_highscore_streak.desc())
        .first()[0]
    )
    return highscore_value


# filter_for_highscore_objects_in_db
def filter_for_highscore_objects_in_db(
    session, highscore_value: int
) -> list[Habit]:
    """
    This function filters for all habits with the same highscore.

    ----- Description -----
    The function takes an integer, the highest value in the highscore column
    and returns a list of habits that have this value.

    ----- Arguments -----
    session (Session):      Containing the reference to the database session.
    highscore_value (int):  Value that represents the highscore and used to
                            filter for the habits.

    ----- Returns -----
    entries (list):         List of habits that have the highscore value.
    """
    entries = (
        session.query(Habit)
        .filter(Habit.habit_highscore_streak == highscore_value)
        .all()
    )
    return entries


# endregion

# ----------------------------------------
# HabitHistory class related filters
# region ----------------------------------------


# filter_for_history_entries
def filter_for_history_entries(
    session, status_filter: int, timespan: int
) -> list[HabitHistory]:
    """
    A filter function that searches for history data according to the input
    values.

    ----- Description -----
    This function filters the database table habithistory according to the
    parameters. It returns a list of history entries.

    ----- Arguments -----
    session (Session):      Containing the reference to the database session.
    status_Filter (int):    A value that indicates if it should be filtered for
                            only completed tasks, non-completed tasks / fails
                            or both. Can take the values 0, 1, 2.
    timespan (int):         An integer that describes the timespan from today
                            backwards where the user wants to see the history
                            entries. Max. value is 36500 (around 100 years).

    ----- Returns -----
    table_content (list):   A list of history entries is returned.
    """
    if timespan is None:
        if status_filter == 0:
            table_content = session.query(HabitHistory).all()
        elif status_filter == 1:
            table_content = (
                session.query(HabitHistory)
                .filter(HabitHistory.type_of_completion == True)
                .all()
            )
        elif status_filter == 2:
            table_content = (
                session.query(HabitHistory)
                .filter(HabitHistory.type_of_completion == False)
                .all()
            )
    else:
        reference_date = (
            datetime.date.today() - datetime.timedelta(days=timespan)
        )
        if status_filter == 0:
            table_content = (
                session.query(HabitHistory)
                .filter(
                    HabitHistory.fail_or_completion_date_time >= reference_date
                )
                .all()
            )
        elif status_filter == 1:
            table_content = (
                session.query(HabitHistory)
                .filter(
                    sqla_and_(
                        HabitHistory.fail_or_completion_date_time
                        >= reference_date,
                        HabitHistory.type_of_completion == True,
                    )
                )
                .all()
            )
        elif status_filter == 2:
            table_content = (
                session.query(HabitHistory)
                .filter(
                    sqla_and_(
                        HabitHistory.fail_or_completion_date_time
                        >= reference_date,
                        HabitHistory.type_of_completion == False,
                    )
                )
                .all()
            )
    return table_content

# endregion
