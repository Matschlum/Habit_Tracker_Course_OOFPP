"""
This module is used to test the main database functions using unittest.

----- Functions to be tested -----
From module db_functions:
add_standard_habits_to_db
add_new_entry_to_db
delete_entries_from_db
modify_existing_object_in_db

From module db_object_functions:
change_active_passiv_status
manage_active_passiv_status
manage_passiv_habits
switch_active_passiv_status
setup_active_habits
reset-functions
set_tracking_status_to_true
streak_calculator                   # done

From module db_history_functions:
create_new_history_entry
delete_history_entries
"""
# ----------------------------------------
# Imports
# region ----------------------------------------
# Standard library imports
import unittest
from unittest.mock import Mock

# Related third party imports

# Import from other modules
from db_functions import *
from db_object_functions import *
from db_history_functions import *

# endregion

# ----------------------------------------
# Test module db_functions.
# region ----------------------------------------

# TestAddNewEntryToDb

class TestAddNewEntryToDb(unittest.TestCase):
    def setUp(self):
        self.habit_object = Mock()
        self.session = Mock()

    def test_correct_data(self):
        name = str("Test Habit")
        description = str("Test Description")
        period = int(17)
        active_status = True
        
        # Setting the search for check_name in the function to None to simulate that there is none such entry.
        self.session.query.return_value.filter_by.return_value.first.return_value = None

        return_value = add_new_entry_to_db(self.session, name, description, period, active_status)
        self.assertEqual(return_value, [0])

    def test_integer_for_description_and_name(self):
        name = int(17)
        description = int(17)
        period = int(5)
        active_status = True
        
        # Setting the search for check_name in the function to None to simulate that there is none such entry.
        self.session.query.return_value.filter_by.return_value.first.return_value = None
        return_value = add_new_entry_to_db(self.session, name, description, period, active_status)
        self.assertEqual(return_value, [100, 101, 0])

    def test_all_integer_input(self):
        pass
    
    def test_all_string_input(self):
        pass

# endregion

# ----------------------------------------
# Test module db_object_functions.
# region ----------------------------------------

# TestStreakCalculator
class TestStreakCalculator(unittest.TestCase):
    def setUp(self):
        self.session = Mock()
        self.habit_object = Mock()

    def test_streak_calculation_with_higher_highscore(self):
        self.habit_object.habit_current_streak = 17
        self.habit_object.habit_highscore_streak = 36
        
        streak_calculator(self.session, self.habit_object)
        self.assertEqual(self.habit_object.habit_current_streak, 18)
        self.assertEqual(self.habit_object.habit_highscore_streak, 36)

    def test_streak_calculator_with_current_equals_highscore(self):
        self.habit_object.habit_current_streak = 17
        self.habit_object.habit_highscore_streak = 17

        streak_calculator(self.session, self.habit_object)
        self.assertEqual(self.habit_object.habit_current_streak, 18)
        self.assertEqual(self.habit_object.habit_highscore_streak, 18)

    def test_streak_calculator_with_highscore_lower_than_current(self):
        self.habit_object.habit_current_streak = 36
        self.habit_object.habit_highscore_streak = 17

        streak_calculator(self.session, self.habit_object)
        self.assertEqual(self.habit_object.habit_current_streak, 37)
        self.assertEqual(self.habit_object.habit_highscore_streak, 37)

# endregion

# ----------------------------------------
# Test module db_history_functions.
# region ----------------------------------------

# endregion