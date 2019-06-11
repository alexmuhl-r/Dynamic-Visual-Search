# Dynamic Visual Search
Dynamic visual search tasks in Python and SR Research's Experiment Builder by Alex Muhl-Richardson and Hayward Godwin

## Branch Specific Task Parameters

When the task is started it will ask for a number of parameters:

1. 'PPT ID' - this is a participant ID number which also determines the target colour selection. Each participant number starting at 0 and going up to 15 (looping round from 16 and up, etc.) will have a different one of the 16 colours within the colour scale as their target colour.

2. 'Condition' - this determines the target prevalence, this should be set to 0 for the low prevalence condition or 1 for the high prevalence condition.

3. 'Targets' - this determines the target/practice settings. If 'p' is pressed here a three trial practice block will run. This task variant does not support multiple targets, so if practice is not being used, '0' should always be pressed here.
