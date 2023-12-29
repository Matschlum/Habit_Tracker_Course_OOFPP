''' 

tbd

'''

# Standard library imports
import tkinter as tk

# Import from other modules
from db_functions import add_new_entry_to_db
from pop_up_windows import InputMessageWindow

# Class CreateNewHabitWindow
class CreateNewHabitWindow():
    ''' Creates the Create New Habit Window

    -----
    Description
    This class creates the window incl. all entry
    fields for creating new habits.
    It is possible to save the information by
    calling the add_new_habit_to_db function.
    It consists of labels for description, entry-fields,
    a checkbox, a dropdown menu and buttons.

    -----
    Arguments
    session
        handed over, to connect with the db session
    main_window
        to communicate with the MainWindow
    period_selection_lst
        to make the user the three periods available
        (Daily, Every Other Day, Weekly)
    -----
    Methods
    click_apply
        Calls a function to add the new habit to db
        and updates the table in the mainwindow
    click_close
        Closes the window, without adding any
        data to the database
    click_apply_and_close
        Calls the apply and the close method
        to first save the data to the db and then
        close the window
    convert_period_to_integer
        Convertes the text information from the
        input field to a corresponding integer number
    '''

    # Constructor
    def __init__(self, main_window, session):
        ''' Constructor of the class

        -----
        Parameter
        session
            to connect with the db session
        '''
        # Create the window and define its properties.
        self.new_habit_root = tk.Tk()
        self.new_habit_root.geometry("750x400")
        self.new_habit_root.title("Create New Habit - Habit Tracker")
        self.new_habit_root.grid_columnconfigure(0, weight=1)

        # Define the layout of the window
        self.new_habit_frame = tk.Frame(self.new_habit_root)
        self.new_habit_frame.grid(sticky="nsew")
        self.new_habit_frame.grid_columnconfigure(0, weight=1, minsize=100)

        # Used to connect to the database
        self.session = session

        # Connect to the MainWindow
        self.main_window = main_window

        # Selection for periodicity values and variable to store
        # the value incl. standard value
        # How to modify:
        # 1 Change list in period_option_lst (add, remove, edit)
        # 2 adjust function convert_period_to_integer accordingly
        # 3 in main_window.py adjust the filter buttons
        self.period_option_lst = [
            "Daily",
            "Every Other Day",
            "Weekly"
        ]
        self.period_variable = tk.StringVar(
            self.new_habit_root
        )
        self.period_variable.set(
            self.period_option_lst[0]
        )
        # Set up the storage variable for the checkbox (acitve)
        self.active_checkbox_status = tk.BooleanVar(
            self.new_habit_root
        )
        self.active_checkbox_status.set(False)

        # SECTION WIDGET CREATION
        # LABELS
        # Headline Labels and entry fields
        self.headline_label_category = tk.Label(
            self.new_habit_frame,
            text="Category",
            justify="left"
        )
        self.headline_label_enter_data = tk.Label(
            self.new_habit_frame,
            text="Enter your data here",
            justify="left"
        )
        self.headline_label_default_info = tk.Label(
            self.new_habit_frame,
            text="Information about default values",
            justify="left"
        )
        # Habit Name
        self.name_label = tk.Label(
            self.new_habit_frame,
            text="Habit Name",
            justify="left"
        )
        self.name_entry = tk.Entry(
            self.new_habit_frame,
            text="Enter name"
        )
        self.name_information_label = tk.Label(
            self.new_habit_frame,
            text="Field is requiered",
            justify="left"
        )
        # Habit Description
        self.description_label = tk.Label(
            self.new_habit_frame,
            text="Habit Description",
            justify="left"
        )
        self.description_entry = tk.Text(
            self.new_habit_frame,
            height=3,
            width=50,
            wrap="word"
        )
        self.description_information_label = tk.Label(
            self.new_habit_frame,
            text="Default value will be 'default'",
            justify="left"
        )
        # Habit Periodicity
        self.period_label = tk.Label(
            self.new_habit_frame,
            text="Periodicity",
            justify="left"
        )
        self.period_entry = tk.OptionMenu(
            self.new_habit_frame,
            self.period_variable,
            *self.period_option_lst
        )
        self.period_information_label = tk.Label(
            self.new_habit_frame,
            text="the default value will be 'daily'",
            justify="left"
        )
        # Habit Active Status
        self.active_label = tk.Label(
            self.new_habit_frame,
            text="Do you want to track the habit?",
            justify="left"
        )
        self.active_entry = tk.Checkbutton(
            self.new_habit_frame,
            variable=self.active_checkbox_status
        )

        # BUTTONS
        self.apply_button = tk.Button(
            self.new_habit_frame,
            text="Apply",
            command=self.click_apply
        )
        self.apply_and_close_button = tk.Button(
            self.new_habit_frame,
            text="Apply and Close",
            command=self.click_apply_and_close
        )
        self.close_button = tk.Button(
            self.new_habit_frame,
            text="Close",
            command=self.click_close
        )

        # SECTION LAYOUT
        label_properties = {"padx": 10, "pady": 10, "sticky": "w"}
        # 1st Row
        self.headline_label_category.grid(
            row=0, column=0,
            padx=10, pady=10,
            sticky="w"
        )
        self.headline_label_enter_data.grid(
            row=0, column=1,
            **label_properties
        )
        self.headline_label_default_info.grid(
            row=0, column=2,
            **label_properties
        )
        # 2nd Row
        self.name_label.grid(
            row=1, column=0,
            **label_properties
            )
        self.name_entry.grid(
            row=1, column=1,
            **label_properties
        )
        self.name_information_label.grid(
            row=1, column=2,
            **label_properties
        )
        # 3rd Row
        self.description_label.grid(
            row=2, column=0,
            **label_properties
        )
        self.description_entry.grid(
            row=2, column=1,
            **label_properties
        )
        self.description_information_label.grid(
            row=2, column=2,
            **label_properties
        )
        # 4th Row
        self.period_label.grid(
            row=3, column=0,
            **label_properties
        )
        self.period_entry.grid(
            row=3, column=1,
            sticky="e"
        )
        self.period_information_label.grid(
            row=3, column=2,
            **label_properties
        )
        # 5th Row
        self.active_label.grid(
            row=4, column=0,
            **label_properties
        )
        self.active_entry.grid(
            row=4, column=1
        )

        # 6th Row
        self.apply_button.grid(
            row=5, column=0
        )
        self.apply_and_close_button.grid(
            row=5, column=1
        )
        self.close_button.grid(
            row=5, column=2
        )

    # Methods
    # click_apply(self)
    def click_apply(self):
        ''' Function to pass input values

        -----
        Description
        This function sends the data to add_new_entry_to_db
        function and stores its reply in the message.

        -----
        Parameter
        message
            to receive the return value from the add_new_entry_to_db
            function and to hand these message codes to
            the InputMessageWindoW
        '''
        message = add_new_entry_to_db(
            session=self.session,
            name=self.name_entry.get(),
            description=self.description_entry.get("1.0", tk.END).strip(),
            period=self.convert_period_to_integer(),
            active_status=self.active_checkbox_status.get()
        )
        # Update table in the MainWindow
        self.main_window.update_data_in_table()
        # Open Pop-Up to inform the user
        InputMessageWindow(message)

    # click_apply_and_close(self)
    def click_apply_and_close(self):
        ''' Saves the data and closes the window

        -----
        Description
        Calls the apply function and then the close
        function
        '''
        self.click_apply()
        self.click_close()

    # click_close(self)
    def click_close(self):
        ''' Closes the Create New Habit Window '''
        self.new_habit_root.destroy()

    # convert_period_to_integer(self)
    def convert_period_to_integer(self):
        ''' Used to convert the text into integer

        -----
        Description
        This function is used convert the text
        information provided by the input field
        to an integer value. For error handling,
        the function will any not recognized value
        transform into the integer 1 (means: daily)

        -----
        Return
        Returns the integer for periodicty needed
        for the add_new_habit_to_db function.

        -----
        Note
        The first if function can be left out, since
        it is automatically covered in the else condition.
        For a clear assignment of an integer is it written
        explicitly.
        '''
        period = self.period_variable.get()
        if period == self.period_option_lst[0]:
            period = int(1)
        elif period == self.period_option_lst[1]:
            period = int(2)
        elif period == self.period_option_lst[2]:
            period = int(7)
        else:
            period = int(1)
        return period

