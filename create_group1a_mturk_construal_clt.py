from ItcConstrualTaskManager import *


#trial length=
#ITIfix+construal_trail+rTaskInterval+trial
#maximum possible=
#ntrial*(1+4+0.3+6)=ntrial*11.3s
#we can have up to 74 trials to fit within 14 minutes.
#that would be...36 ish trials per condition!
#but let's say participants actually take one less second than allotted for the delayed task; 0.3 less seconds for construal task.
#then we have
#ntrial*(1+4-0.3+0.3+5)=ntrial*10 s
#That gives us 84 trials per condition; cut in half, that's 42 trials.
#So that's our absolute maximum, considering that we need to fit practice in the front

#raise Exception("One side looks beautiful; but the SS/LL on fixed-value trials appears not to be population properly")
#raise Exception("Additionally, it appears that the trial type is not properly alternating by run. Fix this.")
#create_two_run_itc_construal_mturk_script_set(
# create_itc_construal_mturk_script_set_interleaveddesign(
#     range(0,10),n=12,set_label='mturk_group1a',
#     mean_intertask_interval=1,
#     mean_intratask_interval=0.3,
#     min_intertask_interval=0.75,
#     min_intratask_interval=0)
#create_practice_csv('fmri_v1')

create_itc_construal_mturk_script_set(
    range(0,4),n=12,set_label='mturk_test',
    mean_intertask_interval=1,
    mean_intratask_interval=0.3,
    min_intertask_interval=0.75,
    min_intratask_interval=0,
    )

