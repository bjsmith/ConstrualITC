from ItcConstrualTask import *
from pandas import *
#
citc_task = ItcConstrualTask(n=72, subid=201, day=1, runid=1)
citc_task.populate_construal_itc_task_with_parameters()

citc_task.task_data['LeftColor'] = '[220 100 100]'
citc_task.task_data['RightColor'] = '[100 100 220]'
citc_task.task_data[citc.task_data['SSonLorR']==2,'LeftColor']='[100 100 220]'
citc_task.task_data[citc.task_data['SSonLorR']==2,'RightColor']='[220 100 100]'

# citc_task.populate_itc_task_with_parameters()
# # we have three sessions of two runs of ITC
# # every subject consistently has the same salience condition first
# # we'll make each subject also consistently have the same construal ITC task first.
# # but we'll counterbalance construal task and salience condition
#
# construal_stim = pandas.read_csv('spunt_dataset/stim.csv')
# construal_data = pandas.read_csv('spunt_dataset/data.csv')
# construal_seeker = pandas.read_csv('spunt_dataset/seeker.csv')
#
# #    %% SEEKER column key %%
# #    % 1 - trial #
# #    % 2 - cond (1=1to2, 2=2to3, 3=3to4, 4=2to1, 5=3to2, 6=4to3)
# #    % 3 - correct (normative) response (1=Yes, 2=No)
# #    % 5 - scheduled question onset
# #    % 6 - (added above) scheduled action onset
# #    % 7 - (added below) actual question onset (s)
# #    % 8 - (added below) actual action onset (s)
# #    % 9 - (added below) actual response [0 if NR]
# #    % 10 - (added below) response time (s) [0 if NR]
#
#
# construal_data['StimulusId'] = range(1, 145)
# construal_stim['StimulusId'] = range(1, 145)
# # so we want to use the stimulus column in Seeker to index stimulus and data
# # do we need other stuff from seekers?
# # we want cond,correct, so yes.
# construal_all_trials = construal_seeker. \
#     merge(construal_stim, how='left', left_on='Stimulus', right_on='StimulusId'). \
#     merge(construal_data, how='left', left_on='Stimulus', right_on='StimulusId')
#
# construal_all_trials = \
#     pandas.concat([
#         construal_all_trials,
#         pandas.DataFrame(construal_all_trials.q_and_a.str.split('?', 1).tolist(),
#                          columns=['Question', 'Answer'])
#     ], axis=1)
# # great, we've concatenated them. now
#
# construal_all_trials['Question'] = construal_all_trials['Question'] + '?'
# #    % 4 - stimulus # (corresponds to row in stim & data, see above)
# # we only want the first condition for now - that's the first 72
#
#
#
#
# construal_all_trials = construal_all_trials.rename(columns={'Condition_x': 'Condition'})
#
# #print construal_all_trials.index.values
# #print citc_task.construal_condition
# if citc_task.construal_condition==0:
#     construal_run=construal_all_trials.loc[:, ['TrialN', 'Question', 'Answer', 'Stimulus', 'Condition']].iloc[
#                 0:72]
# elif citc_task.construal_condition==1:
#     construal_run=construal_all_trials.loc[:, ['TrialN', 'Question', 'Answer', 'Stimulus', 'Condition']].iloc[
#     72:144]
#
# #construal_run=construal_run.reindex(range(0,72))
#
# construal_run = construal_run.rename(columns={c: ('Construal_' + c) for c in construal_run.columns})
#
# construal_run.reset_index(drop=True,inplace=True)
# #print citc_task.task_data.index.values
# #print construal_run.index.values
# citc_task.task_data = pandas.concat([citc_task.task_data, construal_run], axis=1)
# #citc_task.task_data.combine_first(construal_run)
# #print citc_task.task_data
