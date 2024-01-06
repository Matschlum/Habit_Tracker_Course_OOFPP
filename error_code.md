# Error Codes
## Successfull
0:		Habit Successfully added to the database  
301:	Name of habit changed  
302:	Description of habit changed  
303:	Periodicity of habit changed  
304:	Status for active of habit changed  
## WARNINGS
100:	WARNING: Name was converted to a string  
101:	WARNING: Description was converted to a string  
201:	WARNING: Habit already markes as complete for this due date  
401:	WARNING: No name changed  
402:	WARNING: No description changed  
403:	WARNING: No periodicity changed  
404:	WARNING: No status for active chagned  
411:	WARNING: Description is None. Set to default  
412:	WARNING: Periodicity is None or empty. Set to default 1  
413:	WARNING: Active Status is None or empty. Set to default False  
## ERROR
1:		ERROR: Habit with this name already existing  
112:	ERROR: Status for active was not of type boolean. No data added  
113:	ERROR: Periodicity was not of type integer. No data added  
114:	ERROR: Name cannot be None or empty  
120:	ERROR: Standard Periodicty does not only contain integers  
121:	ERROR: Standard status for active does not only contain boolean  
122:	ERROR: Standad lists have different length  
123:	ERROR: Not all inputs are lists  
200:	ERROR: Habit tracking status cannot be changed, habit marked as inactive  