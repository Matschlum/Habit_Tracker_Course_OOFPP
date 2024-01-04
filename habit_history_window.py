"""
This module contains the class to open and show the habit history.

----- Classes -----
ShowHabitHistory:   Representation of a window that shows all habit history
                    entries.
"""

# ----------------------------------------
# Imports
# region ----------------------------------------

# Standard library imports
import tkinter as tk
from tkinter import ttk

# Related third party imports

# Import from other modules
from db_filter_functions import filter_for_history_entries

# endregion


# Class ShowHabitHistory
class ShowHabitHistory:
    """
    Representation of a window that shows all habit history entries.

    ----- Description -----
    This class is used to show the habit history. Therefore it has methods to
    load the data.
    IT will offer different filters to the user as well.

    ----- Attributes -----
    session (Session):      Containing the reference to the database session.
    digit_validation (str): This attribute is for validation if the entry is a
                            digit or not.
    status_filter (int):    This is the filter for completed/not completed
                            habits within the window.
    timespan (int):         This is the filter for the timespan - from today
                            backwards in days.

    ----- Methods -----
    click_close_window:             Closing the window.
    click_reset_filter_settings:    Reseting the filter to default
                                    (all entries).
    click_show_fails_completed:     Swtiches between completed / not completed
                                    / both.
    click_show_timespan_only:       Using a user input to create a timespan
                                    for the history.
    on_releasing_key:               Function used to limit the entry for the
                                    timespan to 36500 days (ca. 100 years).
    validation_of_entry_data:       Checking if an input is a digit or an empty
                                    string (meaning: nothing).
    load_history_data_to_table:     Loads the data from the database to the
                                    table according to the filter settings.
    update_table:                   Updates the table content by removing
                                    all entries and then load the data again.
    """

    # Constructor
    def __init__(self, session):
        """
        Creates the window to show habit history entries.

        ----- Arguments -----
        session (Session):  Containing the reference to the database session.
        """
        # ----------------------------------------
        # Setting up the basics for the GUI to show the history.
        # region ----------------------------------------

        self.habit_history_root = tk.Tk()
        self.habit_history_root.geometry("950x400")
        self.habit_history_root.title("Habit History - Habit Tracker")
        self.habit_history_root.grid_columnconfigure(0, weight=1)

        self.habit_history_frame = tk.Frame(self.habit_history_root)
        self.habit_history_frame.grid(sticky="nsew")

        self.subframe_filter_buttons = tk.Frame(self.habit_history_frame)
        self.subframe_filter_buttons.grid(
            row=0, column=0, padx=10, pady=10, sticky="nw"
        )
        self.subframe_history_table = tk.Frame(self.habit_history_frame)
        self.subframe_history_table.grid(
            row=1, column=0, padx=10, pady=10, sticky="nsew"
        )
        self.subframe_interaction_buttons = tk.Frame(self.habit_history_frame)
        self.subframe_interaction_buttons.grid(
            row=2, column=0, padx=10, pady=10, sticky="nw"
        )

        self.habit_history_frame.grid_columnconfigure(0, weight=1)
        self.habit_history_frame.grid_columnconfigure(1, weight=1)
        self.habit_history_frame.grid_columnconfigure(2, weight=1)
        self.subframe_filter_buttons.grid_columnconfigure(0, weight=1)
        self.subframe_history_table.grid_columnconfigure(0, weight=1)
        self.subframe_interaction_buttons.grid_columnconfigure(0, weight=1)

        # Setting the main attributes that are used.
        self.session = session

        digit_validation = self.habit_history_root.register(
            self.validation_of_entry_data
        )
        widget_properties = {"padx": 10, "pady": 10, "sticky": "w"}

        self.status_filter = 0
        self.timespan = None

        # endregion

        # ----------------------------------------
        # Filter buttons
        # region ----------------------------------------

        self.reset_filter_button = tk.Button(
            self.subframe_filter_buttons,
            text="Reset filter settings",
            command=self.click_reset_filter_settings,
        )

        self.show_fails_completed_filter_button = tk.Button(
            self.subframe_filter_buttons,
            text="Show fails / completed",
            command=self.click_show_fails_completed,
        )

        self.show_timespan_only_filter_button = tk.Button(
            self.subframe_filter_buttons,
            text="Show timespan only",
            command=self.click_show_timespan_only,
        )

        self.entry_timespan = tk.Entry(
            self.subframe_filter_buttons,
            validate="all",
            validatecommand=(digit_validation, "%P"),
        )
        self.entry_timespan.bind("<KeyRelease>", self.on_releasing_key)

        self.timespan_information = tk.Label(
            self.subframe_filter_buttons,
            text=(
                "No entry or 0 means default (None),"
                "\nMax. value is 36500 days (approx. 100 years)"
            ),
            justify="left",
        )

        # endregion

        # ----------------------------------------
        # Creating the table to show the entries to the user.
        # region ----------------------------------------

        column_lst = [
            "habit_name",
            "fail_or_complete_date_and_time",
            "corresponding_due_date",
            "type_of_completion",
        ]
        self.history_table = ttk.Treeview(
            self.subframe_history_table, column=column_lst, show="headings"
        )
        for entry in column_lst:
            formated_heading = " ".join(entry.split("_")).capitalize()
            self.history_table.heading(
                entry, text=formated_heading, anchor=tk.W
            )
            self.history_table.column(entry, minwidth=50)
        self.load_history_data_to_table()

        # endregion

        # ----------------------------------------
        # Creating the widgets for the subframe_interaction_buttons
        # region ----------------------------------------
        self.close_window_button = tk.Button(
            self.subframe_interaction_buttons,
            text="Close Window",
            command=self.click_close_window,
        )

        # endregion

        # ----------------------------------------
        # Place the widgets into the frames.
        # region ----------------------------------------

        self.reset_filter_button.grid(row=0, column=0, **widget_properties)
        self.show_fails_completed_filter_button.grid(
            row=0, column=1, **widget_properties
        )
        self.entry_timespan.grid(row=0, column=2, **widget_properties)
        self.show_timespan_only_filter_button.grid(
            row=0, column=3, **widget_properties
        )
        self.timespan_information.grid(row=0, column=4, **widget_properties)

        self.history_table.grid(
            row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew"
        )

        self.close_window_button.grid(
            row=0, column=0, padx=10, pady=10, sticky="w"
        )

        # endregion

    # ----------------------------------------
    # Class Methods
    # region ----------------------------------------

    # click_close_window
    def click_close_window(self):
        """
        Closes the window by destroying the instance of the class.
        """
        self.habit_history_root.destroy()

    # click_reset_filter_settings
    def click_reset_filter_settings(self):
        """
        Resets the filter settings to the default values.

        ----- Description -----
        This functions resets the filter settings to the default values to show
        all habit history entries.
        Further it will update the table to show the new entries.
        """
        self.timespan = None
        self.status_filter = 0

        self.update_table()

    # click_show_fails_completed
    def click_show_fails_completed(self):
        """
        Alters the filter setting between all, only completed and only failed.

        ----- Description -----
        Alters the value for the status filter between
        0: all
        1: only completed
        2: only failed
        Calls the function to update the table.
        """
        if self.status_filter == 2:
            self.status_filter = 0
        else:
            self.status_filter += 1
        self.update_table()

    # click_show_timespan_only
    def click_show_timespan_only(self):
        """
        Taking the user input and store it in the timespan variable for
        filtering.
        """
        if self.entry_timespan.get() == "" or self.entry_timespan.get() == "0":
            self.timespan = None
        else:
            user_input = int(self.entry_timespan.get())
            self.timespan = min(user_input, 36500)
        self.update_table()

    # on_releasing_key
    def on_releasing_key(self, not_used_event):
        """
        This function controlls the user input in the entry field for the
        timespan.

        ----- Description -----
        This function takes the user input after releasing the keyboard and
        checks it for being a digit as well as if the total value is not above
        36500.
        If the value exceeds the limit, then the value is set to 36500 and the
        display is updated accordingly.

        ----- Arguments -----
        not_used_event: The binding method expects a function with two
                        arguments. This argument is just to satisfy the
                        requirements of the method although it is not used in
                        this method.
        """
        value_after_pressing = self.entry_timespan.get()
        if value_after_pressing.isdigit():
            if value_after_pressing.isdigit():
                value_after_pressing = int(value_after_pressing)
            else:
                value_after_pressing = 0

            value_after_pressing = min(value_after_pressing, 36500)

            self.entry_timespan.delete(0, tk.END)
            self.entry_timespan.insert(0, str(value_after_pressing))

    # validation_of_entry_data
    def validation_of_entry_data(self, P: str) -> bool:
        """
        This function is used to validate if the user input is a digit.

        ----- Arguments -----
        P (str):    Containg the key-value that has been pressed.

        ----- Returns -----
        boolean (bool):   Returns True or False
        """
        if (P.isdigit() is True) or P == "":
            return True
        elif P == "":
            return True
        else:
            return False

    # load_history_data_to_table
    def load_history_data_to_table(self):
        """
        This functions is used to load the history entries in the database into
        the table.

        ----- Description -----
        This function uses the filter attributes to load the data from the
        history table into the window.
        """
        table_content = filter_for_history_entries(
            session=self.session,
            status_filter=self.status_filter,
            timespan=self.timespan,
        )

        for table_entry in table_content:
            if table_entry.type_of_completion is False:
                completion_status = "Failed to complete"
            else:
                completion_status = "Completed in time"

            display_date_time = (
                table_entry
                .fail_or_completion_date_time
                .strftime("%Y/%m/%d - %H:%M:%S")
            )

            self.history_table.insert(
                parent="",
                index="end",
                value=(
                    table_entry.habit_key,
                    display_date_time,  # fail_or_completion_date_time
                    table_entry.corresponding_due_date,
                    completion_status,  # type_of_completion
                ),
            )

    # update_table
    def update_table(self):
        """
        This function updates the table content by removing all entries and
        then load it again.
        """
        for row in self.history_table.get_children():
            self.history_table.delete(row)
        self.load_history_data_to_table()

    # endregion
