''' 

tbd

'''

# Standard library imports
import tkinter as tk
from tkinter import ttk
from tkinter.tix import ROW

# Related third party imports

# Import from other modules
from db_filter_functions import (
    search_for_highscore_in_db,
    filter_for_highscore_objects_in_db
)

# Class ShowHighscoreWindow
class ShowHighscoreWindow():
    ''' 

    tbd

    '''

    # Constructor
    def __init__(self, session):

        ''' 

        tbd

        '''

        self.highscore_root = tk.Tk()
        self.highscore_root.geometry("400x400")
        self.highscore_root.title("Highscore Streak - Habit Tracker")
        self.highscore_root.grid_columnconfigure(0, weight=1)

        self.highscore_frame = tk.Frame(self.highscore_root)
        self.highscore_frame.grid(sticky="nsew")
        self.subframe_table = tk.Frame(self.highscore_frame)
        self.subframe_table.grid(
            row=0, column=0,
            padx=10, pady=10,
            sticky="nsew"
        )
        self.subframe_close_button = tk.Frame(self.highscore_frame)
        self.subframe_close_button.grid(
            row=1, column=0,
            padx=10, pady=10,
            sticky="w"
        )

        self.highscore_frame.grid_columnconfigure(0, weight=1)
        self.highscore_frame.grid_columnconfigure(1, weight=1)
        self.subframe_table.grid_columnconfigure(0, weight=1)
        self.subframe_close_button.grid_columnconfigure(0, weight=1)

        self.session = session


        # ----------------------------------------
        # Creating the widget for the subframe_close_button.
        # ----------------------------------------
        # region
        self.close_button = tk.Button(
            self.subframe_close_button,
            text="Close window",
            command=self.click_close_window
        )
        # endregion

        # ----------------------------------------
        # Creating the table to show the habits to the user.
        # ----------------------------------------
        # region
        column_lst = [
            "habit_name",
            "habit_highscore_streak",
        ]
        self.habit_highscore_table = ttk.Treeview(
            self.subframe_table,
            column=column_lst,
            show="headings"
        )
        for entry in column_lst:
            formated_heading = " ".join(entry.split("_")).capitalize()
            self.habit_highscore_table.heading(
                entry,
                text=formated_heading,
                anchor=tk.W
            )
            self.habit_highscore_table.column(entry, minwidth=50)
        self.load_highscore_data_to_table()
        # endregion

        # ----------------------------------------
        # Place the widgets into the frames.
        # ----------------------------------------
        # region
        self.habit_highscore_table.grid(
            row=0, column=0,
            padx=10, pady=10,
            sticky="nsew"
        )
        self.close_button.grid(
            row=0, column=0,
            padx=10, pady=10,
            sticky="e"
        )

        # endregion

    # ----------------------------------------
    # Methods
    # ----------------------------------------

    # load_highscore_data_to_table
    def load_highscore_data_to_table(self):
        highscore_value = search_for_highscore_in_db(session=self.session)
        highscore_objects = filter_for_highscore_objects_in_db(session=self.session, highscore_value=highscore_value)

        for highscore_habit in highscore_objects:
            self.habit_highscore_table.insert(
                parent="",
                index="end",
                value=(
                    highscore_habit.habit_name,
                    highscore_habit.habit_highscore_streak
                )
            )

    # click_close_window
    def click_close_window(self):
        self.highscore_root.destroy()



# Class InputMessageWindow
class InputMessageWindow():
    ''' 

    tbd

    '''
    def __init__(self, message_codes):
        ''' 

        tbd

        '''

        messages = {
            0: "Habit Successfully added to the database",
            1: "ERROR: Habit with this name already existing",
            100: "WARNING: Name was converted to a string.",
            101: "WARNING: Description was converted to a string.",
            112: ("ERROR: Status for active was not of type boolean. "
                  "No data added."),
            113: "ERROR: Periodicity was not of type integer. No data added.",
            114: "ERROR: Name cannot be empty. No data added.",
            120: "ERROR: Standard Periodicty does not only contain integers.",
            121: ("ERROR: Standard status for active does not only "
                  "contain boolean."),
            122: "ERROR: Standad lists have different length.",
            200: "ERROR: Habit tracking status cannot be changed, habit marked as inactive.",
            301: "Name of habit changed.",
            302: "Description of habit changed.",
            303: "Periodicity of habit changed.",
            304: "Status for active of habit changed.",
            401: "No name changed.",
            402: "No description changed.",
            403: "No periodicity changed.",
            404: "No status for active chagned."
            }
        if message_codes is not None:
            self.input_message_root = tk.Tk()
            self.input_message_root.geometry("480x280")
            self.input_message_root.title("Information - Habit Tracker")
            self.input_message_frame = tk.Frame(self.input_message_root)
            self.input_message_frame.pack(fill="both", expand=True)
            for code in message_codes:
                message_text = messages.get(code, f"Unknown error: Code {code}")
                label = tk.Label(self.input_message_frame, text=message_text)
                label.pack(anchor="w", padx=10, pady=10)
            self.ok_button = tk.Button(
                self.input_message_frame,
                text="Ok",
                command=self.click_close_window
            )
            self.ok_button.pack(padx=10, pady=10)
    
    # click_ok
    def click_close_window(self):
        ''' 
       
        tbd

        '''
        self.input_message_root.destroy()
