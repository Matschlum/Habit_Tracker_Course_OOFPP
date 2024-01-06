"""
This module is used to test the main database functions using unittest.

----- tested Functions -----
From module db_functions:
add_standard_habits_to_db
add_new_entry_to_db
modify_existing_object_in_db

From module db_object_functions:
manage_tracking_status
setup_active_habits
streak_calculator

From module db_filter_functions:
filter_habits
filter_for_history_entries

----- not tested Functions -----
From module db_functions:
delete_entries_from_db              This function consists of two function calls and a simple call of the delete method from SQLAlchemy's session.

From module db_object_functions:
change_active_passiv_status         This function only calls other functions.
manage_active_passiv_status         This function only calls other functions.
manage_passiv_habits                This function only calls other functions.
switch_active_passiv_status         This function only switches one boolean attribute from the habit.
reset-functions                     These functions only switch one attribute from the habit.
set_tracking_status_to_true         This function only switches one boolean attribute from the habit and calls one function.

From module db_history_functions:
create_new_history_entry            This function creates a new instance of the HabitHistory object based on the input by 
delete_history_entries              This function consists of a simple search for objects in the database and the call of the delete method from SQLAlchemy's session.

From module db_filter_functions:
filter_db_for_names                 This is a simple filtering for names using SQLAlchemy. No testing needed.
search_for_highscore_in_db          This is a simple search for a value in a specific column using SQLAlchemy. No testing needed.
filter_for_highscore_objects_in_db  This is a simple search for a value in a specific column using SQLAlchemy. No testing needed.
"""
# ----------------------------------------
# Imports
# region ----------------------------------------
# Standard library imports
import unittest
from unittest.mock import Mock, MagicMock

# Related third party imports

# Import from other modules
from db_filter_functions import *
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
        return_value = add_new_entry_to_db(
            self.session, name, description, period, active_status
        )
        self.assertEqual(return_value, [0])

    def test_integer_for_description_and_name(self):
        name = int(17)
        description = int(17)
        period = int(5)
        active_status = True

        # Setting the search for check_name in the function to None to simulate that there is none such entry.
        self.session.query.return_value.filter_by.return_value.first.return_value = None
        return_value = add_new_entry_to_db(
            self.session, name, description, period, active_status
        )
        self.assertEqual(return_value, [100, 101, 0])

    def test_all_integer_input(self):
        name = int(17)
        description = int(17)
        period = int(5)
        active_status = int(17)

        # Setting the search for check_name in the function to None to simulate that there is no such entry.
        self.session.query.return_value.filter_by.return_value.first.return_value = None
        return_value = add_new_entry_to_db(
            self.session, name, description, period, active_status
        )
        self.assertEqual(return_value, [112])

    def test_all_string_input(self):
        name = str("Test")
        description = str("Test")
        period = str("Test")
        active_status = str("Test")

        # Setting the search for check_name in the function to None to simulate that there is no such entry.
        self.session.query.return_value.filter_by.return_value.first.return_value = None
        return_value = add_new_entry_to_db(
            self.session, name, description, period, active_status
        )
        self.assertEqual(return_value, [113, 112])

    def test_all_empty(self):
        name = ""
        description = ""
        period = ""
        active_status = ""

        # Setting the search for check_name in the function to None to simulate that there is no such entry.
        self.session.query.return_value.filter_by.return_value.first.return_value = None
        return_value = add_new_entry_to_db(
            self.session, name, description, period, active_status
        )
        self.assertEqual(return_value, [113, 112, 114])

    def test_all_None(self):
        name = None
        description = None
        period = None
        active_status = None

        # Setting the search for check_name in the function to None to simulate that there is no such entry.
        self.session.query.return_value.filter_by.return_value.first.return_value = None
        return_value = add_new_entry_to_db(
            self.session, name, description, period, active_status
        )
        self.assertEqual(return_value, [113, 112, 114])


# TestAddStandardHabitsToDb
class TestAddStandardHabitsToDb(unittest.TestCase):
    def setUp(self):
        self.session = Mock()

    def test_single_values_instead_of_integers(self):
        name = "Test"
        description = "Description"
        period = 17
        active_status = True

        return_value = add_standard_habits_to_db(
            self.session, name, description, period, active_status
        )
        self.assertEqual(return_value, [123])

    def test_different_length_of_input_values(self):
        name = ["Test 1", "Test 2", "Test 3"]
        description = ["Descrip 1", "Descrip 2"]
        period = [17, 18, 19, 20]
        active_status = [True]

        return_value = add_standard_habits_to_db(
            self.session, name, description, period, active_status
        )
        self.assertEqual(return_value, [122])

    def test_integers_in_list_for_names(self):
        name = [1, 2, 3]
        description = ["Descrip 1", "Descrip 2", "Descrip 3"]
        period = [17, 18, 19]
        active_status = [True, False, True]
        # Expecting [100, 1, 100, 1, 100, 1] because the function add_new_entry_to_db.
        # Return of 100: each passed name is an integer and gets converted to a string -> warning message
        # Return of 1: the check_name is not None - and therefore there is a habit with this name for the test
        # For proper tests of add_new_entry_to_db see class TestAddNewEntryToDb
        return_value = add_standard_habits_to_db(
            self.session, name, description, period, active_status
        )
        self.assertEqual(return_value, [100, 1, 100, 1, 100, 1])

    def test_working_input(self):
        name = ["Test 1", "Test 2", "Test 3"]
        description = ["Descrip 1", "Descrip 2", "Descrip 3"]
        period = [17, 18, 19]
        active_status = [True, False, True]
        # Expecting [1, 1, 1] because the function add_new_entry_to_db.
        # Return of 1: the check_name is not None - and therefore there is a habit with this name for the test
        # For proper tests of add_new_entry_to_db see class TestAddNewEntryToDb
        return_value = add_standard_habits_to_db(
            self.session, name, description, period, active_status
        )
        self.assertEqual(return_value, [1, 1, 1])

    def test_mixed_values_in_all_lists(self):
        name = [2, "Test 2", "Test 3"]
        description = ["Descrip 1", 7, "Descrip 3"]
        period = [17, 18, "Test"]
        active_status = [True, "Test", True]

        return_value = add_standard_habits_to_db(
            self.session, name, description, period, active_status
        )
        self.assertEqual(return_value, [120])

    def test_empty_lists(self):
        name = []
        description = []
        period = []
        active_status = []

        return_value = add_standard_habits_to_db(
            self.session, name, description, period, active_status
        )
        self.assertEqual(return_value, [])


# TestModifiyExistingObjectsInDb:
class TestModifiyExistingObjectsInDb(unittest.TestCase):
    def setUp(self):
        self.session = Mock()
        self.habit_object = Mock()
        self.habit_object.habit_name = "Test"
        self.habit_object.habit_description = "Description"
        self.habit_object.habit_period = 17
        self.habit_object.habit_active_status = True

    def test_with_equal_input(self):
        name = "Test"
        description = "Description"
        period = 17
        active_status = True

        self.session.query.return_value.filter_by.return_value.first.return_value = None
        return_value = modify_existing_object_in_db(
            self.session, self.habit_object, name, description, period, active_status
        )
        self.assertEqual(return_value, [401, 402, 403, 404])

    def test_with_new_valid_input(self):
        name = "New Test"
        description = "New Description"
        period = 18
        active_status = False

        self.session.query.return_value.filter_by.return_value.first.return_value = None
        return_value = modify_existing_object_in_db(
            self.session, self.habit_object, name, description, period, active_status
        )
        self.assertEqual(return_value, [301, 302, 303, 304])

    def test_with_None_inputs(self):
        name = None
        description = None
        period = None
        active_status = None

        self.session.query.return_value.filter_by.return_value.first.return_value = None
        return_value = modify_existing_object_in_db(
            self.session, self.habit_object, name, description, period, active_status
        )
        self.assertEqual(return_value, [114])

    def test_with_name_not_none_rest_none(self):
        name = "Test Not None"
        description = None
        period = None
        active_status = None

        self.session.query.return_value.filter_by.return_value.first.return_value = None
        return_value = modify_existing_object_in_db(
            self.session, self.habit_object, name, description, period, active_status
        )
        self.assertEqual(return_value, [411, 412, 413, 301, 302, 303, 304])

    def test_with_emtpy_str_inputs(self):
        name = ""
        description = ""
        period = ""
        active_status = ""

        self.session.query.return_value.filter_by.return_value.first.return_value = None
        return_value = modify_existing_object_in_db(
            self.session, self.habit_object, name, description, period, active_status
        )
        self.assertEqual(return_value, [114])

    def test_with_emtpy_str_inputs_name_different(self):
        name = "Test not empty"
        description = ""
        period = ""
        active_status = ""

        self.session.query.return_value.filter_by.return_value.first.return_value = None
        return_value = modify_existing_object_in_db(
            self.session, self.habit_object, name, description, period, active_status
        )
        self.assertEqual(return_value, [412, 413, 301, 302, 303, 304])


# endregion

# ----------------------------------------
# Test module db_object_functions.
# region ----------------------------------------


# TestManageTrackingStatus
class TestManageTrackingStatus(unittest.TestCase):
    def setUp(self):
        self.session = MagicMock()
        self.test_name_list = ["Name"]

    def test_active_true_tracking_true(self):
        # Creating a mock_habit (test object)
        mock_habit = MagicMock(habit_active_status=True, habit_tracking_status=True)
        # Making the filter_db_for_names function return the mock habit
        self.session.query.return_value.filter.return_value.all.return_value = [
            mock_habit
        ]

        return_value = manage_tracking_status(self.session, self.test_name_list)
        self.assertEqual(return_value, [201])

    def test_active_false_tracking_false(self):
        # Creating a mock_habit (test object)
        mock_habit = MagicMock(habit_active_status=False, habit_tracking_status=False)
        # Making the filter_db_for_names function return the mock habit
        self.session.query.return_value.filter.return_value.all.return_value = [
            mock_habit
        ]

        return_value = manage_tracking_status(self.session, self.test_name_list)
        self.assertEqual(return_value, [200])


# TestSetupActiveHabits
class TestSetupActiveHabits(unittest.TestCase):
    def setUp(self):
        self.session = Mock()
        self.habit_object = Mock()

    def test_for_none_start_values(self):
        self.habit_object.habit_start_date = None
        self.habit_object.habit_next_due = None
        self.habit_object.habit_period = 17

        setup_active_habits(self.session, self.habit_object)
        self.assertEqual(self.habit_object.habit_start_date, datetime.date.today())
        self.assertEqual(
            self.habit_object.habit_next_due,
            datetime.date.today() + datetime.timedelta(days=17),
        )

    def test_for_start_date_only(self):
        self.habit_object.habit_start_date = datetime.date(2000, 1, 1)
        self.habit_object.habit_next_due = None
        self.habit_object.habit_period = 17

        setup_active_habits(self.session, self.habit_object)
        self.assertEqual(self.habit_object.habit_start_date, datetime.date(2000, 1, 1))
        self.assertEqual(
            self.habit_object.habit_next_due,
            datetime.date(2000, 1, 1) + datetime.timedelta(days=17),
        )


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
# Test module db_filter_functions
# region ----------------------------------------


# TestFilterHabits
class TestFilterHabits(unittest.TestCase):
    def setUp(self):
        self.session = Mock()
        self.habit_object_filtered = Mock()
        self.habit_object_all = Mock()
        self.session.query.return_value.filter.return_value.all.return_value = [
            self.habit_object_filtered
        ]
        self.session.query.return_value.all.return_value = [self.habit_object_all]

    def test_with_default_values(self):
        period_filter = None
        active_filter = 0

        return_value = filter_habits(self.session, period_filter, active_filter)
        self.assertEqual(return_value, [self.habit_object_filtered])

    def test_with_two_standard_inputs(self):
        period_filter = 2
        active_filter = 1

        return_value = filter_habits(self.session, period_filter, active_filter)
        self.assertEqual(return_value, [self.habit_object_filtered])

    def test_with_two_non_standard_inputs(self):
        period_filter = 17
        active_filter = 17

        return_value = filter_habits(self.session, period_filter, active_filter)
        self.assertEqual(return_value, [self.habit_object_all])

    def test_with_wrong_type_input(self):
        period_filter = "Test"
        active_filter = "Test"

        return_value = filter_habits(self.session, period_filter, active_filter)
        self.assertEqual(return_value, [self.habit_object_all])


# TestFilterForHistoryEntries
class TestForHistoryEntries(unittest.TestCase):
    def setUp(self):
        self.session = Mock()
        self.history_object_filtered = Mock()
        self.history_object_all = Mock()
        self.session.query.return_value.filter.return_value.all.return_value = [
            self.history_object_filtered
        ]
        self.session.query.return_value.all.return_value = [self.history_object_all]

    def test_with_None_inputs(self):
        status_filter = None
        timespan = None

        return_value = filter_for_history_entries(self.session, status_filter, timespan)
        self.assertEqual(return_value, [self.history_object_all])

    def test_with_two_wrong_type_input(self):
        status_filter = "Test"
        timespan = "Test"

        return_value = filter_for_history_entries(self.session, status_filter, timespan)
        self.assertEqual(return_value, [self.history_object_all])

    def test_with_two_valid_inputs(self):
        status_filter = 1
        timespan = 17

        return_value = filter_for_history_entries(self.session, status_filter, timespan)
        self.assertEqual(return_value, [self.history_object_filtered])


# endregion
