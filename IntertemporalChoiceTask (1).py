import random
import pandas
import hashlib
import numpy
# SALIENCE_CONDITION_AMOUNT=0
# SALIENCE_CONDITION_DELAY=1

class IntertemporalChoiceTask:
    """This class manages parameters for an intertemporal choice class
    If we want to actively manage k an experiment on the server-side, this would be the place to do it.
    by default it creates an ITC dataframe
    It can also populate it with parameters
    """

    # def confirm_logicfile_access():
    #     return "access confirmed"
    #choose condition based on the subject ID, run ID, and experimental day,

    #so that these will be counterbalanced
    def choose_condition(subject_id,run_id,exp_day):
        return ((int(subject_id) + int(run_id) + int(exp_day)) % 2)

    def __init__(self,
                 n,subid,day,runid,salience_condition=None,include_dominated_trials=False,task_version='generic',
                 mean_intertask_interval=2,
                 mean_intratask_interval=1,
                 min_intertask_interval=0.5,
                 min_intratask_interval=0.5,
                 require_balance_from_trial=None
                 ):
        if salience_condition is None:
            #raise Exception("need to insert code here for selecting a salience condition based on other data")
            #salienceCondition is gonna be based on subject+run
            salience_condition=(subid+runid) % 2



        self.subid=subid

        self.runid=runid
        self.day=day
        self.task_version=task_version
        self.salience_condition=salience_condition
        self.task_data=create_itc_dataframe(
            n,subid,day,runid,salience_condition
        )
        self.n_trials = n
        self.include_dominated_trials = include_dominated_trials

        self.intertask_interval_mean = mean_intertask_interval
        self.intertask_interval_min = min_intertask_interval
        self.intratask_interval_mean = mean_intratask_interval

        self.intratask_interval_min = min_intratask_interval

        self.iti_fixedamount_values = [25, 30]
        self.iti_variableamount_interval = [20, 40]
        if require_balance_from_trial is None:
            self.require_balance_from_trial = [n]
        else:
            self.require_balance_from_trial=require_balance_from_trial

        self.task_arrangement = ItcTaskArrangement.TasksInterleaved #the default.

        self.subjectclass_seed = self.subid
            # a value for ensuring a different random set for each subject.
            #for instances where we actually want the same seed across subjects or across a particular group of subjects
            #we can manually set this.


    def get_pseudorandom_seed(self,task_salt,consistent_across_runs=False):
        """generate a pseudorandom seed that is predictable on the basis of this subject's ID, run, experimental day, task_version
                rand_salt should be an additional constant that is the same for any particular task
                should be randomly generated once, and then hard-coded. This is to ensure our pseudorandom seed
                is different for each generated value.
                """
        if consistent_across_runs:
            runid_to_pass=None
        else:
            runid_to_pass=self.runid
        return get_pseudorandom_seed(task_salt,
                              task_version=self.task_version,
                              subid=self.subjectclass_seed,
                              day=self.day,
                              runid=runid_to_pass)

    def update_trial(self,trial_i,ss_onLorR,startingK,endingK,
                     trialStart,iti,choice_presented,choice_made,
                     trial_over,condition,choice,
                     ss_amount=None,ll_delay=None):
        self.task_data.loc[trial_i, 'SSonLorR'] = ss_onLorR
        self.task_data.loc[trial_i, 'RT'] = choice_made-choice_presented
        self.task_data.loc[trial_i, 'startingK'] = startingK
        self.task_data.loc[trial_i, 'endingK'] = endingK
        self.task_data.loc[trial_i, 'TrialStart'] = trialStart
        self.task_data.loc[trial_i, 'ITI'] = iti
        self.task_data.loc[trial_i, 'choiceUp'] = choice_presented
        self.task_data.loc[trial_i, 'choiceMade'] = choice_made
        self.task_data.loc[trial_i, 'TrialOver'] = trial_over
        self.task_data.loc[trial_i, 'Condition'] = condition
        self.task_data.loc[trial_i, 'Choice'] = choice
        if ss_amount is not None:
            self.task_data.loc[trial_i, 'SSamount'] = ss_amount
        if ll_delay is not None:
            self.task_data.loc[trial_i, 'LLdelay'] = ll_delay
        self.task_data.loc[trial_i, 'SSonLorR'] = trial_over

    def setup_screen_sides(self):
        ss_on_l_or_r = ["L","R"]*(self.n_trials/2)
        random.shuffle(ss_on_l_or_r)
        self.task_data['SSonLorR'] = pandas.Series(ss_on_l_or_r)

    def setup_iti(self):
        self.task_data['ITI'] = get_iti(
            self.n_trials,
            mean_iti=self.intertask_interval_mean,
            min_iti=self.intertask_interval_min,
            max_iti=self.intertask_interval_mean+5.0,
            require_balance_from_trial=self.require_balance_from_trial)

    def setup_task_interval(self):
        self.task_data['TaskInterval'] = get_iti(
            self.n_trials,
            mean_iti=self.intratask_interval_mean,
            min_iti=self.intratask_interval_min,
            max_iti=self.intratask_interval_mean+4.0,
            require_balance_from_trial=self.require_balance_from_trial)

    def populate_itc_task_with_parameters(self):
        """
                sets up ITC task with parameters
                :return:
                """
        # we are going to need:
        # SSonLorR
        # ITI [include this!]
        # SSamount [3 of the 4 main amount variables should be set]
        # LLamount  [3 of the 4 main amount variables should be set]
        # Condition
        # SSdelay  [3 of the 4 main amount variables should be set]
        # LLdelay [3 of the 4 main amount variables should be set]
        # salienceCondition
        # day
        # runid

        # assume the thing has already been created so we have basic columns filled out
        # and the task_data table itself has been created.

        # SSonLorR
        # to copy James's code we want:
        # an even selection of 1's and 2's
        # randomly ordered.
        # although James has included some complicated code to balance, it doesn't appear to be needed
        # I tested this and the generated design appears to always pass the test on the first time.
        # so, as long as we generate a genuinely randomized order, we seem to be fine.
        # we're going to make everything pseudorandomized, using
        # subject runid,

        # n_trials needs to be a multiple of four for the things we set up below to work.
        if self.n_trials % 4 > 0:
            raise Exception("n_trials is " + str(self.n_trials), ", but it must be a multiple of 4")
        # now we get a randomly selected set of L/R values...


        #randomize the side that SS is presented on.
        #this loops through require_balance_from_trial so that the sides are fairly balanced no matter at which point
        #the subject ends on.
        random.seed(self.get_pseudorandom_seed('SSonLorR'))
        L_or_R=[]
        iterrange=[0]+self.require_balance_from_trial
        for i,t in enumerate(iterrange):
            if i==0:
                continue
            #we will generate values at each point to ensure a precise balance of left and right all the time.
            lrrange=(iterrange[i]-iterrange[i-1])
            L_or_R_addition = (["L", "R"] * (lrrange / 2))
            random.shuffle(L_or_R_addition)
            L_or_R = L_or_R + L_or_R_addition

        self.task_data['SSonLorR'] = L_or_R

        # ITI
        # %the ITI should be a random permutation of the possible distances from the
        # %start of the TR added to a 1.5 second ITI, want the same trial length too so
        # %figure out how much of a second (since this is our TR) needs to be added
        # %to the end of the trial
        # %make the ITI an exponential distribution with a mean of 2
        # -AndrewJamesMelrose

        random.seed(self.get_pseudorandom_seed('ITI'))
        self.setup_iti()  # this will automatically add it to the task data

        random.seed(self.get_pseudorandom_seed('TaskInterval'))
        self.setup_task_interval()  # this will automatically add it to the task data

        #method one for determining which trial is rewarded
        #OBSOLETE
        # random.seed(self.get_pseudorandom_seed('RewardTrial'))
        # rewardTrialNum=random.sample(range(0,self.n_trials),1)[0]
        # self.task_data['RewardTrial']=0
        # self.task_data.loc[rewardTrialNum, 'RewardTrial'] = 1

        #method 2 for determining which trial is rewarded. All trials are ranked. this way, in the event subject
        #doesn't provide a response to the top-ranked trial, we can choose an alternative trial to reward them with.

        rewardTrialRankNum =range(0, self.n_trials)
        random.seed(self.get_pseudorandom_seed('RewardTrialRanked'))
        random.shuffle(rewardTrialRankNum)
        self.task_data['RewardTrialRanked'] = rewardTrialRankNum


        # condition
        condition_STANDARD = 1
        condition_DOMINANT = 2
        random.seed(self.get_pseudorandom_seed('Condition'))
        if self.include_dominated_trials:
            condition=[]
            for i, t in enumerate([0] + self.require_balance_from_trial):
                if i == 0:
                    continue
                # we will generate values at each point to ensure a precise balance of left and right all the time.
                condition_range = (self.require_balance_from_trial[i] - self.require_balance_from_trial[i - 1])
                condition_addition = ([1, 1, 1, 2] * (condition_range / 4))
                random.shuffle(condition_addition)
                condition = condition + condition_addition

            condition = ([1, 1, 1, 2] * (self.n_trials / 4))
        else:
            condition = ([1] * (self.n_trials))
            random.shuffle(condition)
        self.task_data['Condition'] = condition

        if self.salience_condition == ItcSalienceCondition.Amount:
            if self.iti_variableamount_interval[1] - self.iti_variableamount_interval[0]>2.0:
                amount_LL_array = get_balanced_repeated_integer_sample_wout_replacement(
                    self.iti_variableamount_interval[0], self.iti_variableamount_interval[1], self.n_trials,
                    self.get_pseudorandom_seed('amountLLamountSalient'),
                    require_balance_from_trial=self.require_balance_from_trial)
            else:
                amount_LL_array = get_balanced_repeated_float_sample(
                    self.iti_variableamount_interval[0], self.iti_variableamount_interval[1], self.n_trials,
                    self.get_pseudorandom_seed('amountLLamountSalient'),points=20,
                    require_balance_from_trial=self.require_balance_from_trial)
            self.task_data['LLamount'] = pandas.Series(amount_LL_array)
            self.task_data['SSdelay'] = pandas.Series([5] * self.n_trials)
            # but for dominated trials, these are going to be the same
            #self.task_data.loc[self.task_data.Condition == condition_DOMINANT, 'SSdelay'] = 90
            #actually no. we will rely on the front-end to adjust this; because we need the variable-amount to be calculated based on the
            #value that would have been displayed.
            self.task_data['LLdelay'] = pandas.Series([90] * self.n_trials)
        elif self.salience_condition == ItcSalienceCondition.Delay:
            delay_SS_array = get_balanced_repeated_integer_sample_wout_replacement(
                1, 9, self.n_trials,
                self.get_pseudorandom_seed('delayLLdelaySalient'),
                self.require_balance_from_trial)
            self.task_data['SSdelay'] = pandas.Series(delay_SS_array)
            self.task_data['SSamount'] = pandas.Series([self.iti_fixedamount_values[0]] * self.n_trials)
            self.task_data['LLamount'] = pandas.Series([self.iti_fixedamount_values[1]] * self.n_trials)
            # but for dominated trials, these are going to be the same
            #self.task_data.loc[self.task_data.Condition == condition_DOMINANT, 'LLamount'] = 25

class ItcTaskArrangement:
    TasksInterleaved, TasksBlocked = range(2)

class ItcSalienceCondition:
    Amount, Delay = range(2)


def get_iti(n_trials,mean_iti=2.0,min_iti=0.5,max_iti=5.0,require_balance_from_trial=None):
    if require_balance_from_trial is None:
        require_balance_from_trial=n_trials

    while True:
        #exponential distribution starting with min_iti, with a mean of mean_iti and we try and try again until we don't get above max_iti.
        iti=[random.expovariate(1.0/(mean_iti-min_iti))+min_iti for i in range(0,n_trials)]
        present_round_is_balanced=True
        for check_point_i in require_balance_from_trial:
            s_iti=sum(iti[0:check_point_i])
        #print(s_iti)
            if (s_iti > (check_point_i*mean_iti-1) and s_iti < (check_point_i*mean_iti+1) and max(iti[0:check_point_i])<max_iti)==False:
                present_round_is_balanced=False
                break
        if present_round_is_balanced:
            return iti

def get_balanced_repeated_float_sample(rangemin,rangemax,n,seed,points=None,require_balance_from_trial=None):
    if require_balance_from_trial is None:
        require_balance_from_trial = [n]
    suitable_range_found = False
    random.seed(seed)
    if points is None:
        points=n

    #if points > n:
    #    raise Exception("It's reasonable to want more points in the sequence than n but we are not currently catering for that.")

    rangeSize = rangemax - rangemin
    while suitable_range_found == False:

        range_n = 0
        myseries = [0.0]*n

        while range_n < n:
            #builds up the range
            myrange=[x*(rangeSize/points)+rangemin for x in range(0,points+1)]
            random.shuffle(myrange) # needs to be a shuffled range!
            #populate range
            myseries[range_n:(min(range_n + points, n))] = myrange[0:(min(n - range_n, points))]
            #mark out how long we want to go.
            range_n = (range_n + points)

        middle_value = (rangemax - rangemin) / 2 + rangemin

        #go through each of the check points and ensure that for this check point, we're roughly in the middle.
        suitable_range_found=True
        for check_point_i in require_balance_from_trial:
            part_series=myseries[0:check_point_i]
            windowsize = (rangemax - rangemin) /  (pow(check_point_i,0.5) * 2)
            if (numpy.mean(part_series) > (middle_value - windowsize) and numpy.mean(part_series) < (middle_value + windowsize))==False:
                # close enough, let's finish off!
                suitable_range_found = False
                break

    return myseries



def get_balanced_repeated_integer_sample_wout_replacement(rangemin,rangemax,n,seed,require_balance_from_trial=None):
    """
    Gets a balanced repeated integer sample ensuring that:
    if the integer range is smaller than n, then each item will appear once in sequence
    before any other item appears, so that at all times, there's only at most 1 difference between the count
    of appearance of each item.
    regardless of whether the range is larger or smaller than n,
    the mean of the range will appear close to the middle of the range,
    either within 5% or not more than 1 difference, whichever is larger.
    :param rangemin:
    :param rangemax:
    :param n:
    :param seed:
    :return:
    """
    if require_balance_from_trial is None:
        require_balance_from_trial = [n]
    suitable_range_found = False
    random.seed(seed)

    while suitable_range_found == False:
        rangeSize = rangemax - rangemin;
        range_n = 0;
        myseries = [0]*n
        while range_n < n:
            myrange=range(rangemin,rangemax+1)
            random.shuffle(myrange) # needs to be a shuffled range!
            myseries[range_n:(min(range_n + rangeSize, n))] = myrange[0:(min(n - range_n, rangeSize))]
            range_n = (range_n + rangeSize)

        #% the average of the values chosen should be close to the middle!

        middle_value = (rangemax - rangemin) / 2 + rangemin

        # go through each of the check points and ensure that for this check point, we're roughly in the middle.
        suitable_range_found = True
        for check_point_i in require_balance_from_trial:
            part_series = myseries[0:check_point_i]
            windowsize = max(middle_value * .05, 1)
            if (numpy.mean(myseries) > (middle_value - windowsize) and numpy.mean(myseries) < (middle_value + windowsize)) == False:
                # close enough, let's finish off!
                suitable_range_found = False
                break


    return myseries

#get amounts from a range ensuring that the range's mean-median
#and items are evenly distributed
def setup_randomly_ordered_amounts_from_range(rangemin,rangemax,n,seed):
    raise Exception('Deprecated in favor of get_balanced_repeated_integer_sample_wout_replacement')
    amounts=[float(x) / (n) * (rangemax - rangemin) + rangemin for x in range(0, n + 1)]
    #the seed is the same thing we use to choose the condition, plus some random entropy
    #plus the ranges we're using, so that it's specific to the range (amount vs. delay)
    random.seed(seed+608009+rangemax+rangemin)
    random.shuffle(amounts)


    #we haven't checked these are actually balanced and not increasing or decreasing.
    #we probably should but whatevs.
    return amounts

def create_itc_dataframe(n,subid,day,runid,salience_condition):
    #'Subject\tTrial\tSSonLorR\tRT\tstartingK
    ## \tendingK\tTrialStart\tITI\tchoiceUp\tchoiceMade\t
    ## TrialOver\tSSamount\tLLamount\tCondition\tChoice\t
    # SSdelay\tLLdelay\tsalienceAmount\n');

    pdf = pandas.DataFrame({
        "Subject": [subid]*n,
        "Trial": range(1,n+1),
        "SSonLorR":[""]*n,
        "RT":[None]*n,
        "startingK":[None]*n,
        "endingK":[None]*n,
        "TrialStart":[None]*n,
        "ITI":[None]*n,
        "choiceUp":[None]*n,
        "choiceMade": [None] * n,
        "TrialOver": [None] * n,
        "SSamount": [None] * n,
        "LLamount": [None] * n,
        "Condition": [None] * n,
        "Choice": [None] * n,
        "SSdelay": [None] * n,
        "LLdelay": [None] * n,
        "salienceCondition": salience_condition,
        "day": [day] * n,
        "runid": [runid] * n,
    }
    )
    pdf_ordered=pdf[["Subject", "Trial", "SSonLorR", "RT", "startingK",
                     "endingK", "TrialStart", "ITI", "choiceUp", "choiceMade",
                     "TrialOver", "SSamount", "LLamount", "Condition", "Choice",
                     "SSdelay", "LLdelay", "salienceCondition","day","runid"]]
    return pdf_ordered

def get_pseudorandom_seed(task_salt,task_version,subid,day,runid=None):
    """generate a pseudorandom seed that is predictable on the basis of this subject's ID, run, experimental day, task_version
    rand_salt should be an additional constant that is the same for any particular task
    should be randomly generated once, and then hard-coded. This is to ensure our pseudorandom seed
    is different for each generated value.
    """
    short_int_hash=lambda x:int(hashlib.md5(str(x)).hexdigest()[0:6],16)



    meta_seed = short_int_hash(str(task_version)+'651901') + \
                short_int_hash(str(subid)+'900185') + \
                short_int_hash(day+633850) + \
                short_int_hash(task_salt+'696737')

    if runid is not None:
        meta_seed = meta_seed+ short_int_hash(str(runid) + '58236')

    random.seed(meta_seed)
    return random.randint(0,pow(10,12))
