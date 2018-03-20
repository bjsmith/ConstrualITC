from ItcConstrualTaskManager import *


#trial length=
#ITIfix+construal_trail+rTaskInterval+trial
#maximum possible=
#ntrial*(2+4+1+6)=ntrial*12
#therefore 20 trials is maximum length of 240 seconds
#36 trials is 7.2 minutes. We could do that. Could even do 9.6 minutes
create_conditions_in_separate_folders('test1',variableamount_interval=[20,40],fixedamount_values=[25,30])