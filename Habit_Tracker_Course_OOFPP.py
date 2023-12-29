'''
Missing:
- History does not show history class all entries
- Change habit does not open window

Go on commenting the db_objects_functions
-------------------------------------------------------------------------------------------
When to create a habit_history entry:

1. when task is marked as completed -> exact in this moment, not when the status is set back
2. when due date passed without tracking_status = True -> can be found in the update_loop

-> double check

Think about what happens with history entries, when habits are changed?
... habits are deleted?

Currently habit history only tracks the completion or the failure of a habit, so it is not really a log.
In the concept paper it was only mentioned as above. Not a real log file.
Makes things easier. According to this plan:

--> instance of the habit history class created in
set_tracking_status_to_true in db_object_functions -> ensures a new object when switching the status
check_tracking_status in update_loop in the else-part, not in the if part!!!!

Both will call a function that gets the information of the habit object and creates a related history entry.

When set from active to passiv: Nothing will happen -> describe in the readme.md how to add the deletion and add the call for this function into the corresponding function as a comment
manage_passiv_habits in db_object_functions

When calling the delete_entry functions use the for loop to delete all corresponding entries in the history.

'''