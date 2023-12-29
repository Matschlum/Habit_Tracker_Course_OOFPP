''' 

tbd

'''

# Standard library imports
import tkinter as tk

# Related third party imports

# Import from other modules

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

        self.highscore_frame = tk.Frame(self.highscore_root)
        self.highscore_frame.grid(sticky="nsew")

        self.session = session


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
            122: "ERROR: Standad lists have different length."
            }
        if message_codes is not None:
            self.input_message_root = tk.Tk()
            self.input_message_root.geometry("400x200")
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
                command=self.click_ok
            )
            self.ok_button.pack(padx=10, pady=10)
    
    # click_ok
    def click_ok(self):
        ''' 
       
        tbd

        '''
        self.input_message_root.destroy()
