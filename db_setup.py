"""
This module contains the basis for the database.

----- Description -----

This module creates the base class for the habit classes.
It further contains functions to create a database or connect to an existing
one and creates a session for it.

----- Classes - only if not empty -----
BaseClass:  Basic class from SQLAlchemy.

----- Functions -----
start_db:           Checks if the database is existing and creats it if it is
                    necessary.
start_db_session:   Starts the session that can be used to interact with the
                    database.
"""

# ----------------------------------------
# Imports
# region ----------------------------------------

# Standard library imports
import os

# Related third party imports
from sqlalchemy import create_engine as sqla_create_engine
from sqlalchemy.ext.declarative import \
    declarative_base as sqla_declarative_base
from sqlalchemy.orm import sessionmaker as sqla_sessionmaker

# Import from other modules

# endregion

# ----------------------------------------
# Classes
# region ----------------------------------------

# BaseClass
BaseClass = sqla_declarative_base()

# endregion

# ----------------------------------------
# Functions
# region ----------------------------------------


# start_database()
def start_db(log: bool = False):
    """
    Starts the database and creates one, if not existing

    ----- Arguments -----
    log (bool): Sets the status of echo. With log = False the database will not
                dispaly all information in the command line (default: False).

    ----- Returns -----
    engine (Engine):    The connection to the database and starting point to
                        start a session.
    """
    db_file = "habit_tracker.db"
    if not os.path.isfile(db_file) is None:
        engine = sqla_create_engine("sqlite:///habit_tracker.db", echo=log)
        BaseClass.metadata.create_all(bind=engine)
    else:
        engine = sqla_create_engine("sqlite:///habit_tracker.db", echo=log)

    return engine


# start_session()
def start_db_session(engine):
    """
    Starts a session based on the engine

    ----- Arguments -----
    engine (Engine): Is used to establish a session to the connected database.

    ----- Returns -----
    session (Session):  Containing the reference to the database session.
    """
    Session = sqla_sessionmaker(engine)
    session = Session()
    return session


# endregion
