# Error Codes
## add_new_entry_to_db  
0:     habit successfully added to the database  
### WARNINING:  
100:   name is not of type str, it will converted into a str  
101:   description os not of type str, it will converted into a str  
  
### ERROR:
1:     habit with this name is already existing  
112:   active_status is not of type boolean  
113:   period is not of type int  
114:   name is None or ""  


## add_standard_habits_to_db
### ERROR:
120:   not all values in standard_period are of type integers
121:   not all values in standard_active_status are of type boolean
122:   not all lists (standard_name, standard_period, standard_active_status and standard_description) have the same length

## manage_tracking_status
### ERROR:
200:   habit_tracking_status cannot be changed - habit marked as inactive
