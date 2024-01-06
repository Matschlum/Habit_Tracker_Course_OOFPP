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
    "Clean Apartment",
    "Do Sports",
    "Code in Python",
    "Learn Spanish",
    "Water plants",
]

# Standard Description
standard_habit_description = [
    "Clean everything",
    "Go to training",
    "Work on Python skills",
    "Spanish classes or hw",
    "Water plants",
]

# Standard Period
standard_habit_period = [
    7,
    2,
    1,
    2,
    7,
]

# Standard Active Status
standard_habit_active_status = [
    True,
    False,
    True,
    True,
    True,
]
