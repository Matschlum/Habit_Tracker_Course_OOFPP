''' 

tbd

'''

# Standard library imports
import datetime
# Related third party imports

# Import from other modules
from habit_classes import(
    Habit
)
from db_object_functions import(
    reset_tracking_status,
    reset_current_streak
)


# loop_for_update_due_date
def loop_for_update_due_date(session, root):
    '''

    tbd

    '''
    check_due_date(session=session)
    timer_in_milliseconds = 300000
    root.after(timer_in_milliseconds, lambda: loop_for_update_due_date(session=session, root=root))

# check_and_set_due_date
def check_due_date(session):
    '''

    tbd

    '''
    current_date = datetime.date.today()
    habit_entries = session.query(Habit).filter(Habit.habit_next_due != None).all()
    for habit_entry in habit_entries:
        if habit_entry.habit_next_due < current_date:
            print(f"for {habit_entry.habit_name} the due date passed // check_and_set_due_date / db_functions")
            check_tracking_status(session, habit_entry)          
        else:
            print(f"for {habit_entry.habit_name} all good // check_and_set_due_date / db_functions")

# check_tracking_status
def check_tracking_status(session, habit_object):
    if habit_object.habit_tracking_status is True:
        calculate_new_due_date(session, habit_object)
        reset_tracking_status(session, habit_object)
    else:
        count_fails_up(session, habit_object)
        reset_current_streak(session, habit_object)
        calculate_new_due_date(session, habit_object)

# calculate_new_due_date
def calculate_new_due_date(session, habit_object):
    '''

    tbd

    '''
    habit_object.habit_next_due = habit_object.habit_next_due + datetime.timedelta(days=habit_object.habit_period)
    session.commit()

# count_fails_up
def count_fails_up(session, habit_object):
    '''

    tbd

    '''
    habit_object.habit_total_fails = habit_object.habit_total_fails + 1
    session.commit()