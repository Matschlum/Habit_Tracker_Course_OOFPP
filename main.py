''' Starts the habit tracker application

-----
Description

tbd

-----
Note
For developing purposes there is a section below the main window,
called CHECK. This is used during the developing to test and show
data in the command line. It has no other influence to the module.
'''

# Standard library imports

# Related third party imports

# Import from other modules
from db_setup import (
    start_db,
    start_db_session
)

if __name__ == "__main__":
    # DB setup
    engine = start_db(log=False)
    session = start_db_session(engine)

