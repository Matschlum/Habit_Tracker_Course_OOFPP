''' Creates the Habit class and HabitHistory class

-----
Description

tbd

-----
Classes
Habit
HabitHistory

'''

# ----------------------------------------
# Imports
# region ----------------------------------------

# Standard library imports
import datetime
# Related third party imports
from sqlalchemy import (
   Column as sqla_Column,
   String as sqla_String,
    Integer as sqla_Integer,
    Boolean as sqla_Boolean,
    Date as sqla_Date,
    DateTime as sqla_DateTime,
    ForeignKey as sqla_ForeignKey
)
# Import from other modules
from db_setup import (
    BaseClass
)
# endregion

# ----------------------------------------
# Classes
# ----------------------------------------

# Class Habit
class Habit(BaseClass):
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

    __tablename__ = "habit"

    # Defining the columns of the habit table
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

    # Constructor
    def __init__(
        self,
        habit_name,
        habit_description,
        habit_period,
        habit_active_status
    ):
        '''
        tbd

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
