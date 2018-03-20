expInfo={'nTrials':20}
from IntertemporalChoiceTask import *
salience_condition=0
n_trials=expInfo['nTrials']
itc_task=IntertemporalChoiceTask(n=n_trials,subid=201,day=2,runid=3,salience_condition=salience_condition)
itc_task.setup_screen_sides()
itc_task.setup_iti()
#now depending on the condition, set the amounts and delays.

if salience_condition==SALIENCE_CONDITION_AMOUNT:
    amount_LL_array=setup_randomly_ordered_amounts_from_range(20,40,n_trials,salience_condition)
    itc_task.task_data['LLamount']=pandas.Series(amount_LL_array)
    #itc_data['SSamount']=
    itc_task.task_data['SSdelay']=pandas.Series([5]*n_trials)
    itc_task.task_data['LLdelay'] = pandas.Series([90] * n_trials)
elif salience_condition==SALIENCE_CONDITION_DELAY:
    delay_LL_array=setup_randomly_ordered_amounts_from_range(1,9,n_trials,salience_condition)
    itc_task.task_data['LLdelay'] = pandas.Series(delay_LL_array)
    # itc_data['SSamount']=
    itc_task.task_data['SSamount'] = pandas.Series([25] * n_trials)
    itc_task.task_data['LLamount'] = pandas.Series([30] * n_trials)

#print(itc_data)

#print(amount_LL_array)

itc_task.task_data.loc[2,'LLdelay']=50000

print itc_task.task_data.loc[0:5,'LLdelay']
itc_task.update_trial(4,"l",2.4,0.002,0.003,3,2.2532,4.2524235,4.2524235+1,0,1,ss_amount=5)
itc_task.update_trial(5,"l",2.4,0.002,0.003,3,2.2532,4.2524235,4.2524235+1,0,1,ll_delay=18)


print(itc_task.task_data)