###BEGIN EXPERIMENT
from itclogic import *
SALIENCE_CONDITION_AMOUNT=0
SALIENCE_CONDITION_DELAY=1
salience_condition=choose_condition(expInfo['participant'] ,expInfo['run_id'],expInfo['day'])
itc_feedback_duration=0.5

if salience_condition==SALIENCE_CONDITION_AMOUNT:
    amount_LL_array=setup_randomly_ordered_amounts_from_range(20,40,expInfo['nTrials'],salience_condition)
elif salience_condition==SALIENCE_CONDITION_DELAY:
    delay__LL_array=setup_randomly_ordered_amounts_from_range(2,20,expInfo['nTrials'],salience_condition)

k_M=float(expInfo['kval'])

#####BEGIN ROUTINE

feedback_began=False

testtextvar="this is set by a var!"
response_timer=None
next_ct_printout=1.5
debugger.text=str("k_M:"+str(k_M))

#set up the responses 

def begin_feedback(feedback_obj):
    global response_timer
    global feedback_began
    feedback_began=True
    response_timer = core.CountdownTimer(itc_feedback_duration)
    feedback_obj.setAutoDraw(True)
    feedback_obj.status= STARTED
    
    
#### EACH FRAME
#ALRIGHT. WE HAVE TO INSERT THIS INTO THE RIGHT PLACE IN THE JS
#AND WE WILL NEED TO INSERT THAT MISC JS FIX EVERY TIME WE COMPILE!
#DISAPPOINTING BUT WE'LL HAVE TO DO THAT TO MOVE THROUGH.
if resp.status == STARTED:
    if len(theseKeys)>0:
        firstResp=theseKeys[0]
        if 'left' in theseKeys:
            fb_obj=left_feedback
        elif 'right' in theseKeys:
            fb_obj=right_feedback
        else:
            raise Exception("Unhandled response key: " + str(theseKeys))
        
        if feedback_began==False: #execute on the first frame after a response.
            begin_feedback(fb_obj)
            resp.status == FINISHED

elif resp.status==FINISHED and feedback_began==False:
    #second trigger for ending trial; response time is ended.
    begin_feedback(no_response)
    #

#execute on first frame after feedback begins
if response_timer is not None:
    #print out the time left but only on multiples of 0.1
    if response_timer.getTime()<next_ct_printout:
        next_ct_printout=next_ct_printout-0.1
        debugger.text=str(round(response_timer.getTime(),1))

    if response_timer.getTime()<0:
        break #force end of routine.
        
        
        
#END ROUTINE
#calculate k value

k_M_new=k_M
firstResp