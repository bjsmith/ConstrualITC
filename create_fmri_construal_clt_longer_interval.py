from ItcConstrualTaskManager import *


#trial length=
#ITIfix+construal_trail+rTaskInterval+trial
#maximum possible=
#ntrial*(2+4+1+6)=ntrial*12
#therefore 20 trials is maximum length of 240 seconds
#36 trials is 7.2 minutes. We could do that. Could even do 9.6 minutes

create_two_independent_runs_itc_construal_script_set(
    range(2000,2030),3,2,n=40,set_label='fmri_v1',practice_as_separate_run=True,
    )
#create_practice_csv('fmri_v1')

