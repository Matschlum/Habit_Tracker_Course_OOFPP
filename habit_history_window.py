''' 

tbd

'''

# Standard library imports
import tkinter as tk
from tkinter import ttk
from unittest.loader import VALID_MODULE_NAME

# Related third party imports

# Import from other modules
from db_filter_functions import (
    filter_for_history_entries
)

# Class ShowHabitHistory
class ShowHabitHistory():
    '''

    tbd

    '''
    
    # Constructor
    def __init__(self, session):
        ''' 

        tbd

        '''
        # ----------------------------------------
        # Creating the main setup for the window.
        # region ----------------------------------------

        self.habit_history_root = tk.Tk()
        self.habit_history_root.geometry("950x400")
        self.habit_history_root.title("Habit History - Habit Tracker")
        self.habit_history_root.grid_columnconfigure(0, weight=1)

        self.habit_history_frame = tk.Frame(self.habit_history_root)
        self.habit_history_frame.grid(sticky = "nsew")
        
        self.subframe_filter_buttons = tk.Frame(self.habit_history_frame)
        self.subframe_filter_buttons.grid(
            row=0, column=0,
            padx=10, pady=10,
            sticky="nw"
        )
        self.subframe_history_table = tk.Frame(self.habit_history_frame)
        self.subframe_history_table.grid(
            row=1, column=0,
            padx=10, pady=10,
            sticky="nsew"
        )
        self.subframe_interaction_buttons = tk.Frame(self.habit_history_frame)
        self.subframe_interaction_buttons.grid(
            row=2, column=0,
            padx=10, pady=10,
            sticky="nw"
        )

        self.habit_history_frame.grid_columnconfigure(0, weight=1)
        self.habit_history_frame.grid_columnconfigure(1, weight=1)
        self.habit_history_frame.grid_columnconfigure(2, weight=1)
        self.subframe_filter_buttons.grid_columnconfigure(0, weight=1)
        self.subframe_history_table.grid_columnconfigure(0, weight=1)
        self.subframe_interaction_buttons.grid_columnconfigure(0, weight=1)

        self.session = session
        # endregion

        digit_validation = self.habit_history_root.register(
            self.validation_of_entry_data
        )
        widget_properties = {"padx": 10, "pady": 10, "sticky": "w"}

        self.status_filter = 0
        self.timespan = None

        # ----------------------------------------
        # Filter buttons
        # region ----------------------------------------
        self.reset_filter_button = tk.Button(
            self.subframe_filter_buttons,
            text="Reset filter settings",
            command=self.click_reset_filter_settings
        )

        self.show_fails_completed_filter_button = tk.Button(
            self.subframe_filter_buttons,
            text="Show fails / completed",
            command=self.click_show_fails_completed
        )

        self.show_timespan_only_filter_button = tk.Button(
            self.subframe_filter_buttons,
            text="Show timespan only",
            command=self.click_show_timespan_only
        )

        self.entry_timespan = tk.Entry(
            self.subframe_filter_buttons,
            validate="all",
            validatecommand=(digit_validation, "%P")
        )
        self.entry_timespan.bind("<KeyRelease>", self.on_releasing_key)

        self.timespan_information = tk.Label(
            self.subframe_filter_buttons,
            text="No entry or 0 means default (None),\nMax. value is 36500 days (approx. 100 years)",
            justify="left"
        )

        # ----------------------------------------
        # Creating the table to show the habits to the user.
        # region ----------------------------------------

        column_lst = [
            "habit_name",
            "fail_or_complete_date_and_time",
            "corresponding_due_date",
            "type_of_completion"
        ]
        self.history_table = ttk.Treeview(
            self.subframe_history_table,
            column=column_lst,
            show="headings"
        )
        for entry in column_lst:
            formated_heading = " ".join(entry.split("_")).capitalize()
            self.history_table.heading(
                entry,
                text=formated_heading,
                anchor=tk.W
            )
            self.history_table.column(entry, minwidth=50)
        self.load_history_data_to_table()
        # endregion


        # ----------------------------------------
        # Creating the widgets for the subframe_interactive_buttons
        # region ----------------------------------------
        self.close_window_button = tk.Button(
            self.subframe_interaction_buttons,
            text="Close Window",
            command=self.click_close_window
        )
        # endregion

        # ----------------------------------------
        # Place the widgets into the frames.
        # region ----------------------------------------

        self.reset_filter_button.grid(
            row=0, column=0,
            **widget_properties
        )
        self.show_fails_completed_filter_button.grid(
            row=0, column=1,
            **widget_properties
        )
        self.entry_timespan.grid(
            row=0, column=2,
            **widget_properties
        )
        self.show_timespan_only_filter_button.grid(
            row=0, column=3,
            **widget_properties
        )
        self.timespan_information.grid(
            row=0, column=4,
            **widget_properties
        )

        self.history_table.grid(
            row=0, column=0, columnspan=4,
            padx=10, pady=10,
            sticky="nsew"
        )

        self.close_window_button.grid(
            row=0, column=0,
            padx=10, pady=10,
            sticky="w"
        )
        # endregion

    # Class Methods
    # click_close_window
    def click_close_window(self):
        '''
        '''
        self.habit_history_root.destroy()


    # click_reset_filter_settings
    def click_reset_filter_settings(self):
        self.timespan = None
        self.status_filter = 0

        self.update_table()

    # click_show_fails_completed
    def click_show_fails_completed(self):
        if self.status_filter == 2:
            self.status_filter = 0
        else:
            self.status_filter += 1
        self.update_table()

    # click_show_timespan_only
    def click_show_timespan_only(self):
        if self.entry_timespan.get() == "" or self.entry_timespan.get() == "0":
            self.timespan = None
        else:
            user_input = int(self.entry_timespan.get())
            self.timespan = min(user_input, 36500)
        self.update_table()

    
    # on_pressing_key
    def on_releasing_key(self, not_used_event):
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
    def validation_of_entry_data(self, P):
        if P.isdigit() is True:
            return True
        elif P == "":
            return True
        else:
            return False

    # load_history_data_to_table
    def load_history_data_to_table(self):
        '''
        '''
        table_content = filter_for_history_entries(
            session=self.session,
            status_filter=self.status_filter,
            timespan=self.timespan
        )

        for table_entry in table_content:
            if table_entry.type_of_completion is False:
                completion_status = "Failed to complete"
            else:
                completion_status = "Completed in time"

            display_date_time = table_entry.fail_or_completion_date_time.strftime("%Y/%m/%d - %H:%M:%S")

            self.history_table.insert(
                parent="",
                index="end",
                value=(
                    table_entry.habit_key,
                    display_date_time,                      # table_entry.fail_or_completion_date_time
                    table_entry.corresponding_due_date,
                    completion_status                       # table_entry.type_of_completion
                )
            )

    # update_table
    def update_table(self):
        for row in self.history_table.get_children():
            self.history_table.delete(row)
        # Call the load_data_to_table function
        self.load_history_data_to_table()