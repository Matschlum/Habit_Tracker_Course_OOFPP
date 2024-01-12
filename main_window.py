"""
This module contains the MainWindow Class

----- Description -----
This module is used to create the representation of the main window for the
application using tkinter.

----- Classes -----
MainWindow
"""

# ----------------------------------------
# Imports
# region ----------------------------------------

# Standard library imports
import sys
import tkinter as tk
from tkinter import ttk

# Related third party imports

# Import from other modules
from create_new_change_habit_window import CreateChangeHabitWindow
from db_filter_functions import filter_db_for_names, filter_habits
from db_functions import delete_entries_from_db
from db_object_functions import (
    change_active_passiv_status, manage_tracking_status
)
from habit_history_window import ShowHabitHistory
from pop_up_windows import InputMessageWindow, ShowHighscoreWindow

# endregion


# Class MainWindow
class MainWindow:
    """
    Class to create the main window of the application.

    ----- Description -----
    This class creates the main window of the application.
    The main window contains three sections:
    1. Buttons to create new habits, adjust filter settings and show highscore
    as well as history data.
    2. A table containg habits from the database according to the filter
    settings made.
    3. Buttons to adjust selected habits. E.g. mark them as completed.

    ----- Attributes -----
    session (Session):          Containing the reference to the database
                                session.
    habit_period_filter (int):  Attribute to filter the habit list.
    habit_active_filter (int):  Attribute to filter the habit list.
    main_root (tk.Tk):          Representation of the main Tkinter window.
    There are more attributes, like for frames, labels, buttons etc.

    ----- Methods -----
    click_create_new_habit:         Opens a window to create new habits.
    click_close_application:        Closes the entire application.
    click_show_highscore:           Opens a window to show the habits with the
                                    highest streak.
    click_show_history:             Opens a window to show the history.
    click_filter_active:            Alters the filter between all, only active
                                    and only passive.
    click_show_period:              Setts the filter setting to the clicked
                                    period.
    click_reset_filter:             Resets the filter settings to default.
    click_change_active_passive:    Calls functions to switch the active
                                    status.
    click_change_tracking_status:   Calls functions to change the tracking
                                    status to True.
    click_change_habit:             Opens a window to change existing habits.
    click_delete_habit:             Calls functions to delete the selected
                                    habits.
    load_data_to_table:             Loads the data from the database into the
                                    table.
    update_data_in_table:           Updates the data in the table.
    catch_selected_entries:         Used to get the habit names of the
                                    seleceted entries in the table.
    """

    # Constructor
    def __init__(self, session):
        """
        Constructor for the CreateChangeHabitWindow class.

        ----- Arguments -----
        session (Session):  Containing the reference to the database session.
        """
        # ----------------------------------------
        # Creating the main setup for the window.
        # region ----------------------------------------

        # Define the main_root and the frames for the MainWinodw.
        self.main_root = tk.Tk()
        self.main_root.geometry("950x400")
        self.main_root.title("Habit Tracker")
        self.main_root.grid_columnconfigure(0, weight=1)
        self.main_root.wm_protocol(
            "WM_DELETE_WINDOW", self.click_close_application
        )

        self.main_frame = tk.Frame(self.main_root)
        self.main_frame.grid(sticky="nsew")
        self.subframe_top_buttons = tk.Frame(self.main_frame)
        self.subframe_top_buttons.grid(row=0, column=0, sticky="w")
        self.subframe_table = tk.Frame(self.main_frame)
        self.subframe_table.grid(
            row=1, column=0, padx=10, pady=10, sticky="nsew"
        )
        self.subframe_low_buttons = tk.Frame(self.main_frame)
        self.subframe_low_buttons.grid(
            row=2, column=0, padx=10, pady=10, sticky="w"
        )

        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(2, weight=1)
        self.subframe_top_buttons.grid_columnconfigure(0, weight=1)
        self.subframe_top_buttons.grid_columnconfigure(1, weight=1)
        self.subframe_table.grid_columnconfigure(0, weight=1)
        self.subframe_low_buttons.grid_columnconfigure(0, weight=1)

        # Defining the main attributes and the default filter settings.
        self.session = session
        self.habit_period_filter = None
        self.habit_active_filter = 0

        widget_properties = {"padx": 10, "pady": 10, "sticky": "w"}

        # endregion

        # ----------------------------------------
        # Creating all widgets for the subframe_top_buttons
        # region ----------------------------------------

        self.create_new_habit_button = tk.Button(
            self.subframe_top_buttons,
            text="Create New Habit",
            command=self.click_create_new_habit,
        )
        self.show_highscore_button = tk.Button(
            self.subframe_top_buttons,
            text="Show High Score Streak",
            command=self.click_show_highscore,
        )
        self.close_application_button = tk.Button(
            self.subframe_top_buttons,
            text="Close Application",
            command=self.click_close_application,
        )
        self.show_history_button = tk.Button(
            self.subframe_top_buttons,
            text="Show History",
            command=self.click_show_history,
        )
        self.reset_all_filters_button = tk.Button(
            self.subframe_top_buttons,
            text="Reset all filters",
            command=self.click_reset_filter,
        )
        self.show_active_passiv_habits_button = tk.Button(
            self.subframe_top_buttons,
            text="Show tracked/not tracked habits",
            command=self.click_filter_active,
        )
        self.show_daily_button = tk.Button(
            self.subframe_top_buttons,
            text="Show only daily tracked habits",
            command=lambda: self.click_show_period(1),
        )
        self.show_every_other_day_button = tk.Button(
            self.subframe_top_buttons,
            text="Show evey other day tracked habits",
            command=lambda: self.click_show_period(2),
        )
        self.show_weekly_button = tk.Button(
            self.subframe_top_buttons,
            text="Show weekly tracked habits",
            command=lambda: self.click_show_period(7),
        )

        # endregion

        # ----------------------------------------
        # Creating all widgets for the subframe_lower_buttons.
        # region ----------------------------------------

        self.change_active_button = tk.Button(
            self.subframe_low_buttons,
            text="Change Active/Passive",
            command=self.click_change_active_passive,
        )
        self.change_tracking_status_button = tk.Button(
            self.subframe_low_buttons,
            text="Mark as complete",
            command=self.click_change_tracking_status,
        )
        self.change_habit_button = tk.Button(
            self.subframe_low_buttons,
            text="Change Habit",
            command=self.click_change_habit,
        )
        self.delete_habit_button = tk.Button(
            self.subframe_low_buttons,
            text="Delete Habit",
            command=self.click_delete_habit,
        )

        # endregion

        # ----------------------------------------
        # Creating the table to show the habits to the user.
        # region ----------------------------------------

        column_lst = [
            "habit_name",
            "habit_active_status",
            "habit_tracking_status",
            "habit_next_due",
            "habit_current_streak",
            "habit_highscore_streak",
            "habit_period",
            "habit_total_fails",
            "habit_start_date",
            "habit_description",
        ]
        self.habit_table = ttk.Treeview(
            self.subframe_table, column=column_lst, show="headings"
        )
        for entry in column_lst:
            formated_heading = " ".join(entry.split("_")).capitalize()
            self.habit_table.heading(entry, text=formated_heading, anchor=tk.W)
            self.habit_table.column(entry, minwidth=50, width=50)
        self.load_data_to_table()

        # endregion

        # ----------------------------------------
        # Place the widgets into the frames.
        # region ----------------------------------------

        first_row_widgets = [
            self.create_new_habit_button,
            self.show_highscore_button,
            self.show_history_button,
            self.close_application_button
        ]
        column_number = [0, 1, 2, 4]
        for i, widget in enumerate(first_row_widgets):
            widget.grid(row=0, column=column_number[i], **widget_properties)

        second_row_widgets = [
            self.reset_all_filters_button,
            self.show_active_passiv_habits_button,
            self.show_daily_button,
            self.show_every_other_day_button,
            self.show_weekly_button
        ]
        for i, widget in enumerate(second_row_widgets):
            widget.grid(row=1, column=i, **widget_properties)

        self.habit_table.grid(
            row=0, column=0, columnspan=10, padx=5, pady=5, sticky="nsew"
        )

        fourth_row_widgets = [
            self.change_active_button,
            self.change_tracking_status_button,
            self.change_habit_button,
            self.delete_habit_button
        ]
        for i, widget in enumerate(fourth_row_widgets):
            widget.grid(row=0, column=i, **widget_properties)

        # endregion

    # ----------------------------------------
    # Methods
    # region ----------------------------------------

    # click_create_new_habit
    def click_create_new_habit(self):
        """
        Creates an instance of the CreateChangeHabitWindow to create a new
        habit.

        ----- Description -----
        This functions does not use an existing habit object to pass to the
        class.
        By passing None for the habit object, the class will create an empty
        window to create a new habit, instead of adjusting an existing one.
        """
        CreateChangeHabitWindow(
            main_window=self, session=self.session, habit_object=None
        )

    # click_close_application
    def click_close_application(self):
        """
        Closes the entire application, including all open windows.
        """
        self.main_root.destroy()
        sys.exit()

    # click_show_highscore
    def click_show_highscore(self):
        """
        Creates an instance of the ShowHighscoreWindow class to show the habits
        with the highest streaks.
        """
        ShowHighscoreWindow(self.session)

    # click_show_history
    def click_show_history(self):
        """
        Creates an instance of the ShowHabitHistory class to show the user
        history.
        """
        ShowHabitHistory(session=self.session)

    # click_filter_active
    def click_filter_active(self):
        """
        Alters the filter setting between all, only active and only passive.

        ----- Description -----
        Alters the value for the status filter between
        0: only active
        1: only passive
        2: all
        Calls the function to update the table.
        """
        if self.habit_active_filter == 2:
            self.habit_active_filter = 0
        else:
            self.habit_active_filter += 1
        self.update_data_in_table()

    # click_show_period
    def click_show_period(self, period: int):
        """
        Gets the period number and sets the filter accordingly.

         ----- Description -----
         Receives the arguemnt from the button and uses it to set the period
         filter.
         Calls the function to update the table.

        ----- Arguments -----
        period (int):   Setting the period filter to this value.
        """
        self.habit_period_filter = period
        self.update_data_in_table()

    # click_reset_filter
    def click_reset_filter(self):
        """
        Resets all filter settings to default (show all active habits).
        """
        self.habit_period_filter = None
        self.habit_active_filter = 0
        self.update_data_in_table()

    # click_change_active_passive
    def click_change_active_passive(self):
        """
        Calls functions to change the active/passive status of the selected
        entries from the table.
        """
        selected_names = self.catch_selected_entries()
        if selected_names:
            change_active_passiv_status(
                session=self.session, names=selected_names
            )
            self.update_data_in_table()

    # click_change_tracking_status
    def click_change_tracking_status(self):
        """
        Calls functions to change the tracking status of the selected entries
        from the table to True.
        """
        selected_names = self.catch_selected_entries()
        if selected_names:
            function_status_messages = manage_tracking_status(
                session=self.session, names=selected_names
            )
            InputMessageWindow(function_status_messages)
            self.update_data_in_table()

    # click_change_habit
    def click_change_habit(self):
        """
        Creates an instance of the CreateChangeHabitWindow including passing an
        object, so that the window will be created as a change habit window.
        """
        selected_names = self.catch_selected_entries()
        if selected_names:
            habit_entries = filter_db_for_names(
                session=self.session, names=selected_names
            )
            for habit_entry in habit_entries:
                CreateChangeHabitWindow(
                    main_window=self,
                    session=self.session,
                    habit_object=habit_entry
                )

    # click_delete_habit
    def click_delete_habit(self):
        """
        Calls the delete function for the selected entries.
        """
        selected_names = self.catch_selected_entries()
        if selected_names:
            delete_entries_from_db(
                session=self.session, habit_names=selected_names
            )
            self.update_data_in_table()

    # load_data_to_table
    def load_data_to_table(self):
        """
        This functions is used to load the habit entries in the database into
        the table.

        ----- Description -----
        This function uses the filter attributes to load the data from the
        habit table into the window.
        """
        # Call the filter function
        table_content = filter_habits(
            self.session, self.habit_period_filter, self.habit_active_filter
        )

        # Load the data into the table in the main window.
        for table_entry in table_content:
            if table_entry.habit_active_status is False:
                active_status = "Not tracked"
            else:
                active_status = "Tracked"
            if table_entry.habit_tracking_status is False:
                tracking_status = "To be completed"
            else:
                tracking_status = "Completed"

            self.habit_table.insert(
                parent="",
                index="end",
                value=(
                    table_entry.habit_name,
                    active_status,  # table_entry.habit_active_status,
                    tracking_status,  # table_entry.habit_tracking_status,
                    table_entry.habit_next_due,
                    table_entry.habit_current_streak,
                    table_entry.habit_highscore_streak,
                    table_entry.habit_period,
                    table_entry.habit_total_fails,
                    table_entry.habit_start_date,
                    table_entry.habit_description,
                ),
            )

    # update_data_in_table
    def update_data_in_table(self):
        """
        This function updates the table content by removing all entries and
        then load it again.
        """
        for row in self.habit_table.get_children():
            self.habit_table.delete(row)
        self.load_data_to_table()

    # catch_selected_entry
    def catch_selected_entries(self):
        """
        This function is used to catch the selection in the table of the
        main window.

        ----- Returns -----
        selected_names (list):  List of names that are selected.
        """
        selected_entries = self.habit_table.selection()

        if selected_entries:
            selected_names = [
                self.habit_table.item(selected_entry, "values")[0]
                for selected_entry in selected_entries
            ]
        else:
            selected_names = []
        return selected_names

    # endregion
