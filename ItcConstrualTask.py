from IntertemporalChoiceTask import *
from pandas import *
import math
import warnings
import random
from enum import *

class ItcConstrualMeanRule:
    fMRILegacyMethod, StdDevMethod = range(2)

# a python class to read in Bob Spunt's 2016 construal task and insert it into James Melrose's ITC
class ItcConstrualTask(IntertemporalChoiceTask):
    def __init__(self, n, subid, day, runid, salience_condition=None, construal_condition=None, task_version='generic',
                 mean_intertask_interval=2,
                 mean_intratask_interval=1,
                 min_intertask_interval=0.5,
                 min_intratask_interval=0.5,
                 require_balance_from_trial=None,
                 construal_mean_rule=ItcConstrualMeanRule.fMRILegacyMethod
                 ):
        IntertemporalChoiceTask.__init__(self, n=n, subid=subid, day=day,
                                         runid=runid, salience_condition=salience_condition,
                                         task_version=task_version,
                                         mean_intertask_interval=mean_intertask_interval,
                                         mean_intratask_interval=mean_intratask_interval,
                                         min_intertask_interval=min_intertask_interval,
                                         min_intratask_interval=min_intratask_interval,
                                         require_balance_from_trial=require_balance_from_trial
                                         )
        if construal_condition is None:
            # raise Exception("need to insert code here for selecting a salience condition based on other data")
            # we set construal condition in this way to balance it with salience_condition
            # this way, precisely half of subjects in each salience condition will be in each construal condition
            self.construal_condition = int((math.floor(subid / 2) + runid) % 2)



    def populate_construal_itc_task_with_parameters(self, construal_set_ids):
        self.populate_itc_task_with_parameters()
        # we have three sessions of two runs of ITC
        # every subject consistently has the same salience condition first
        # we'll make each subject also consistently have the same construal ITC task first.
        # but we'll counterbalance construal task and salience condition

        construal_stim = pandas.read_csv('spunt_dataset/stim.csv')
        construal_data = pandas.read_csv('spunt_dataset/data.csv')
        construal_seeker = pandas.read_csv('spunt_dataset/seeker.csv')

        #    %% SEEKER column key %%
        #    % 1 - trial #
        #    % 2 - cond (1=1to2, 2=2to3, 3=3to4, 4=2to1, 5=3to2, 6=4to3)
        #    % 3 - correct (normative) response (1=Yes, 2=No)
        #    % 5 - scheduled question onset
        #    % 6 - (added above) scheduled action onset
        #    % 7 - (added below) actual question onset (s)
        #    % 8 - (added below) actual action onset (s)
        #    % 9 - (added below) actual response [0 if NR]
        #    % 10 - (added below) response time (s) [0 if NR]


        construal_data['StimulusId'] = range(0, 144)
        construal_stim['StimulusId'] = range(0, 144)
        # so we want to use the stimulus column in Seeker to index stimulus and data
        # do we need other stuff from seekers?
        # we want cond,correct, so yes.

        # this was used before I wrote my own code to select construal trials.
        # construal_all_trials = construal_seeker. \
        #    merge(construal_stim, how='left', left_on='Stimulus', right_on='StimulusId'). \
        #    merge(construal_data, how='left', left_on='Stimulus', right_on='StimulusId')
        construal_all_trials = construal_stim.merge(construal_data, how='left', on='StimulusId')

        construal_all_trials = \
            pandas.concat([
                construal_all_trials,
                pandas.DataFrame(construal_all_trials.q_and_a.str.split('?', 1).tolist(),
                                 columns=['QuestionText', 'AnswerText'])
            ], axis=1)
        # great, we've concatenated them. now

        construal_all_trials['QuestionText'] = construal_all_trials['QuestionText'] + '?'
        #    % 4 - stimulus # (corresponds to row in stim & data, see above)
        # we only want the first condition for now - that's the first 72




        construal_all_trials = construal_all_trials.rename(columns={'Condition_x': 'Condition'})

        # this iterates through all of the construal stimuli to get sets that are each individually
        # well-distributed on important dimensions
        # this has to be consistent across runs, because it generates values for both runs.
        # if we don't make it consistent then we'd risk assigning the same values to both runs.
        # if pre_loaded_construal_set is None:
        #     random.seed(self.get_pseudorandom_seed('BalancedConstrualSet',consistent_across_runs=True))
        #     balanced_construal_sets=self.get_balanced_construal_set(n_trials=self.n_trials,n_runs=n_runs_total)
        # else
        #     balanced_construal_sets=pre_loaded_construal_set


        # this is inefficient; it essentially generates the same set repeatedly. That's OK though,
        # the finding the set itself is fairly fast.
        # construal_run = construal_all_trials.loc[:, ['QuestionText', 'AnswerText', 'Condition']].iloc[
        #    balanced_construal_sets[0]]
        # elif self.construal_condition == 1:
        construal_run = construal_all_trials.loc[:, ['QuestionText', 'AnswerText', 'Condition']].iloc[
            construal_set_ids]

        # construal_run=construal_run.reindex(range(0,72))

        construal_run = construal_run.rename(columns={c: ('Construal_' + c) for c in construal_run.columns})

        construal_run.reset_index(drop=True, inplace=True)
        # print citc_task.task_data.index.values
        # print construal_run.index.values


        if (self.task_arrangement==ItcTaskArrangement.TasksBlocked and
                (self.condition_design == ItcConstrualConditionDesign.BlockDesignAbstractFirst or
                         self.condition_design == ItcConstrualConditionDesign.BlockDesignConcreteFirst)):
            # we concatenate differently if this is block design because we actually want construal runs to come BEFORE task_data
            construal_run['ITI']=self.task_data['ITI']
            self.task_data['ITI'] = None
            self.task_data = pandas.concat([construal_run, self.task_data], axis=0)
        else:

            self.task_data = pandas.concat([self.task_data, construal_run], axis=1)



        if self.task_arrangement==ItcTaskArrangement.TasksBlocked and self.condition_design==ItcConstrualConditionDesign.RandomCounterbalanced:
            citc_task_one_per_row = self.task_data[["Subject", "salienceCondition", "day", "runid"]]
            to_doubleup = self.task_data[
                [c for c in self.task_data.columns if c not in ["Subject", "salienceCondition", "day", "runid"]]]
            #to_doubleup_1 = to_doubleup.copy(deep=True)
            #to_doubleup_2 = to_doubleup.copy(deep=True)
            to_doubleup_1 = to_doubleup[0::2].rename(columns=dict([(c, c + "1") for c in to_doubleup.columns]))
            #to_doubleup_1 = to_doubleup_1.rename(index=str, columns=dict([(c, c + "1") for c in to_doubleup_1.columns]))
            # to_doubleup_1 = to_doubleup_1.rename(str,
            #                                      index= [c for c in to_doubleup_1.columns],
            #                                      columns = [c + "1" for c in to_doubleup_1.columns])
            to_doubleup_2 = to_doubleup[1::2].rename(columns=dict([(c, c + "2") for c in to_doubleup.columns]))
            #to_doubleup_2 = to_doubleup_2.rename(index=str, columns=dict([(c, c + "2") for c in to_doubleup_2.columns]))
            # to_doubleup_2 = to_doubleup_1.rename(str,
            #                                      index=[c for c in to_doubleup_2.columns],
            #                                      columns=[c + "2" for c in to_doubleup_2.columns])
            to_doubleup_1.reset_index(drop=True, inplace=True)
            to_doubleup_2.reset_index(drop=True, inplace=True)
            #citc_task_one_per_row.reset_
            full_task_data = pandas.concat([citc_task_one_per_row[0:len(citc_task_one_per_row)/2],
                                            to_doubleup_1, to_doubleup_2],axis=1)
            self.task_data = full_task_data


def get_balanced_construal_set(n_trials, n_runs, n_repeats=1):
    """

    :param n_trials: int describing number of trials in each run, or n_runs-length list describing number of trials in each run.
    :param n_runs: number of runs.
    :return:
    """
    # construal_seeker = pandas.read_csv('spunt_dataset/seeker.csv')
    construal_data = pandas.read_csv('spunt_dataset/data.csv')
    construal_data['Q_Mean'] = construal_data.loc[:, ['Q_Body', 'Q_Spec', 'Q_Conc', 'Q_Imag']].mean(1)
    construal_data['A_Mean'] = construal_data.loc[:, ['A_Body', 'A_Spec', 'A_Conc', 'A_Imag']].mean(1)
    all_db_means = construal_data.mean(0)

    getconditionprops = lambda x: x.groupby('Condition').count()['A_Mean'] / x.count()['A_Mean']
    getconditionvals = lambda x: x.groupby('Condition').count()['A_Mean']

    # all_db_means=pandas.concat([all_db_means,getconditionprops(construal_data)])


    # loop through possible candidate sets.
    candidate_set_qualifies = False
    while candidate_set_qualifies == False:

        # algorithmic approach
        # list the indices belonging to each condition
        # then iterate through each run, sample without replacement from each list of indices
        # then we have our groups.
        condition_indices = []
        for c in range(0, 6):
            condition_indices.append(construal_data.index.values[construal_data['Condition'] == (c + 1)])

        candidate_set = [None] * n_runs

        if isinstance(n_trials, int):
            runs_n_trials = [n_trials] * n_runs
        else:
            runs_n_trials = n_trials
        for r in range(0, n_runs):
            n_t = runs_n_trials[r]
            run_vals = []
            # this run has 32 trials.
            extras = (n_t % 6)
            # get the number to select from each condition for this run
            run_condition_count = (
                [int(math.ceil(n_t / 6.0))] * extras + [int(math.floor(n_t / 6.0))] * (6 - extras))
            # shuffle, making sure that we have at least enough.
            while True:
                random.shuffle(run_condition_count)
                if all([c1.__len__() - run_condition_count[ci] >= 0 for ci, c1 in enumerate(condition_indices)]):
                    break
                print "warning: there may not be enough construal items to pick from."

            # now select from condition_indices
            for c in range(0, 6):
                # print(condition_indices[c])
                vals_to_select_for_r_from_c = random.sample(condition_indices[c], run_condition_count[c])
                condition_indices[c] = numpy.setdiff1d(condition_indices[c], vals_to_select_for_r_from_c)
                # run_vals = run_vals + vals_to_select_for_r_from_c
                # instead, should shuffle each of the run vals individually
                random.shuffle(vals_to_select_for_r_from_c)
                # print(vals_to_select_for_r_from_c)
                # and put them into a list of lists
                run_vals.append(vals_to_select_for_r_from_c)

            run_vals_final = []
            # then slice so that the lists are interleaved
            for i in range(0, min(run_condition_count)):
                # this is relying on the fact that the run lengths can only differ by 1
                runval_slice = [v[i] for v in run_vals]
                # then randomize the order of each set of six.
                random.shuffle(runval_slice)
                run_vals_final = run_vals_final + runval_slice
            # finally add the last set, if there's an uneven number of items in each condition.
            if (min(run_condition_count) != max(run_condition_count)):
                last_slice = [rvl[max(run_condition_count) - 1] for j, rvl in enumerate(run_vals) if
                              run_condition_count[j] == max(run_condition_count)]
                random.shuffle(last_slice)
                run_vals_final = run_vals_final + last_slice

            candidate_set[r] = run_vals_final

        # get a random sample of all of the construal trials
        # whole_sample=random.sample(range(0,143),n_trials*n_runs)
        # benefit of the doubt
        candidate_set_qualifies = True
        # iterate through each of the portions in our sample
        # candidate_set=[]
        for portion_i in range(0, n_runs):

            sample_portion = candidate_set[portion_i]  # whole_sample[(portion_i*n_trials):((portion_i+1)*n_trials)]
            # candidate_set.append(sample_portion)
            # check to see that portion's balance score
            sample_means = construal_data.iloc[sample_portion].mean(0)
            # sample_means=pandas.concat([sample_means,getconditionprops(construal_data.iloc[sample_portion])])
            differences = abs(((all_db_means - sample_means) / all_db_means))
            condition_counts = getconditionvals(construal_data.iloc[sample_portion])
            # print differences
            # each portion should differ by less than 2% on the question and answer means
            # and we should have a reasonably similar proportion of true to false answers
            # and at least some false answers!
            # only apply this check to blocks of greater than 8; blocks of less than 8 are practice blocks
            # and we're not concerned about balancing those.
            if runs_n_trials[portion_i] > 10:
                if ((any(differences[['Q_Mean', 'A_Mean']] > 0.02) or any(differences[['Answer']] > 0.1) or
                             sample_means['Answer'] == 1)):
                    # repeat
                    candidate_set_qualifies = False
                    break
                # and also the counts of each individual condition have to be relatively close.
                if max(condition_counts) > (min(condition_counts) + 1):
                    candidate_set_qualifies = False
                    break
    # we got to the end; that means we found a good set!
    print candidate_set
    return candidate_set
    # if it is sufficient, pass the selection out.

def get_construal_data_with_means():
    construal_data = pandas.read_csv('spunt_dataset/data.csv')
    construal_data['Q_Mean'] = construal_data.loc[:, ['Q_Body', 'Q_Spec', 'Q_Conc', 'Q_Imag']].mean(1)
    construal_data['A_Mean'] = construal_data.loc[:, ['A_Body', 'A_Spec', 'A_Conc', 'A_Imag']].mean(1)
    return construal_data

class ItcConstrualConditionDesign:
    RandomCounterbalanced, BlockDesignConcreteFirst,BlockDesignAbstractFirst = range(3)


# class ItcConstrualDesigns:
#     RandomCounterbalanced, SixBlockConditions = range(2)

def get_construal_set_block(n_total_trials,n_runs,condition,monotonic_construal_sets_only=True):
    """
        this should return a set of construal IDs that are divided into exactly 3 blocks.
        They will come in two possible orders. the condition will be set by a variable passed in and accepts either 0 or 1.
        n_runs must be a multiple of 3. If there are more than 3 runs then each set of n_runs/3 runs will be treated as one block for the purposes of this

    :param n_total_trials:
    :param n_runs:
    :return: a set of construal IDs that are divided into exactly 6 blocks.
    """
    #I think we can do this from the
    assert [ItcConstrualConditionDesign.BlockDesignConcreteFirst,ItcConstrualConditionDesign.BlockDesignAbstractFirst].__contains__(condition)
    return get_construal_set(n_total_trials,n_runs,n_repeats=1,construal_design=condition,monotonic_construal_sets_only=True)

def get_balanced_construal_set_2(n_total_trials, n_runs, n_repeats=1,require_balance_from_trial=None,monotonic_construal_sets_only=False):
    if require_balance_from_trial is None : require_balance_from_trial=[n_total_trials]
    #for construal, require_balance_from_trial has to be spaced at least n_repeats*6 apart.
    spaces_apart=[b-a for a,b in zip(require_balance_from_trial[0:-1],require_balance_from_trial[1:])]
    construal_balance_trials=[require_balance_from_trial[0]]
    a=0
    for i, b in enumerate(require_balance_from_trial[1:]):
        s=spaces_apart[i]
        a=a+s
        if a>=n_repeats*6:
            construal_balance_trials =construal_balance_trials+[require_balance_from_trial[i+1]]
            a=0

    return get_construal_set(n_total_trials, n_runs, n_repeats,
                             construal_design=ItcConstrualConditionDesign.RandomCounterbalanced,
                             require_balance_from_trial=construal_balance_trials,
                             monotonic_construal_sets_only=monotonic_construal_sets_only)


def get_construal_set(n_total_trials, n_runs, n_repeats=1, construal_design=ItcConstrualConditionDesign.RandomCounterbalanced,
                      require_balance_from_trial=None,monotonic_construal_sets_only=False):
    """

    :param n_total_trials: int describing number of trials in each run, or n_runs-length list describing number of trials in each run.
    :param n_runs: number of runs.
    :param require_balance_throughout_task: if set to true, this will ensure that the set is relatively balanced regardless of how long it is being run for.
    :param monotonic_construal_sets_only: if set to true, this only uses some of the construal conditions, 2,3,4,5; these 4 conditions can be monotonically arranged from most abstract to most concrete, in contrast to the other two conditions, whose status is unclear.
    :return:
    """
    # Need to improve by:
    # allowing to duplicate within-number sets (e.g., follow every condition 1 with another condition 1)

    # set n_trials to be divied by the number of repeats of each condition type
    try:
        if any([x % n_repeats > 0 for x in n_total_trials]):
            raise Exception("n_total_trials must be a multiple of n_repeats")
        n_trials = [x / n_repeats for x in n_total_trials]
    except TypeError, te:
        if n_total_trials % n_repeats > 0:
            raise Exception("n_total_trials must be a multiple of n_repeats")
        n_trials = n_total_trials / n_repeats
    # hello.

    isBlockDesign=False
    # for the SixBlockConditions design, n_runs must be a multiple of 6
    # and there must block condition specified
    if [ItcConstrualConditionDesign.BlockDesignConcreteFirst,ItcConstrualConditionDesign.BlockDesignAbstractFirst].__contains__(construal_design):
        isBlockDesign=True
        #if n_runs % 6 != 0:
        if monotonic_construal_sets_only:
            assert (n_runs % 4 == 0)
        else:
            assert (n_runs % 6 == 0)
        #print "isBlockDesign"
    #else:
    #    print "is Not block design"
        #assert SixBlockConditions_condition is not None

    #only allow a SixBlockConditionsCondition for SixBlockConditions; otherwise it makes no sense.
    #if construal_design ==ItcConstrualConditionDesign.RandomCounterbalanced:
    #    assert SixBlockConditions_condition is None

    # allowing to add a mirror set after the original (
    # construal_seeker = pandas.read_csv('spunt_dataset/seeker.csv')
    construal_data = get_construal_data_with_means()
    all_db_means = construal_data.mean(0)


    getconditionprops = lambda x: x.groupby('Condition').count()['A_Mean'] / x.count()['A_Mean']
    getconditionvals = lambda x: x.groupby('Condition').count()['A_Mean']

    # all_db_means=pandas.concat([all_db_means,getconditionprops(construal_data)])
    # get the target means for each run

    condition_indices_range=[None]*n_runs
    run_target_means = [None]*n_runs
    run_target_stds= [None]*n_runs
    run_target_answer_2_proportion = [None]*n_runs
    #determine the range of conditions for each run.
    #conditions are numbered 0 through 5 here.
    #let's try to keep the indices referring to indices of the original set of SIX conditions.
    if [ItcConstrualConditionDesign.BlockDesignConcreteFirst,
          ItcConstrualConditionDesign.BlockDesignAbstractFirst].__contains__(construal_design):
        if construal_design == ItcConstrualConditionDesign.BlockDesignAbstractFirst:
            # go from abstract to concrete
            condition_indices_range = [[c-1] for c in [3,2,5,4]]#[5,6,3,4,1,2]]  # select from a set of conditions for every run.
        elif construal_design == ItcConstrualConditionDesign.BlockDesignConcreteFirst:
            # go from concrete to abstract
            condition_indices_range = [[c-1] for c in [4,5,2,3]]#[2,1,4,3,6,5]]  # select from a set of conditions for every run.
    elif construal_design == ItcConstrualConditionDesign.RandomCounterbalanced:
        for r in range(0,n_runs):
                if monotonic_construal_sets_only:
                    condition_indices_range[r] = [(c-1) for c in [2,3,4,5]]  # only select from the same ones we used above.
                else:
                    condition_indices_range[r] = range(0, 6) # only select from the same ones we used above.
    #record which conditions we're using
    selected_condition_indices_set = list(set().union(*condition_indices_range))

    for r in range(0, n_runs):
        #get the means we want to target for each run.
        run_target_means[r] = construal_data[construal_data.Condition.isin([i+1 for i in condition_indices_range[r]])].mean(0)
        run_target_answer_2_proportion[r] = float(sum(construal_data.Answer[
            construal_data.Condition.isin([i + 1 for i in condition_indices_range[r]])]==2))/len(construal_data.Answer[
            construal_data.Condition.isin([i + 1 for i in condition_indices_range[r]])])
        run_target_stds[r] = construal_data[
            construal_data.Condition.isin([i + 1 for i in condition_indices_range[r]])].std()


    candidate_count=0
    selected_condition_indices=None
    # loop through possible candidate sets.
    candidate_set_qualifies = False
    while candidate_set_qualifies == False:
        candidate_count=candidate_count+1
        # algorithmic approach

        # list the indices belonging to each condition
        condition_indices = []
        for c in range(0,6):
            condition_indices.append(construal_data.index.values[construal_data['Condition'] == (c+1)])

        # then iterate through each run, sample without replacement from each list of indices
        # then we have our groups.
        candidate_set = [None] * n_runs

        #make sure runs_n_trials is a list of integers, one for each run.
        if isinstance(n_trials, int):
            runs_n_trials = [n_trials] * n_runs
        else:
            runs_n_trials = n_trials
        #ADDED THIS INDEX IN FOR THE CONDITION_INDICES RANGE BUT THAT BREAKS THE FMRI
        n_construal_conditions=len(selected_condition_indices_set) #len(condition_indices_range[0])

        #create an array with just the conditions we actually want to access; this will be convenient.
        selected_condition_indices=[condition_indices[i] for i in selected_condition_indices_set]

        #for each run
        for r in range(0, n_runs):
            n_t = runs_n_trials[r]
            run_vals = []
            # this run has 32 trials.
            extras = (n_t % n_construal_conditions)
            #print condition_indices_range[r]
            n_conds=len(pandas.unique(condition_indices_range[r]))
            # get the number to select from each condition for this run
            run_selected_condition_count = (
                    [int(math.ceil(float(n_t) / n_conds))] * extras + [int(math.floor(n_t / n_conds))] * (n_construal_conditions - extras))
            # shuffle, making sure that we have at least enough.
            while True:
                random.shuffle(run_selected_condition_count)

                #make sure there's enough items to choose from for the size of trial that we want.
                if all([c1.__len__() - run_selected_condition_count[ci] >= 0 for ci, c1 in
                        enumerate(selected_condition_indices)]):
                    break
                print "warning: there may not be enough construal items to pick from."

            # now select from condition_indices for this run.
            for i,c in enumerate(condition_indices_range[r]):
                #select a few indicess from each condition.
                vals_to_select_for_r_from_c = random.sample(condition_indices[c], run_selected_condition_count[i]*n_repeats)
                #update the condition index list to remove the values we "used".
                condition_indices[c] = numpy.setdiff1d(condition_indices[c], vals_to_select_for_r_from_c)

                # instead, should shuffle each of the run vals individually
                random.shuffle(vals_to_select_for_r_from_c)
                # print(vals_to_select_for_r_from_c)
                # and put them into a list of lists
                run_vals.append(vals_to_select_for_r_from_c)

            if isBlockDesign:
                run_vals_final = [item for sublist in run_vals for item in sublist]
                #not sure this will work for two-condition runs but it will work for a one-condition run at least.
            elif not isBlockDesign:
                run_vals_final = []
                # then slice so that the lists are interleaved.
                for i in range(0, min(run_selected_condition_count)):
                    # this is relying on the fact that the run lengths can only differ by 1
                    #we're potentially going to take more than one value each time
                    runval_slice = [v[(i*n_repeats):(i*n_repeats+2)] for v in run_vals]
                    # then randomize the order of each set of six.
                    random.shuffle(runval_slice)
                    #OK, so if n_repeats>1 then runval_slice will be a list of lists; time to flatten.
                    #if n_repeats>1:#flatten the list
                    runval_slice = [item for sublist in runval_slice for item in sublist]
                    run_vals_final = run_vals_final + runval_slice
                    if n_repeats==1:
                        raise Exception("Discovered a bug where n_repeats is 1 and I'm not sure that this will work. but you can try...")
                # finally add the last set, if there's an uneven number of items in each condition.
                if (min(run_selected_condition_count) != max(run_selected_condition_count)):
                    #ahh, for each group rvl where we want an extra run out of it, pick the nth value (because weouldn't have picked it before now)
                    rangemin=(max(run_selected_condition_count) - 1)*n_repeats
                    rangemax=rangemin+2
                    last_slice = [rvl[rangemin:rangemax] for j, rvl in enumerate(run_vals) if
                                  run_selected_condition_count[j] == max(run_selected_condition_count)]
                    random.shuffle(last_slice)
                    if n_repeats>1:#flatten the list
                        last_slice = [item for sublist in last_slice for item in sublist]
                    run_vals_final = run_vals_final + last_slice


            candidate_set[r] = run_vals_final
            #this candidate set should be a list, one item for each run, of integer vectors
            #if it's something different, then we need to look into why.

        #now TEST TO SEE IF THIS SET WORKS.
        # get a random sample of all of the construal trials
        # benefit of the doubt
        candidate_set_qualifies = True
        # iterate through each of the portions in our sample
        # candidate_set=[]
        for portion_i in range(0, n_runs):
            #do we want to just check the whole set, or are we interested in making sure that the set is balanced throughout?
            if require_balance_from_trial is None:
                check_point = [len(candidate_set[portion_i])]
            elif hasattr(require_balance_from_trial, '__iter__'):
                check_point = require_balance_from_trial
            else:
                #we require balance from a particular trial onwards so let's make sure that's set up!
                check_point = [i*6*n_repeats for i in range(require_balance_from_trial/(n_construal_conditions*n_repeats), 
                                                            len(candidate_set[portion_i])/(n_construal_conditions*n_repeats))]

            for check_point_i in check_point:


                sample_portion = candidate_set[portion_i][0:check_point_i]  # whole_sample[(portion_i*n_trials):((portion_i+1)*n_trials)]
                # check to see that portion's balance score
                #print sample_portion
                sample_means = construal_data.iloc[sample_portion].mean(0)
                #these are potentially different for each run to allow for the mTurk version
                # in which different versoins
                differences_std = abs(((run_target_means[portion_i] - sample_means) / run_target_stds[portion_i]))
                differences_abs = abs(((run_target_means[portion_i] - sample_means) / run_target_means[portion_i]))
                condition_counts = getconditionvals(construal_data.iloc[sample_portion])
                # print differences
                # each portion should differ by less than 2% of the question and answer means
                # NEW RULE: differ by less than 10% of 1 SD of the entire sample population.
                # and we should have a reasonably similar proportion of true to false answers
                # and at least some false answers!
                # only apply this check to blocks of greater than 8; blocks of less than 8 are practice blocks
                # and we're not concerned about balancing those.
                if runs_n_trials[portion_i] > 10:
                    if ((any(differences_abs[['Q_Mean', 'A_Mean']] > 0.02) or any(differences_abs[['Answer']] > 0.1) or
                                 sample_means['Answer'] > 0)) and ItcConstrualMeanRule.fMRILegacyMethod:
                        # repeat
                        candidate_set_qualifies = False
                        break

                    if (any(differences_std[['Q_Mean', 'A_Mean']] > 1/numpy.sqrt(check_point_i+1)) or
                            sum(construal_data.Answer[sample_portion] == 2) < (run_target_answer_2_proportion[portion_i]*len(construal_data.Answer[sample_portion])-1) or
                                sum(construal_data.Answer[sample_portion] == 2) > (run_target_answer_2_proportion[portion_i]*len(construal_data.Answer[sample_portion]) + 1)) and ItcConstrualMeanRule.StdDevMethod:
                        # repeat
                        candidate_set_qualifies = False
                        break
                    # and also the counts of each individual condition have to be relatively close.
                    if max(condition_counts) > (min(condition_counts) + 1):
                        candidate_set_qualifies = False
                        break

            if candidate_set_qualifies==False:
                #print "broke on " + str(check_point_i)
                break
    # we got to the end; that means we found a good set!
    #print "n_repeats: " +str(n_repeats)
    #print "ItcConstrualConditionDesign: " + str(construal_design)

    print candidate_set
    return candidate_set
    # if it is sufficient, pass the selection out.
