''' 

tbd

'''

# Standard library imports
import tkinter as tk

# Related third party imports

# Import from other modules

# Class ShowHabitHistory
class ShowHabitHistory():
    ''' Creates the Habit History Window

    -----
    Description
    This class creates the window to show the habit history
ed)
    -----
    Arguments
    session
        to handle the db session

    -----
    Methods
    click_close_window
        closes the window
    '''
    
    # Constructor
    def __init__(self, session):
        ''' Constructor of the ShowHabitHistory class

        -----
        Parameters
        session
            session used to load the data from the db
        '''
        # Create the window and define its properties.
        self.habit_history_root = tk.Tk()
        self.habit_history_root.geometry("950x400")
        self.habit_history_root.title("Habit History - Habit Tracker")
        # Expand the column within the window
        # Meaning: The frame will stay within the borders of the window
        self.habit_history_root.grid_columnconfigure(0, weight=1)
        #self.main_root.grid_rowconfigure(0, weight=1)
        # Connect to the database
        self.session = session

        # Define the layout of the main window
        self.habit_history_frame = tk.Frame(self.habit_history_root)
        # Let the buttons stay on the top left side
        self.habit_history_frame.grid(sticky = "nw")
        # Define that the first two rows of the frame shoudl stay within the
        # frame, leading to them staying in the window
        self.habit_history_frame.grid_columnconfigure(0, weight=1)
        self.habit_history_frame.grid_columnconfigure(1, weight=1)
        #self.all_habits_frame.grid_rowconfigure(0, weight=1)

        # SECTION WIDGET CREATION
        # Creating all the buttons on the Habit History Window
        self.close_window_button = tk.Button(
            self.habit_history_frame,
            text="Close",
            command=self.click_close_window
        )
        self.close_window_button.grid(
            row=0, column=2,
            padx=10, pady=10,
            sticky="w"
        )

    # Class Methods
    # click_create_new_habit
    def click_create_new_habit(self):
        pass

    # click_close_window
    def click_close_window(self):
        ''' closes the window '''
        self.habit_history_root.destroy()
