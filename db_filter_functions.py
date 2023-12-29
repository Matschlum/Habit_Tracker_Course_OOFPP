'''

tbd

'''

# Standard library imports

# Related third party imports
from sqlalchemy import(
    and_ as sqla_and_
)
# Import from other modules
from habit_classes import(
    Habit
)

# filter_db
def filter_db(session, period_filter: int = None, active_filter: int =0):
    ''' Function to filter the db
    
    -----
    Description
        This function checks the parameters and loads data accordingly
        from the db.
        It returns then the information in form of a list.

    -----
    Parameters
    period_filter : int
        This parameter is used to set the filter for periodicity.
    active_filter : int
        This parameter is used to set the filter for active/passiv.

    -----
    Return
    table_content : list
        It returns the db entries that then can be displayed.

    '''

    if (period_filter == 1 or period_filter == 2 or period_filter == 7) and active_filter == 0:
        table_content = (session.query(Habit)
                         .filter(sqla_and_(Habit.habit_period == period_filter, Habit.habit_active_status == True))
                         .all())
    elif (period_filter == 1 or period_filter == 2 or period_filter == 7) and active_filter == 1:
        table_content = (session.query(Habit)
                         .filter(sqla_and_(Habit.habit_period == period_filter, Habit.habit_active_status == False))
                         .all())
    elif (period_filter == 1 or period_filter == 2 or period_filter == 7) and active_filter == 2:
        table_content = (session.query(Habit)
                         .filter(Habit.habit_period == period_filter)
                         .all())
    elif (not (period_filter == 1 or period_filter == 2 or period_filter == 7)) and active_filter == 0:
        table_content = (session.query(Habit)
                         .filter(Habit.habit_active_status == True)
                         .all())
    elif (not (period_filter == 1 or period_filter == 2 or period_filter == 7)) and active_filter == 1:
        table_content = (session.query(Habit)
                         .filter(Habit.habit_active_status == False)
                         .all())
    else:
        table_content = (session.query(Habit).all())

    return table_content

# filter_db_for_names
def filter_db_for_names(session, names):
    ''' 

    tbd

    '''
    entries = session.query(Habit).filter(Habit.habit_name.in_(names)).all()
    return entries