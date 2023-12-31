'''
        self.habit_name = habit_name
        self.habit_description = habit_description
        self.habit_period = habit_period
        self.habit_active_status = habit_active_status

        self.habit_tracking_status = False
        self.habit_creation_date = datetime.datetime.now()
        self.habit_start_date = None
        self.habit_current_streak = 0
        self.habit_highscore_streak = 0
        self.habit_total_fails = 0
        self.habit_next_due = None
'''
# ----------------------------------------
# Imports
# region ----------------------------------------

# Standard library imports
import tkinter as tk
# Related third party imports

# Import from other modules
from db_functions import (
    add_new_entry_to_db,
    modify_existing_object_in_db
)
from pop_up_windows import (
    InputMessageWindow
)

# endregion

# Class CreateChangeHabitWindow
class CreateChangeHabitWindow():
    '''
    
    tbd
    
    '''

    def __init__(self, main_window, session, habit_object=None):
        '''

        tbd

        '''

        # Create a flag to distinguish between create and change
        if habit_object is None:
            self.create_new_habit_flag = True
        else:
            self.habit_object = habit_object
            self.create_new_habit_flag = False
            self.existing_habit_name = habit_object.habit_name
            self.existing_habit_description = habit_object.habit_description
            self.existing_habit_period = habit_object.habit_period
            self.existing_habit_active_status = habit_object.habit_active_status

            if habit_object.habit_tracking_status is True:
                self.existing_habit_tracking_status = "Completed"
            else:
                self.existing_habit_tracking_status = "To be completed"

            self.existing_habit_creation_date = habit_object.habit_creation_date
            self.existing_habit_start_date = habit_object.habit_start_date
            self.existing_habit_current_streak = habit_object.habit_current_streak
            self.existing_habit_highscore_streak = habit_object.habit_highscore_streak
            self.existing_habit_total_fails = habit_object.habit_total_fails
            self.existing_habit_next_due = habit_object.habit_next_due

        # ----------------------------------------
        # General setup for CreateChangeHabitWindow class
        # region ----------------------------------------
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
            row=0, column=0,
            padx=10, pady=10,
            sticky="nsew"
        )
        
        self.subframe_buttons = tk.Frame(self.create_change_main_frame)
        self.subframe_buttons.grid(
            row=1, column=0,
            padx=10, pady=10,
            sticky="nsew"
        )

        self.create_change_root.grid_columnconfigure(0, weight=1)
        self.create_change_main_frame.grid_columnconfigure(0, weight=1)
        self.create_change_main_frame.grid_columnconfigure(1, weight=1)
        self.subframe_input_values.grid_columnconfigure(0, weight=1)
        self.subframe_input_values.grid_columnconfigure(1, weight=1)
        self.subframe_input_values.grid_columnconfigure(2, weight=1)
        self.subframe_input_values.grid_columnconfigure(3, weight=1)
        self.subframe_input_values.grid_columnconfigure(4, weight=1)

        if self.create_new_habit_flag is False:
            self.subframe_additional_information = tk.Frame(self.create_change_main_frame)
            self.subframe_additional_information.grid(
                row=2, column=0,
                padx=10, pady=10,
                sticky="nsew"
            )
            self.create_change_main_frame.grid_columnconfigure(2, weight=1)
            self.subframe_additional_information.grid_columnconfigure(0, weight=1)
            self.subframe_additional_information.grid_columnconfigure(1, weight=1)
            self.subframe_additional_information.grid_columnconfigure(2, weight=1)
        # endregion

        # ----------------------------------------
        # Defining the basic variables for the class
        # region ----------------------------------------
        self.main_window = main_window
        self.session = session
        
        self.period_option_lst = [
            "Daily",
            "Every Other Day",
            "Weekly"
        ]
        self.period_variable = tk.StringVar(
            self.create_change_root
        )
        if self.create_new_habit_flag:
            self.period_variable.set(
                self.period_option_lst[0]
            )
        elif self.existing_habit_period == 1:
            self.period_variable.set(
                self.period_option_lst[0]
            )
        elif self.existing_habit_period == 2:
            self.period_variable.set(
                self.period_option_lst[1]
            )
        elif self.existing_habit_period == 7:
            self.period_variable.set(
                self.period_option_lst[2]
            )

        self.active_checkbox_status = tk.BooleanVar(
            self.create_change_root
        )
        if self.create_new_habit_flag:
            self.active_checkbox_status.set(False)
        else:
            self.active_checkbox_status.set(self.existing_habit_active_status)

        widget_properties = {"padx": 10, "pady": 10, "sticky": "w"}
        title_properties = {"padx": 10, "pady": 10, "sticky": "e"}
        # endregion

        # ----------------------------------------
        # Creating the labels and entry fields for the subframe_input_values
        # region ----------------------------------------

        self.headline_label_category = tk.Label(
            self.subframe_input_values,
            text="Category",
            justify="left"
        )
        self.headline_label_enter_data = tk.Label(
            self.subframe_input_values,
            text="Enter your data here",
            justify="left"
        )
        self.headline_label_default_info = tk.Label(
            self.subframe_input_values,
            text="Information about default values",
            justify="left"
        )

        self.name_label = tk.Label(
            self.subframe_input_values,
            text="Habit Name",
            justify="left"
        )
        self.name_entry = tk.Entry(
            self.subframe_input_values,
            text="Enter name"
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
        self.description_entry = tk.Text(
            self.subframe_input_values,
            height=3,
            width=50,
            wrap="word"
        )
        self.description_information_label = tk.Label(
            self.subframe_input_values,
            text="Default value will be 'default'",
            justify="left"
        )

        self.period_label = tk.Label(
            self.subframe_input_values,
            text="Periodicity",
            justify="left"
        )
        self.period_entry = tk.OptionMenu(
            self.subframe_input_values,
            self.period_variable,
            *self.period_option_lst
        )
        self.period_information_label = tk.Label(
            self.subframe_input_values,
            text="the default value will be 'daily'",
            justify="left"
        )

        self.active_label = tk.Label(
            self.subframe_input_values,
            text="Do you want to track the habit?",
            justify="left"
        )
        self.active_entry = tk.Checkbutton(
            self.subframe_input_values,
            variable=self.active_checkbox_status
        )
        # endregion

        # ----------------------------------------
        # Creating the buttons for the subframe_buttons
        # region ----------------------------------------

        if self.create_new_habit_flag:
            self.apply_button = tk.Button(
                self.subframe_buttons,
                text="Apply",
                command=self.click_apply
            )
            self.apply_and_close_button = tk.Button(
                self.subframe_buttons,
                text="Apply and Close",
                command=self.click_apply_and_close
            )
        else:
            self.change_and_close_button = tk.Button(
                self.subframe_buttons,
                text="Change and close",
                command=self.click_change_and_close
            )

        self.close_button = tk.Button(
            self.subframe_buttons,
            text="Close",
            command=self.click_close
        )

        # endregion

        # ----------------------------------------
        # Creating the labels for the subframe_additional_information
        # region ----------------------------------------
        if self.create_new_habit_flag is False:
            self.tracking_status_title_lable = tk.Label(
                self.subframe_additional_information,
                text="Tracking Status",
                justify="left"
            )
            self.tracking_status_value_label = tk.Label(
                self.subframe_additional_information,
                text=self.existing_habit_tracking_status,
                justify="left"
            )
        
            self.creation_date_title_label = tk.Label(
                self.subframe_additional_information,
                text="Creation date",
                justify="left"
            )
            self.creation_date_value_label = tk.Label(
                self.subframe_additional_information,
                text=self.existing_habit_creation_date,
                justify="left"
            )

            self.start_date_title_label = tk.Label(
                self.subframe_additional_information,
                text="Start Date",
                justify="left"
            )
            self.start_date_value_label = tk.Label(
                self.subframe_additional_information,
                text=self.existing_habit_start_date,
                justify="left"
            )

            self.current_streak_title_label = tk.Label(
                self.subframe_additional_information,
                text="Current streak",
                justify="left"
            )
            self.current_streak_value_label = tk.Label(
                self.subframe_additional_information,
                text=self.existing_habit_current_streak,
                justify="left"
            )
        
            self.highscore_title_label = tk.Label(
                self.subframe_additional_information,
                text="Highscore",
                justify="left"
            )
            self.highscore_value_label = tk.Label(
                self.subframe_additional_information,
                text=self.existing_habit_highscore_streak,
                justify="left"
            )

            self.total_fails_title_label = tk.Label(
                self.subframe_additional_information,
                text="Total failures",
                justify="left"
            )
            self.total_fails_value_label = tk.Label(
                self.subframe_additional_information,
                text=self.existing_habit_total_fails,
                justify="left"
            )

            self.next_due_title_label = tk.Label(
                self.subframe_additional_information,
                text="Next Due Date",
                justify="left"
            )
            self.next_due_value_label = tk.Label(
                self.subframe_additional_information,
                text=self.existing_habit_next_due,
                justify="left"
            )
        # endregion

        # ----------------------------------------
        # Fill in the values for changing habits
        # region ----------------------------------------
        if self.create_new_habit_flag is False:
            self.name_entry.insert(tk.END, self.existing_habit_name)
            self.description_entry.insert(tk.END, self.existing_habit_description)
            # active status and period are already set in the region to define the variables
        # endregion

        # ----------------------------------------
        # Position the widgets in the frames to create the layout
        # region ----------------------------------------

        self.headline_label_category.grid(
            row=0, column=0,
            **widget_properties
        )
        self.headline_label_enter_data.grid(
            row=0, column=1,
            **widget_properties
        )
        self.headline_label_default_info.grid(
            row=0, column=2,
            **widget_properties
        )

        self.name_label.grid(
            row=1, column=0,
            **widget_properties
            )
        self.name_entry.grid(
            row=1, column=1,
            **widget_properties
        )
        self.name_information_label.grid(
            row=1, column=2,
            **widget_properties
        )

        self.description_label.grid(
            row=2, column=0,
            **widget_properties
        )
        self.description_entry.grid(
            row=2, column=1,
            **widget_properties
        )
        self.description_information_label.grid(
            row=2, column=2,
            **widget_properties
        )

        self.period_label.grid(
            row=3, column=0,
            **widget_properties
        )
        self.period_entry.grid(
            row=3, column=1,
            sticky="e"
        )
        self.period_information_label.grid(
            row=3, column=2,
            **widget_properties
        )

        self.active_label.grid(
            row=4, column=0,
            **widget_properties
        )
        self.active_entry.grid(
            row=4, column=1
        )

        if self.create_new_habit_flag:
            self.apply_button.grid(
                row=0, column=0,
                **widget_properties
            )
            self.apply_and_close_button.grid(
                row=0, column=1,
                **widget_properties
            )
            self.close_button.grid(
                row=0, column=2,
                **widget_properties
            )
        else:
            self.change_and_close_button.grid(
                row=0, column=0,
                **widget_properties
            )
            self.close_button.grid(
                row=0, column=1,
                **widget_properties
            )

        if self.create_new_habit_flag is False:
            self.tracking_status_title_lable.grid(
                row=0, column=0,
                **title_properties
            )
            self.tracking_status_value_label.grid(
                row=0, column=1,
                **widget_properties
            )

            self.creation_date_title_label.grid(
                row=1, column=0,
                **title_properties
            )
            self.creation_date_value_label.grid(
                row=1, column=1,
                **widget_properties
            )
            self.start_date_title_label.grid(
                row=1, column=2,
                **title_properties
            )
            self.start_date_value_label.grid(
                row=1, column=3,
                **widget_properties
            )
            self.next_due_title_label.grid(
                row=1, column=4,
                **title_properties
            )
            self.next_due_value_label.grid(
                row=1, column=5,
                **widget_properties
            )
        
            self.current_streak_title_label.grid(
                row=2, column=0,
                **title_properties
            )
            self.current_streak_value_label.grid(
                row=2, column=1,
                **widget_properties
            )
            self.highscore_title_label.grid(
                row=2, column=2,
                **title_properties
            )
            self.highscore_value_label.grid(
                row=2, column=3,
                **widget_properties
            )
            self.total_fails_title_label.grid(
                row=2, column=4,
                **title_properties
            )
            self.total_fails_value_label.grid(
                row=2, column=5,
                **widget_properties
            )
        # endregion

    # ----------------------------------------
    # Methods
    # region ----------------------------------------
    # click_apply
    def click_apply(self):
        '''     

        tbd

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

    # click_apply_and_close
    def click_apply_and_close(self):
        ''' 

        tbd

        '''
        self.click_apply()
        self.click_close()

    # click_close
    def click_close(self):
        ''' 
       
        tbd

        '''
        self.create_change_root.destroy()


    # click_change_and_close
    def click_change_and_close(self):
        function_status_messages = modify_existing_object_in_db(
            session=self.session,
            original_object=self.habit_object,
            name=self.name_entry.get(),
            description=self.description_entry.get("1.0", tk.END).strip(),
            period=self.convert_period_to_integer(),
            active_status=self.active_checkbox_status.get()       
        )

        self.main_window.update_data_in_table()
        InputMessageWindow(function_status_messages)
        self.click_close()

    # convert_period_to_integer
    def convert_period_to_integer(self):
        ''' 
        
        tbd

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

    # endregion
