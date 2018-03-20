from ItcConstrualTaskManager import *

#in this version we do an interleaved, block design.
#this means that for half of subjects, concrete comes first, while for the other half, abstract comes first.

create_two_run_itc_construal_mturk_script_set(
    range(0,10),n=36,set_label='mturk_group1a',
    mean_intertask_interval=1,
    mean_intratask_interval=0.3,
    min_intertask_interval=0.75,
    min_intratask_interval=0)
#create_practice_csv('fmri_v1')

