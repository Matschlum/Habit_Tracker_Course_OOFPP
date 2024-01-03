"""
Used as a basis for the standard habits

----- Description -----
This module contains all information to create standard
entries for the database in form of lists.

----- Note -----
Habits can be created within the application itself.
If additional standard values are needed please follow
these rules:
(1) Keep the lists at the same length for
    name
    description
    period
    active_status

(2) Use the following types for the list entries only:
    name :              str
    description :       str
    period :            int
    active_status :     bool

(3) For periodicity all values from type int can be
    entered. Later in the in-app habit creation only
    values 1, 2 or 7 can be entered (via choice of
    daily, evey other day or weekly).
    The filters in the application will handle 1, 2, 7 as
    values. So it is highly recommended to only use these.
"""

# Standard Habit Names
standard_habit_name = [
    "Standard Habit 1",
    "Standard Habit 2",
    "Standard Habit 3",
    "Standard Habit 4",
    "Standard Habit 5",
    "Standard Habit 6",
    "Standard Habit 7",
    "Standard Habit 8",
]

# Standard Description
standard_habit_description = [
    "Standard Description 1",
    "Standard Description 2",
    "Standard Description 3",
    "Standard Description 4",
    "Standard Description 5",
    "Standard Description 6",
    "Standard Description 7",
    "Standard Description 8",
]

# Standard Period
standard_habit_period = [
    1,
    1,
    1,
    2,
    2,
    2,
    7,
    7,
]

# Standard Active Status
standard_habit_active_status = [
    True,
    True,
    False,
    True,
    False,
    False,
    True,
    False,
]
