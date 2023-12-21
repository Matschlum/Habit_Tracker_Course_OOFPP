''' This module contains the basic functions to setup the database

-----
Description

tbd

-----
Functions
start_db()
    checks if the database is existing and creats it if
    it is necessary.
start_db_session()
    starts the session that can be used to interact with
    the database
'''

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

# BaseClass
BaseClass = sqla_declarative_base()

# start_database()
def start_db(log=False):
    ''' Starts the database and creates one, if not existing

    -----
    Parameters
    log : boolean
        Sets the status of echo. With log = False the database
        will not dispaly all information in the command line
        (default: False)

    -----
    Return
    engine
        the connection to the database and starting point to
        start a session
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
    ''' Starts a session based on the engine

    -----
    Parameters
    engine
        Is used to establish a session to the connected database.

    -----
    Return
    session
        as connection to the session for the main module
    '''
    Session = sqla_sessionmaker(engine)
    session = Session()
    return session