# db_setup.py
This module is only used for the general setup of the database.
It is used in the main.py to create the database section used for the application.
The created class is used as the parent class for the habit classes which are used to
handle the habits.
## Classes
### BaseClass
- used as the parent class for habit classes
- needed for SQLAlchemy

## Functions
### start_database()
- creates an engine for the database
- if needed it creates the database
- returns engine

### start_db_session(engine)
- creates a session for the database
- uses the engine of the database as input
- returns session -> used for other functions to create / change / delete database entries
