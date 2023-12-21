''' MODULE DESCRIPTION

will contain all functions only handling a single habit object
second and third level functions

'''

# ----------------------------------------
# Imports
# ----------------------------------------

# Standard library imports
import datetime
# Related third party imports

# Import from other modules

# ----------------------------------------
# Second level functions
# ----------------------------------------

# manage_active_passiv_status()
def manage_active_passiv_status(session, habit_object):
    '''
    
    tbd

    '''
    if habit_object.habit_active_status is True:
        set_active_habits(session=session, habit_object=habit_object)
    else:
        manage_passiv_habits(session=session, habit_object=habit_object)

# manage_passiv_habits
def manage_passiv_habits(session, habit_object):
    ''' 

    tbd
        
    '''
    reset_start_date(session, habit_object)
    reset_next_due(session, habit_object)
    reset_total_fails(session, habit_object)
    reset_current_streak(session, habit_object)
    reset_tracking_status(session, habit_object)

# ----------------------------------------
# Third level functions
# ----------------------------------------

# setup_active_habits()
def set_active_habits(session, habit_object):
    '''
    
    tbd

    '''
    if habit_object.habit_start_date is None:
        habit_object.habit_start_date = datetime.date.today()
    if habit_object.habit_next_due is None:
        habit_object.habit_next_due = habit_object.habit_start_date + datetime.timedelta(days=habit_object.habit_period)
    session.commit()

# reset_current_streak
def reset_current_streak(session, habit_object):
    habit_object.habit_current_streak = 0
    session.commit()

# reset_tracking_status
def reset_tracking_status(session, habit_object):
    habit_object.habit_tracking_status = False
    session.commit()

# reset_start_date
def reset_start_date(session, habit_object):
    habit_object.habit_start_date = None
    session.commit()

# reset_next_due
def reset_next_due(session, habit_object):
    habit_object.habit_next_due = None
    session.commit()

# reset_total_fails
def reset_total_fails(session, habit_object):
    habit_object.habit_total_fails = 0
    session.commit()