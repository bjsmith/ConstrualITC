import random
import pandas

SALIENCE_CONDITION_AMOUNT=0
SALIENCE_CONDITION_DELAY=1
class IntertemporalChoiceTask:
    def confirm_logicfile_access():
        return "access confirmed"
    #choose condition based on the subject ID, run ID, and experimental day,

    #so that these will be counterbalanced
    def choose_condition(subject_id,run_id,exp_day):
        return ((int(subject_id) + int(run_id) + int(exp_day)) % 2)

    def __init__(self,condition,n,subid,day,runid,salience_condition):
        self.task_data=IntertemporalChoiceTask.create_itc_dataframe(
            condition,n,subid,day,runid,salience_condition
        )

    def update_trial(self,trial_i,ss_onLorR,startingK,endingK,
                     trialStart,iti,choice_presented,choice_made,
                     trial_over,condition,choice,
                     ss_amount=None,lldelay=None):
        self.task_data.loc[trial_i, 'SSonLorR'] = ss_onLorR
        self.task_data.loc[trial_i, 'rt'] = choice_made-choice_presented
        self.task_data.loc[trial_i, 'startingK'] = startingK
        self.task_data.loc[trial_i, 'endingK'] = endingK
        self.task_data.loc[trial_i, 'TrialStart'] = trialStart
        self.task_data.loc[trial_i, 'ITI'] = iti
        self.task_data.loc[trial_i, 'choiceUp'] = choice_presented
        self.task_data.loc[trial_i, 'choiceMade'] = choice_made
        self.task_data.loc[trial_i, 'TrialOver'] = trial_over
        self.task_data.loc[trial_i, 'Condition'] = condition
        self.task_data.loc[trial_i, 'Choice'] = choice
        self.task_data.loc[trial_i, 'SSamount'] = ss_amount
        self.task_data.loc[trial_i, 'LLdelay'] = lldelay
        self.task_data.loc[trial_i, 'SSonLorR'] = trial_over




#get amounts from a range ensuring that the range's mean-median
#and items are evenly distributed
def setup_randomly_ordered_amounts_from_range(rangemin,rangemax,n,seed):
    amounts=[float(x) / (n) * (rangemax - rangemin) + rangemin for x in range(0, n + 1)]
    #the seed is the same thing we use to choose the condition, plus some random entropy
    #plus the ranges we're using, so that it's specific to the range (amount vs. delay)
    random.seed(seed+608009+rangemax+rangemin)
    random.shuffle(amounts)

    #we haven't checked these are actually balanced and not increasing or decreasing.
    #we probably should but whatevs.
    return amounts

def create_itc_dataframe(condition,n,subid,day,runid,salience_condition):
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
