'''
This module contains the two classes for habits.

----- Description -----
This module contains the two classes describing the habits and its history.

----- Classes -----
Habit:          This class is a representation of a habit.
HabitHistory:   This class is a representation of the history behind a habit.

----- Note -----
Both classes have the BaseClass as a parent.
'''

# ----------------------------------------
# Imports
# region ----------------------------------------

# Standard library imports
import datetime

# Related third party imports
from sqlalchemy import Boolean as sqla_Boolean
from sqlalchemy import Column as sqla_Column
from sqlalchemy import Date as sqla_Date
from sqlalchemy import DateTime as sqla_DateTime
from sqlalchemy import ForeignKey as sqla_ForeignKey
from sqlalchemy import Integer as sqla_Integer
from sqlalchemy import String as sqla_String

# Import from other modules
from db_setup import BaseClass

# endregion

# ----------------------------------------
# Classes
# region ----------------------------------------

# Class Habit
class Habit(BaseClass):
    '''
    This class is a representation of a habit.

    ----- Description -----
    This class describes all characteristics of a habit.

    ----- Attributes -----
    habit_name (str):               Represents the name of the habit, must be unique.
    habit_description (str):        Describing the habit in more detail.
    habit_period (int):             Representing the periodicity of the habit.
    habit_active_status (bool):     Showing if a habit is activly tracked or not.
    habit_tracking_status (bool):   Showing if a habit is completed within its time.
    habit_creation_date (date):     Containing the date when the habit has been created.
    habit_start_date (date):        Showing the start date, when the habit has been set to active.
    habit_current_streak (int):     Showing the current streak of completed in time.
    habit_highscore_streak (int):   Showing the highest streak reached for the active habit.
    habit_total_fails (int):        Counting the total fails to complete in time.
    habit_next_due (date):          Showing until when the habit has to be completed.
    '''

    __tablename__ = "habit"

    # ----------------------------------------
    # Defining each column in the habit table.
    # region ----------------------------------------
    habit_name = sqla_Column(
        "habit_name",
        sqla_String,
        primary_key=True
    )
    habit_description = sqla_Column(
        "habit_description",
        sqla_String
    )
    habit_period = sqla_Column(
        "habit_period",
        sqla_Integer
    )
    habit_active_status = sqla_Column(
        "habit_active_status",
        sqla_Boolean
    )
    habit_tracking_status = sqla_Column(
        "habit_tracking_status",
        sqla_Boolean
    )
    habit_creation_date = sqla_Column(
        "habit_creation_date",
        sqla_Date
    )
    habit_start_date = sqla_Column(
        "habit_start_date",
        sqla_Date
    )
    habit_current_streak = sqla_Column(
        "habit_current_streak",
        sqla_Integer
    )
    habit_highscore_streak = sqla_Column(
        "habit_highscore_streak",
        sqla_Integer
    )
    habit_total_fails = sqla_Column(
        "habit_total_fails",
        sqla_Integer
    )
    habit_next_due = sqla_Column(
        "habit_next_due",
        sqla_Date
    )

    # endregion

    # Constructor
    def __init__(
        self,
        habit_name,
        habit_description,
        habit_period,
        habit_active_status
    ):
        '''
        Initialize a new habit object.

        ----- Arguments -----
        habit_name (str):               Represents the name of the habit, must be unique.
        habit_description (str):        Describing the habit in more detail.
        habit_period (int):             Representing the periodicity of the habit.
        habit_active_status (bool):     Showing if a habit is activly tracked or not.
        '''
        self.habit_name = habit_name
        self.habit_description = habit_description
        self.habit_period = habit_period
        self.habit_active_status = habit_active_status
        self.habit_tracking_status = False
        self.habit_creation_date = datetime.datetime.now()
        self.habit_start_date = None
        self.habit_current_streak = 0
        self.habit_highscore_streak = 0
        self.habit_total_fails = 0
        self.habit_next_due = None


# Class HabitHistory
class HabitHistory(BaseClass):
    '''
    tbd

    -----
    Description
   
    tbd

    -----
    Arguments
    
    tbd

    -----
    Methods
    None
    '''

    __tablename__ = "habithistory"

    # Defining the columns of the table
    habit_id = sqla_Column(
        "entry_id",
        sqla_Integer,
        primary_key=True,
        autoincrement=True
    )
    habit_key = sqla_Column(
        "habit_key",
        sqla_String,
        sqla_ForeignKey("habit.habit_name"),
        nullable=False
    )
    fail_or_completion_date_time = sqla_Column(
        "fail_or_completion_date_time",
        sqla_DateTime
    )
    corresponding_due_date = sqla_Column(
        "corresponding_due_date",
        sqla_Date
    )
    type_of_completion = sqla_Column(
        "type_of_completion",
        sqla_Boolean
    )

    # Constructor
    def __init__(
        self,
        habit_key,
        fail_or_completion_date_time,
        corresponding_due_date,
        type_of_completion
    ):
        '''
        
        tbd

        '''

        self.habit_key = habit_key
        self.fail_or_completion_date_time = fail_or_completion_date_time
        self.corresponding_due_date = corresponding_due_date
        self.type_of_completion = type_of_completion

# endregion
