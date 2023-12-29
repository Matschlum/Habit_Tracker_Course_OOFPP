'''
This module contains the basis for the database.

----------------------------------------
Description

This module creates the base class for the habit classes.
It further contains functions to create a database or connect to an existing one
and creates a session for it.

----------------------------------------
Functions

start_db
    Checks if the database is existing and creats it if it is necessary.
start_db_session
    Starts the session that can be used to interact with the database.
'''

# ----------------------------------------
# Imports
# ----------------------------------------

# Standard library imports
import os
# Related third party imports
from sqlalchemy import (
    create_engine as sqla_create_engine
)
from sqlalchemy.orm import (
   sessionmaker as sqla_sessionmaker
)
from sqlalchemy.ext.declarative import (
    declarative_base as sqla_declarative_base
)

# Import from other modules

# ----------------------------------------
# Classes
# ----------------------------------------

# BaseClass
BaseClass = sqla_declarative_base()

# ----------------------------------------
# Functions
# ----------------------------------------

# start_database()
def start_db(log=False):
    ''' 
    Starts the database and creates one, if not existing

    ----------------------------------------
    Arguments (Parameters)
    log
        Sets the status of echo. With log = False the database
        will not dispaly all information in the command line
        (default: False)

    ----------------------------------------
    Returns
    engine
        The connection to the database and starting point to
        start a session.
    '''
    db_file = "habit_tracker.db"
    if not os.path.isfile(db_file) is None:
        engine = sqla_create_engine(f"sqlite:///habit_tracker.db", echo=log)
        BaseClass.metadata.create_all(bind=engine)
    else:
        engine = sqla_create_engine(f"sqlite:///habit_tracker.db", echo=log)

    return engine

# start_session()
def start_db_session(engine):
    '''
    Starts a session based on the engine

    ----------------------------------------
    Arguments (Parameters)
    engine
        Is used to establish a session to the connected database.

    ----------------------------------------
    Returns
    session
        as connection to the session for the main module
    '''
    Session = sqla_sessionmaker(engine)
    session = Session()
    return session