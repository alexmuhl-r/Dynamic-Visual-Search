# Dynamic Visual Search
Dynamic visual search tasks in Python and SR Research's Experiment Builder by Alex Muhl-Richardson and Hayward Godwin

## Branch Specific Task Parameters

When the task is started it will ask for a number of parameters:

1. 'PPT ID' - this is a participant ID number which also determines the target colour and number selection. Even participant numbers are assigned one target colour and a target number. Odd participant numbers are assigned a different target colour and a target number. There are two possible target colours and target numbers rotate between all 10 digits. 

2. 'Condition' - this determines the target prevalence, as this task variant does not support varied target prevalence levels, this should always be set to 1.

3. 'Condition 2' - this determines whether the displays contain numbers and colours ('MN'), only colours ('M') or only numbers ('N').

4. 'Layout' - this determines the spatial configuration of the display, centred ('0 - C'), numbers right and colours left ('1 - NR ML'), numbers left and colours right ('2 - NL MR'), numbers and colours left ('3 - NM Left'), numbers and colours right ('4 - NM Right').

5. 'Targets' - this determines the target/practice settings. If 'p' is pressed here a three trial practice block will run. Other legacy multiple target functionality (beyond the digit/colour combinations specific to this variant) is not supported and, if practice is not being used, '0' should always be pressed here.
