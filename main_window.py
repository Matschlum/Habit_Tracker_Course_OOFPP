'''
This module contains the MainWindow Class

-----
Description
This module is used to create the representation of the
main window for the application using tkinter.

-----
Classes
MainWindow
'''

# Standard library imports
import tkinter as tk
from tkinter import ttk
# Related third party imports

# Import from other modules
from db_object_functions import (
    change_active_passiv_status,
    manage_tracking_status,
)
from db_filter_functions import(
    filter_habits,
    filter_db_for_names
)
from pop_up_windows import(
    ShowHighscoreWindow,
    InputMessageWindow
)
from create_new_change_habit_window import(
    CreateChangeHabitWindow
)
from habit_history_window import(
    ShowHabitHistory
)
from db_functions import(
    delete_entries_from_db
)

# Class MainWindow
class MainWindow():
    '''
    
    tbd

    '''

    def __init__(self, session):
        '''

        tbd

        '''
        # ----------------------------------------
        # Creating the main setup for the window.
        # region ----------------------------------------

        # Define the main_root and the frames for the MainWinodw.
        self.main_root = tk.Tk()
        self.main_root.geometry("950x400")
        self.main_root.title("Habit Tracker")
        self.main_root.grid_columnconfigure(0, weight=1)
        
        self.main_frame = tk.Frame(self.main_root)
        self.main_frame.grid(sticky="nsew")
        self.subframe_top_buttons = tk.Frame(self.main_frame)
        self.subframe_top_buttons.grid(
            row=0, column=0,
            sticky="w"
        )
        self.subframe_table = tk.Frame(self.main_frame)
        self.subframe_table.grid(
            row=1, column=0,
            padx=10, pady=10,
            sticky="nsew"
        )
        self.subframe_low_buttons = tk.Frame(self.main_frame)
        self.subframe_low_buttons.grid(
            row=2, column=0,
            padx=10, pady=10,
            sticky="w"
        )
        
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(2, weight=1)
        self.subframe_top_buttons.grid_columnconfigure(0, weight=1)
        self.subframe_top_buttons.grid_columnconfigure(1, weight=1)
        self.subframe_table.grid_columnconfigure(0, weight=1)
        self.subframe_low_buttons.grid_columnconfigure(0, weight=1)

        # Set the DB session for the MainClass.
        self.session = session

        # Set the default settings for the filter options.
        self.habit_period_filter = None
        self.habit_active_filter = 0
        #endregion

        # ----------------------------------------
        # Creating all widgets for the subframe_top_buttons
        # region ----------------------------------------

        self.create_new_habit_button = tk.Button(
            self.subframe_top_buttons,
            text="Create New Habit",
            command=self.click_create_new_habit
        )
        self.show_highscore_button = tk.Button(
            self.subframe_top_buttons,
            text="Show Highscore Streak",
            command=self.click_show_highscore
        )
        self.close_application_button = tk.Button(
            self.subframe_top_buttons,
            text="Close Application",
            command=self.click_close_application
        )
        self.show_history_button = tk.Button(
            self.subframe_top_buttons,
            text="Show History",
            command=self.click_show_history
        )
        self.reset_all_filters_button = tk.Button(
            self.subframe_top_buttons,
            text="Reset all filters",
            command=self.click_reset_filter
        )
        self.show_active_passiv_habits_button = tk.Button(
            self.subframe_top_buttons,
            text="Show tracked/not tracked habits",
            command=self.click_filter_active
        )
        self.show_daily_button = tk.Button(
            self.subframe_top_buttons,
            text="Show only daily tracked habits",
            command=lambda: self.click_show_period(1)
        )
        self.show_every_other_day_button = tk.Button(
            self.subframe_top_buttons,
            text="Show evey other day tracked habits",
            command=lambda: self.click_show_period(2)
        )
        self.show_weekly_button = tk.Button(
            self.subframe_top_buttons,
            text="Show weekly tracked habits",
            command=lambda: self.click_show_period(7)
        )
        #endregion

        # ----------------------------------------
        # Creating all widgets for the subframe_lower_buttons.
        # region ----------------------------------------
        self.change_active_button = tk.Button(
            self.subframe_low_buttons,
            text="Change Active/Passiv",
            command=self.click_change_active_passive
        )
        self.change_tracking_status_button = tk.Button(
            self.subframe_low_buttons,
            text="Mark as complete",
            command=self.click_change_tracking_status
        )
        self.change_habit_button = tk.Button(
            self.subframe_low_buttons,
            text="Change Habit",
            command=self.click_change_habit
        )
        self.delete_habit_button = tk.Button(
            self.subframe_low_buttons,
            text="Delete Habit",
            command=self.click_delete_habit
        )
        #endregion

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
            "habit_description"
        ]
        self.habit_table = ttk.Treeview(
            self.subframe_table,
            column=column_lst,
            show="headings"
        )
        for entry in column_lst:
            formated_heading = " ".join(entry.split("_")).capitalize()
            self.habit_table.heading(
                entry,
                text=formated_heading,
                anchor=tk.W
            )
            self.habit_table.column(entry, minwidth=50, width=50)
        self.load_data_to_table()
        #endregion

        # ----------------------------------------
        # Place the widgets into the frames.
        # region ----------------------------------------

        # Placing the widgets for the first row.
        self.create_new_habit_button.grid(
            row=0, column=0,
            padx=10, pady=10,
            stick="w"
        )
        self.show_highscore_button.grid(
            row=0, column=1,
            padx=10, pady=10,
            sticky="w"
        )
        self.show_history_button.grid(
            row=0, column=2,
            padx=10, pady=10,
            sticky="w"
        )
        self.close_application_button.grid(
            row=0, column=4,
            padx=10, pady=10,
            sticky="w"
        )
        # Placing the widgets for the second row.
        self.reset_all_filters_button.grid(
            row=1, column=0,
            padx=10, pady=10,
            sticky="w"
        )
        self.show_active_passiv_habits_button.grid(
            row=1, column=1,
            padx=10, pady=10,
            sticky="w"
        )
        self.show_daily_button.grid(
            row=1, column=2,
            padx=10, pady=10,
            sticky="w"
        )
        self.show_every_other_day_button.grid(
            row=1, column=3,
            padx=10, pady=10,
            sticky="w"
        )
        self.show_weekly_button.grid(
            row=1, column=4,
            padx=10, pady=10,
            sticky="w"
        )
        # Placing the table (as third row)
        self.habit_table.grid(
            row=0, column=0, columnspan=10,
            padx=5, pady=5,
            sticky="nsew"
        )

        # Placing the widgets for the fourth row.
        self.change_active_button.grid(
            row=0, column=0,
            padx=10, pady=10,
            sticky="w"
        )
        self.change_tracking_status_button.grid(
            row=0, column=1,
            padx=10, pady=10,
            sticky="w"
        )
        self.change_habit_button.grid(
            row=0, column=2,
            padx=10, pady=10,
            sticky="w"
        )
        self.delete_habit_button.grid(
            row=0, column=3,
            padx=10, pady=10,
            sticky="w"
        )
        #endregion

    # ----------------------------------------
    # Methods
    # region ----------------------------------------

    # click_create_new_habit
    def click_create_new_habit(self):
        '''

        tbd

        '''
        CreateChangeHabitWindow(main_window=self, session=self.session, habit_object=None)
  
    # click_close_application
    def click_close_application(self):
        ''' 
       
        tbd

        '''
        self.main_root.destroy()

    # click_show_highscore
    def click_show_highscore(self):
        ''' 

        tbd

        '''
        ShowHighscoreWindow(self.session)

    # click_show_history
    def click_show_history(self):
        ''' 

        tbd

        '''
        ShowHabitHistory(session=self.session)

    # click_filter_active
    def click_filter_active(self):
        ''' 

        tbd

        '''

        if self.habit_active_filter == 2:
            self.habit_active_filter = 0
        else:
            self.habit_active_filter += 1
        self.update_data_in_table()

    # click_show_period
    def click_show_period(self, period: int):
        ''' 

        tbd

        '''
        self.habit_period_filter = period
        self.update_data_in_table()

    # click_reset_filter
    def click_reset_filter(self):
        ''' 

        tbd

        '''
        self.habit_period_filter = None
        self.habit_active_filter = 0
        self.update_data_in_table()

    # click_change_active_passive
    def click_change_active_passive(self):
        '''

        tbd

        '''
        selected_names = self.catch_selected_entries()
        if selected_names:
            change_active_passiv_status(
                session=self.session,
                names=selected_names
            )
            self.update_data_in_table()

    # click_change_tracking_status
    def click_change_tracking_status(self):
        '''

        tbd

        '''
        selected_names = self.catch_selected_entries()
        if selected_names:
            function_status_messages = manage_tracking_status(
                session=self.session,
                names=selected_names
            )
            InputMessageWindow(function_status_messages)
            self.update_data_in_table()

    # click_change_habit
    def click_change_habit(self):
        selected_names = self.catch_selected_entries()
        if selected_names:
            habit_entries = filter_db_for_names(session=self.session, names=selected_names)
            for habit_entry in habit_entries:
                CreateChangeHabitWindow(main_window=self, session=self.session, habit_object=habit_entry)

    # click_delete_habit
    def click_delete_habit(self):
        selected_names = self.catch_selected_entries()
        if selected_names:
            delete_entries_from_db(session=self.session, habit_names=selected_names)
            self.update_data_in_table()

    # load_data_to_table
    def load_data_to_table(self):
        ''' 
        
        tbd

        '''

        # Call the filter function
        table_content = filter_habits(
            self.session,
            self.habit_period_filter,
            self.habit_active_filter
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
                    active_status,                          #table_entry.habit_active_status,
                    tracking_status,                        #table_entry.habit_tracking_status,
                    table_entry.habit_next_due,
                    table_entry.habit_current_streak,
                    table_entry.habit_highscore_streak,
                    table_entry.habit_period,
                    table_entry.habit_total_fails,
                    table_entry.habit_start_date,
                    table_entry.habit_description
                )
            )

    # update_data_in_table
    def update_data_in_table(self):
        ''' 

        tbd

        '''
        # Delete the current entries in the table
        for row in self.habit_table.get_children():
            self.habit_table.delete(row)
        # Call the load_data_to_table function
        self.load_data_to_table()

    # catch_selected_entry
    def catch_selected_entries(self):
        '''

        tbd

        '''
        selected_entries = self.habit_table.selection()

        if selected_entries:
            selected_names = [self.habit_table.item(selected_entry, "values")[0]
                              for selected_entry in selected_entries
            ]
            return selected_names
        else:
            print("No entry selected")
    #endregion