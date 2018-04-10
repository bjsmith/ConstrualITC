from ItcConstrualTaskManager import *


#trial length=
#ITIfix+construal_trail+rTaskInterval+trial
#maximum possible=
#ntrial*(2+4+1+6)=ntrial*12
#therefore 20 trials is maximum length of 240 seconds
#36 trials is 7.2 minutes. We could do that. Could even do 9.6 minutes

create_two_independent_runs_itc_construal_script_set(
    range(2000,2200),3,2,n=60,set_label='fmri_v3',practice_as_separate_run=True,
    mean_intertask_interval=2,
    mean_intratask_interval=2,
    min_intertask_interval=1,
    min_intratask_interval=1,
    require_balance_from_trial=[24,30,36,42,48,54,60])#[30,42,54,60])
#create_practice_csv('fmri_v1')

