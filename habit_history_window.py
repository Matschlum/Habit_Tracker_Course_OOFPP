''' 

tbd

'''

# Standard library imports
import tkinter as tk
from tkinter import ttk

# Related third party imports

# Import from other modules

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

        self.session = session
        # endregion

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
