"""
This module is used to create the window to change or add habits.

----- Description -----
The module contains the class to create the window for the user to add new
habits to the application, or to modify existing ones.

----- Classes -----
CreateChangeHabitWindow:    This is the class to create the change/add habit
window based on Tkinter.
"""
# ----------------------------------------
# Imports
# region ----------------------------------------

# Standard library imports
import tkinter as tk

# Import from other modules
from db_functions import add_new_entry_to_db, modify_existing_object_in_db
from pop_up_windows import InputMessageWindow

# endregion


# Class CreateChangeHabitWindow
class CreateChangeHabitWindow:
    """
    Class to create a window to change and modify habits.

    ----- Description -----
    This class creates a window, using tkinter, to allow creating and change
    habits.
    The class methods will forward also information to the InputMessageWindow
    class to inform the user if the change has been successfull or not.

    ----- Attributes -----
    main_window (MainWindow):       Containing the reference to the MainWindow.
    session (Session):              Containing the reference to the database
                                    session.
    habit_object (Habit):           Attribute to contain the object to be
                                    modified by the user.
    create_new_habit_flag (bool):   Indication if a new habit is created or an
                                    existing one is modified.
    create_change_root (tk.Tk):     Representation of the main Tkinter window.
    There are more attributes, like for frames, labels, buttons etc, as well as
    for data handling within the class.

    ----- Methods -----
    click_apply:            Command for button to add a new habit to the
                            database based on the values in the input fields.
    click_close:            Command for closing the window.
    click_apply_and_close:  Command for button to firstly add a new habit to
                            the database and then close the window.
    click_change_and_close: Command for button to firstly apply the changes to
                            the habit and then close the window.

    convert_period_to_integer:  Converter for the attribute handling the
    periodicity; converts the string into the corresponding integer value.

    ----- Note - only if not empty -----
    Currently there are three options for periodicity (daily, every other day
    and weekly). A description how to add, change, remove options is given in
    the readme.md.
    """

    def __init__(self, main_window, session, habit_object=None):
        """
        Constructor for the CreateChangeHabitWindow class.

        ----- Arguments -----
        main_window (MainWindow):   Containing the reference to the main
                                    window.
        session (Session):          Containing the reference to the database
                                    session.
        habit_object (Habit):       Argument to contain the object to be
                                    modified by the user. Default set to None.
        """
        # ----------------------------------------
        # Setting up the basics for the GUI to create or change habits.
        # region ----------------------------------------

        if habit_object is None:
            self.create_new_habit_flag = True
        else:
            self.create_new_habit_flag = False
            self.habit_object = habit_object
            if self.habit_object.habit_tracking_status is True:
                self.written_tracking_status = "Completed"
            else:
                self.written_tracking_status = "To be completed"
        # Setting up the window and the needed frames as a base layout for the
        # application.
        self.create_change_root = tk.Tk()
        self.create_change_root.geometry("850x600")
        if self.create_new_habit_flag is True:
            self.create_change_root.title("Create New Habit - Habit Tracker")
        else:
            self.create_change_root.title("Change Habit - Habit Tracker")

        self.create_change_main_frame = tk.Frame(self.create_change_root)
        self.create_change_main_frame.grid(sticky="nsew")
        self.subframe_input_values = tk.Frame(self.create_change_main_frame)
        self.subframe_input_values.grid(
            row=0, column=0, padx=10, pady=10, sticky="nsew"
        )

        self.subframe_buttons = tk.Frame(self.create_change_main_frame)
        self.subframe_buttons.grid(
            row=1, column=0, padx=10, pady=10, sticky="nsew"
        )

        self.create_change_root.grid_columnconfigure(0, weight=1)
        self.create_change_main_frame.grid_columnconfigure(0, weight=1)
        self.create_change_main_frame.grid_columnconfigure(1, weight=1)

        number_of_columns_in_subframe_input_values = 5
        for i in range(number_of_columns_in_subframe_input_values):
            self.subframe_input_values.grid_columnconfigure(i, weight=1)

        if self.create_new_habit_flag is False:
            self.subframe_additional_information = tk.Frame(
                self.create_change_main_frame
            )
            self.subframe_additional_information.grid(
                row=2, column=0, padx=10, pady=10, sticky="nsew"
            )
            self.create_change_main_frame.grid_columnconfigure(2, weight=1)
            self.subframe_additional_information.grid_columnconfigure(
                0, weight=1
            )
            self.subframe_additional_information.grid_columnconfigure(
                1, weight=1
            )
            self.subframe_additional_information.grid_columnconfigure(
                2, weight=1
            )

        # endregion

        # ----------------------------------------
        # Defining the basic attributes for entry fields, buttons and methods.
        # region ----------------------------------------

        self.main_window = main_window
        self.session = session

        self.period_option_lst = ["Daily", "Every Other Day", "Weekly"]
        self.period_variable = tk.StringVar(self.create_change_root)
        if self.create_new_habit_flag:
            self.period_variable.set(self.period_option_lst[0])
        elif self.habit_object.habit_period == 1:
            self.period_variable.set(self.period_option_lst[0])
        elif self.habit_object.habit_period == 2:
            self.period_variable.set(self.period_option_lst[1])
        elif self.habit_object.habit_period == 7:
            self.period_variable.set(self.period_option_lst[2])

        self.active_checkbox_status = tk.BooleanVar(self.create_change_root)
        if self.create_new_habit_flag:
            self.active_checkbox_status.set(False)
        else:
            self.active_checkbox_status.set(
                self.habit_object.habit_active_status
            )

        # Define the basic styling for most of the widgets.
        widget_properties = {"padx": 10, "pady": 10, "sticky": "w"}
        title_properties = {"padx": 10, "pady": 10, "sticky": "e"}

        # endregion

        # ----------------------------------------
        # Creating the labels and entry fields for the input values.
        # region ----------------------------------------
        # Labels
        self.headline_label_category = tk.Label(
            self.subframe_input_values, text="Category", justify="left"
        )
        self.headline_label_enter_data = tk.Label(
            self.subframe_input_values,
            text="Enter your data here",
            justify="left"
        )
        self.headline_label_default_info = tk.Label(
            self.subframe_input_values,
            text="Information about default values",
            justify="left",
        )

        self.name_label = tk.Label(
            self.subframe_input_values, text="Habit Name", justify="left"
        )
        self.name_information_label = tk.Label(
            self.subframe_input_values,
            text="Field is requiered",
            justify="left"
        )

        self.description_label = tk.Label(
            self.subframe_input_values,
            text="Habit Description",
            justify="left"
        )
        self.description_information_label = tk.Label(
            self.subframe_input_values,
            text="Default value will be 'default'",
            justify="left",
        )

        self.period_label = tk.Label(
            self.subframe_input_values, text="Periodicity", justify="left"
        )
        self.period_information_label = tk.Label(
            self.subframe_input_values,
            text="the default value will be 'daily'",
            justify="left",
        )

        self.active_label = tk.Label(
            self.subframe_input_values,
            text="Do you want to track the habit?",
            justify="left",
        )

        # Entry fields
        self.name_entry = tk.Entry(
            self.subframe_input_values, text="Enter name"
        )
        self.description_entry = tk.Text(
            self.subframe_input_values, height=3, width=50, wrap="word"
        )
        self.period_entry = tk.OptionMenu(
            self.subframe_input_values,
            self.period_variable,
            *self.period_option_lst
        )
        self.active_entry = tk.Checkbutton(
            self.subframe_input_values, variable=self.active_checkbox_status
        )

        # endregion

        # ----------------------------------------
        # Creating the buttons to interact with the application.
        # region ----------------------------------------

        if self.create_new_habit_flag:
            self.apply_button = tk.Button(
                self.subframe_buttons, text="Apply", command=self.click_apply
            )
            self.apply_and_close_button = tk.Button(
                self.subframe_buttons,
                text="Apply and Close",
                command=self.click_apply_and_close,
            )
        else:
            self.change_and_close_button = tk.Button(
                self.subframe_buttons,
                text="Change and close",
                command=self.click_change_and_close,
            )

        self.close_button = tk.Button(
            self.subframe_buttons,
            text="Close",
            command=self.click_close_window
        )

        # endregion

        # ----------------------------------------
        # Creating the labels to show additional information when a habit is
        # modified.
        # region ----------------------------------------

        if self.create_new_habit_flag is False:
            self.tracking_status_title_lable = tk.Label(
                self.subframe_additional_information,
                text="Tracking Status",
                justify="left",
            )
            self.tracking_status_value_label = tk.Label(
                self.subframe_additional_information,
                text=self.written_tracking_status,
                justify="left",
            )

            self.creation_date_title_label = tk.Label(
                self.subframe_additional_information,
                text="Creation date",
                justify="left",
            )
            self.creation_date_value_label = tk.Label(
                self.subframe_additional_information,
                text=self.habit_object.habit_creation_date,
                justify="left",
            )

            self.start_date_title_label = tk.Label(
                self.subframe_additional_information,
                text="Start Date",
                justify="left"
            )
            self.start_date_value_label = tk.Label(
                self.subframe_additional_information,
                text=self.habit_object.habit_start_date,
                justify="left",
            )

            self.current_streak_title_label = tk.Label(
                self.subframe_additional_information,
                text="Current streak",
                justify="left",
            )
            self.current_streak_value_label = tk.Label(
                self.subframe_additional_information,
                text=self.habit_object.habit_current_streak,
                justify="left",
            )

            self.highscore_title_label = tk.Label(
                self.subframe_additional_information,
                text="Highscore",
                justify="left"
            )
            self.highscore_value_label = tk.Label(
                self.subframe_additional_information,
                text=self.habit_object.habit_highscore_streak,
                justify="left",
            )

            self.total_fails_title_label = tk.Label(
                self.subframe_additional_information,
                text="Total failures",
                justify="left",
            )
            self.total_fails_value_label = tk.Label(
                self.subframe_additional_information,
                text=self.habit_object.habit_total_fails,
                justify="left",
            )

            self.next_due_title_label = tk.Label(
                self.subframe_additional_information,
                text="Next Due Date",
                justify="left",
            )
            self.next_due_value_label = tk.Label(
                self.subframe_additional_information,
                text=self.habit_object.habit_next_due,
                justify="left",
            )

        # endregion

        # ----------------------------------------
        # Transfering the data from the existing habit to the GUI, so that the
        # values can be changed.
        # region ----------------------------------------

        if self.create_new_habit_flag is False:
            self.name_entry.insert(tk.END, self.habit_object.habit_name)
            self.description_entry.insert(
                tk.END, self.habit_object.habit_description
            )
            # active status and period are already set in the region to define
            # the variables

        # endregion

        # ----------------------------------------
        # Position the widgets in the different frames to create the layout
        # region ----------------------------------------

        entry_widgets_position = [
            (self.headline_label_category, 0, 0),
            (self.headline_label_enter_data, 0, 1),
            (self.headline_label_default_info, 0, 2),
            (self.name_label, 1, 0),
            (self.name_entry, 1, 1),
            (self.name_information_label, 1, 2),
            (self.description_label, 2, 0),
            (self.description_entry, 2, 1),
            (self.description_information_label, 2, 2),
            (self.period_label, 3, 0),
            (self.period_entry, 3, 1),
            (self.period_information_label, 3, 2),
            (self.active_label, 4, 0),
            (self.active_entry, 4, 1),
        ]
        for widget, row, column in entry_widgets_position:
            widget.grid(row=row, column=column, **widget_properties)

        if self.create_new_habit_flag:
            self.apply_button.grid(row=0, column=0, **widget_properties)
            self.apply_and_close_button.grid(
                row=0, column=1, **widget_properties
            )
            self.close_button.grid(row=0, column=2, **widget_properties)
        else:
            self.change_and_close_button.grid(
                row=0, column=0, **widget_properties
            )
            self.close_button.grid(row=0, column=1, **widget_properties)

        if self.create_new_habit_flag is False:
            additional_info_widgets_position = [
                (self.tracking_status_title_lable, 0, 0, title_properties),
                (self.tracking_status_value_label, 0, 1, widget_properties),
                (self.creation_date_title_label, 1, 0, title_properties),
                (self.creation_date_value_label, 1, 1, widget_properties),
                (self.start_date_title_label, 1, 2, title_properties),
                (self.start_date_value_label, 1, 3, widget_properties),
                (self.next_due_title_label, 1, 4, title_properties),
                (self.next_due_value_label, 1, 5, widget_properties),
                (self.current_streak_title_label, 2, 0, title_properties),
                (self.current_streak_value_label, 2, 1, widget_properties),
                (self.highscore_title_label, 2, 2, title_properties),
                (self.highscore_value_label, 2, 3, widget_properties),
                (self.total_fails_title_label, 2, 4, title_properties),
                (self.total_fails_value_label, 2, 5, widget_properties),
            ]
            for (
                widget,
                row,
                column,
                style_properties,
            ) in additional_info_widgets_position:
                widget.grid(row=row, column=column, **style_properties)

        # endregion

    # ----------------------------------------
    # Methods
    # region ----------------------------------------

    # click_apply
    def click_apply(self):
        """
        Method to create a new habit based on the data entered.

        ----- Description -----
        This method takes the input values from the entry, text etc. fields and
        transfers them to the function that adds this data to the database.
        It also refers to the main window, so that the table containg all the
        habits will be updated.
        Further it takes the return message from the adding function and
        creates an instance of the InputMessageWindow to inform the user about
        the state.
        """
        message = add_new_entry_to_db(
            session=self.session,
            name=self.name_entry.get(),
            description=self.description_entry.get("1.0", tk.END).strip(),
            period=self.convert_period_to_integer(),
            active_status=self.active_checkbox_status.get(),
        )
        self.main_window.update_data_in_table()
        if message is not None:
            InputMessageWindow(message)

    # click_close
    def click_close_window(self):
        """
        Closing the window, without saving any changes.
        """
        self.create_change_root.destroy()

    # click_apply_and_close
    def click_apply_and_close(self):
        """
        Applying the changes and closing the window.

        ----- Description -----
        Calling firstly the click_apply method and then the click_close method.
        """
        self.click_apply()
        self.click_close_window()

    # click_change_and_close
    def click_change_and_close(self):
        """
        This method is used to first apply the changes and then close the
        window.

        ----- Description -----
        The method calls the modify_existing_object_in_db function to firstly
        modify the object.
        Then it updates the table in the main window, showing all habits to the
        user.
        It also calls the InputMessageWindow to feedback the user the state.
        Lastly it uses the click_close method to close the window.
        """
        function_status_messages = modify_existing_object_in_db(
            session=self.session,
            original_object=self.habit_object,
            name=self.name_entry.get(),
            description=self.description_entry.get("1.0", tk.END).strip(),
            period=self.convert_period_to_integer(),
            active_status=self.active_checkbox_status.get(),
        )

        self.main_window.update_data_in_table()
        InputMessageWindow(function_status_messages)
        self.click_close_window()

    # convert_period_to_integer
    def convert_period_to_integer(self):
        """
        Method to convert the string from period into the needed integer.

        ----- Description -----
        The method takes the selected value from the period, which is a string
        and converts it into the needed integer.

        ----- Returns - onyl if not empty -----
        period (int):   Returns the needed integer to calculate the due dates.
        """
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

    # endregion
