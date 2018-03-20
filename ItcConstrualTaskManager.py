from ItcConstrualTask import *
import time,os,pandas,numpy,shutil
import re

class ItcConstrualTaskManager:

    def __init__(self):
        return;

            #cool.
            #right so for a single script we are going to need....

            # for each trial we are going to need:
            # subject info

            # subject, trial, day, runid,
            # ITC task information
            # SSonLorLR, SSDelay, LLDelay, SSAmount, LLAmount, DominanceCondition, SalienceCondition,
            # ITC task display information
            # LeftColor, RightColor, ITILength
            # #we will NOT include LeftText, RightText, because we can't know these without knowing all four
            # #ITC values and we don't know that until we're in the experiment calculating the user's k-value.


            # construal task
            # condition, question, answer, stim_id

            #try to present in this order, and then include extra things over the top.
            # Subject
            # Trial
            # SSonLorR
            # RT    [blank]
            # startingK [blank]
            # endingK  [blank]
            # TrialStart  [blank]
            # ITI [include this!]
            # choiceUp [blank]
            # choiceMade [blank]
            # TrialOver [blank]
            # SSamount [3 of the 4 main amount variables should be set]
            # LLamount  [3 of the 4 main amount variables should be set]
            # Condition
            # Choice
            # SSdelay  [3 of the 4 main amount variables should be set]
            # LLdelay [3 of the 4 main amount variables should be set]
            # salienceCondition
            # day
            # runid

            ##color information: color1 is SS, color2 is LL,
            #color1 = [220 100 100];
            #color2 = [100 100 220];

            #so to get all this information, we want to create a IntertemporalChoiceTask object,

            #and use it to generate settings for ITC
            #then we call ConstrualTask and get information for THAT
            #ensuring that they are aligned in the way we want
            #then pass the pandas array back to the script set object to handle.

class RewardSchedule:
    LargeHypothetical, SmallReal = range(2)

def create_two_run_itc_construal_script_set(subid_list,day_count,run_count,n,set_label):
    if not os.path.exists('design_csv_files'):
        os.makedirs('design_csv_files')

    dir_to_create = 'design_csv_files/' + set_label + datetime.now().strftime("%Y%m%d%H%M%S")

    metaloop_list=[]
    metaloop_list.append({
        'LoopFile':'practice.csv',
        'PreTaskInstructions':'You will now see two practice trials before you get started.'})
    if not os.path.exists(dir_to_create):
        os.makedirs(dir_to_create)
    for s in subid_list:
        for d in range(0,day_count):
            for r in range(0,run_count):
                citc_task = ItcConstrualTask(n=n, subid=s, day=(d+1), runid=(r+1))
                citc_task.salience_condition
                citc_task.populate_construal_itc_task_with_parameters()
                task_filename= dir_to_create + '/sub' + str(s) + 'd' + str(d+1) + 'r' + str(r+1) +'.csv'
                if citc_task.salience_condition==SALIENCE_CONDITION_AMOUNT:
                    varying_condition='AMOUNT of money'
                    constant_condition='DELAY to get the money'
                elif citc_task.salience_condition==SALIENCE_CONDITION_DELAY:
                    varying_condition = 'DELAY to get the money'
                    constant_condition = 'AMOUNT of money'

                metaloop_list.append({
                    'LoopFile': task_filename,
                    'PreTaskInstructions': standard_pre_task_instructions(citc_task.salience_condition, 10),
                    'DisplayS': 10
                })

                raise Exception("this function hasn't been tested yet. remove this exception, but test it.")
                citc_task.task_data.to_csv(task_filename,
                                           index=False)




def create_itc_construal_mturk_script_set_interleaveddesign(subjectclassid_list,n,set_label,
    mean_intertask_interval=1,
    mean_intratask_interval=0.3,
    min_intertask_interval=0.75,
    min_intratask_interval=0):
    if not os.path.exists('design_csv_files'):
        os.makedirs('design_csv_files')

    dir_to_create = 'design_csv_files/' + set_label + datetime.now().strftime("%Y%m%d%H%M%S")


    task_filename_list = []
    if not os.path.exists(dir_to_create):
        os.makedirs(dir_to_create)
    for s in subjectclassid_list:
        metaloop_list = []
        metaloop_list.append({
            'LoopFile': 'practice.csv',
            'PreTaskInstructions': 'You will now see two practice trials before you get started.',
            'DisplayS':4})
        metaloop_filename = dir_to_create + '/metaloop_subclass' + str(s) + '.csv'


        #set the conditions
        condition_design = s % 3
        #condition_task_arrangement = (numpy.floor(s/3))%2
        condition_salience_on_first_run = (numpy.floor(s / 6)) % 2


        if condition_design==ItcConstrualConditionDesign.RandomCounterbalanced:
            construal_set = get_balanced_construal_set_2(n, 6, n_repeats=2)

        elif [ItcConstrualConditionDesign.BlockDesignConcreteFirst, ItcConstrualConditionDesign.BlockDesignConcreteFirst].__contains__(condition_design):
            construal_set = get_construal_set_block(n,6,condition_design)

        #THERE WILL BE 6 RUNS
        #WITHIN EACH SUBJECT, REWARDSCHEDULE WILL HAVE TO BE CONFLATED WITH THE LEVELS. BUT WE CAN ALTERNATE IT SO IT WON'T BE TOO BAD.
        for r in range(0,6):

            run_salience_condition = (condition_salience_on_first_run + r) % 2

            citc_task = ItcConstrualTask(n=n, subid=s, day=0, runid=r,
                                         mean_intertask_interval=mean_intertask_interval,
                                         mean_intratask_interval=mean_intratask_interval,
                                         min_intertask_interval=min_intertask_interval,
                                         min_intratask_interval=min_intratask_interval,
                                         salience_condition=run_salience_condition,
                                        construal_mean_rule=ItcConstrualMeanRule.StdDevMethod)
            citc_task.iti_variableamount_interval=[0.40,0.80]
            citc_task.iti_fixedamount_values = [0.50, 0.60]

            #raise Exception(
            #    "ALSO NEED TO REMEMBER: HOWEVER MANY CONDITION FILES WE GENERATE, THEY SOMEHOW NEED TO BE STAGGERED SO THEY'RE NOT CONFLATED WITH CONDITION")
            # RandomCounterBalanced
            citc_task.populate_construal_itc_task_with_parameters(construal_set_ids=construal_set[r])
            task_filename= dir_to_create + '/subclass' + str(s) + 'r' + str(r)+'.csv'
            task_filename_list = task_filename_list + [task_filename]
            #"On this block, you will always be choosing between $25 and $30 but the delay to get the money will vary."
            #"On this block, you will always be choosing between getting money in 5 days or 90 days but how much money will vary."
            metaloop_list.append({
                'LoopFile': task_filename,
                'PreTaskInstructions': standard_pre_task_instructions(citc_task.salience_condition, 5),
                'DisplayS': 5
            })


            citc_task.task_data.to_csv(task_filename,
                                       index=False)
        #one trial from each run is set the reward trial from that run. But we only want one reward trial for BOTH runs.
        #so we need to select a particular run to reward.
        random.seed(citc_task.get_pseudorandom_seed("SelectRunReward", True))
        run_to_select = random.sample([0, 1], 1)[0]

        metaloop_list_df = pandas.DataFrame(metaloop_list)
        metaloop_list_df['RewardRun']=0
        metaloop_list_df.loc[run_to_select+1,'RewardRun'] = 1
        metaloop_list_df.to_csv(metaloop_filename, index=False)

    return task_filename_list


def create_itc_construal_mturk_script_set(subjectclassid_list, n, set_label,
                                                            mean_intertask_interval=1,
                                                            mean_intratask_interval=0.3,
                                                            min_intertask_interval=0.75,
                                                            min_intratask_interval=0):
    if not os.path.exists('design_csv_files'):
        os.makedirs('design_csv_files')

    dir_to_create = 'design_csv_files/' + set_label + datetime.now().strftime("%Y%m%d%H%M%S")

    task_filename_list = []
    if not os.path.exists(dir_to_create):
        os.makedirs(dir_to_create)
    for s in subjectclassid_list:

        metaloop_list = []
        metaloop_list.append({
            'LoopFile': 'practice.csv',
            'PreTaskInstructions': 'You will now see two practice trials before you get started.',
            'DisplayS': 4})
        metaloop_filename = dir_to_create + '/metaloop_subclass' + str(s) + '.csv'

        # set the conditions
        condition_design = s % 3
        condition_task_arrangement = (numpy.floor(s/3))%2
        condition_salience_on_first_run = (numpy.floor(s / 6)) % 2
        set_seed = numpy.floor(s/12) #try to keep things constant as far as possible between conditions.


        print (str(s) + ":" + str(set_seed) + ", " + str(condition_salience_on_first_run) + ", " +
               str(condition_task_arrangement) + ","+ str(condition_design) +",")

        random.seed(get_pseudorandom_seed("balancedConstrualSet",set_label,set_seed,0))
        if condition_design == ItcConstrualConditionDesign.RandomCounterbalanced:
            construal_set = get_balanced_construal_set_2(n, 6, n_repeats=2)

        elif [ItcConstrualConditionDesign.BlockDesignConcreteFirst,
              ItcConstrualConditionDesign.BlockDesignAbstractFirst].__contains__(condition_design):
            construal_set = get_construal_set_block(n, 6, condition_design)

        # THERE WILL BE 6 RUNS
        # WITHIN EACH SUBJECT, REWARDSCHEDULE WILL HAVE TO BE CONFLATED WITH THE LEVELS. BUT WE CAN ALTERNATE IT SO IT WON'T BE TOO BAD.
        for r in range(0, 6):

            run_salience_condition = (condition_salience_on_first_run + r) % 2

            citc_task = ItcConstrualTask(n=n, subid=s, day=0, runid=r,
                                         mean_intertask_interval=mean_intertask_interval,
                                         mean_intratask_interval=mean_intratask_interval,
                                         min_intertask_interval=min_intertask_interval,
                                         min_intratask_interval=min_intratask_interval,
                                         salience_condition=run_salience_condition,
                                         construal_mean_rule=ItcConstrualMeanRule.StdDevMethod)
            citc_task.iti_variableamount_interval = [0.40, 0.80]
            citc_task.iti_fixedamount_values = [0.50, 0.60]
            citc_task.task_arrangement=condition_task_arrangement
            citc_task.subjectclass_seed=set_seed

            # raise Exception(
            #    "ALSO NEED TO REMEMBER: HOWEVER MANY CONDITION FILES WE GENERATE, THEY SOMEHOW NEED TO BE STAGGERED SO THEY'RE NOT CONFLATED WITH CONDITION")
            # RandomCounterBalanced
            citc_task.populate_construal_itc_task_with_parameters(construal_set_ids=construal_set[r])
            task_filename = dir_to_create + '/subclass' + str(s) + 'r' + str(r) + '.csv'
            task_filename_list = task_filename_list + [task_filename]

            # "On this block, you will always be choosing between $25 and $30 but the delay to get the money will vary."
            # "On this block, you will always be choosing between getting money in 5 days or 90 days but how much money will vary."
            metaloop_list.append({
                'LoopFile': task_filename,
                'PreTaskInstructions': standard_pre_task_instructions(citc_task.salience_condition, 8),
                'DisplayS': 5
            })


            citc_task.task_data.to_csv(task_filename,
                                       index=False)
        # one trial from each run is set the reward trial from that run. But we only want one reward trial for BOTH runs.
        # so we need to select a particular run to reward.
        random.seed(citc_task.get_pseudorandom_seed("SelectRunReward", True))
        run_to_select = random.sample([0, 1], 1)[0]

        metaloop_list_df = pandas.DataFrame(metaloop_list)
        metaloop_list_df['RewardRun'] = 0
        metaloop_list_df.loc[run_to_select + 1, 'RewardRun'] = 1
        metaloop_list_df.to_csv(metaloop_filename, index=False)

    return task_filename_list


def create_simple_run_itc_construal_mturk_script_set(subjectclassid_list,n,set_label,
    mean_intertask_interval=1,
    mean_intratask_interval=0.3,
    min_intertask_interval=0.75,
    min_intratask_interval=0,
    design=ItcTaskArrangement.TasksInterleaved):
    if not os.path.exists('design_csv_files'):
        os.makedirs('design_csv_files')

    dir_to_create = 'design_csv_files/' + set_label + datetime.now().strftime("%Y%m%d%H%M%S")



    if not os.path.exists(dir_to_create):
        os.makedirs(dir_to_create)
    for s in subjectclassid_list:
        metaloop_list = []
        metaloop_list.append({
            'LoopFile': 'practice.csv',
            'PreTaskInstructions': 'You will now see two practice trials before you get started.',
            'DisplayS':4})
        metaloop_filename = dir_to_create + '/metaloop_subclass' + str(s) + '.csv'

        balanced_construal_set = get_balanced_construal_set_2(n, 2, n_repeats=2)

        for r in range(0,2):
            citc_task = ItcConstrualTask(n=n, subid=s, day=0, runid=r,
                                         mean_intertask_interval=mean_intertask_interval,
                                         mean_intratask_interval=mean_intratask_interval,
                                         min_intertask_interval=min_intertask_interval,
                                         min_intratask_interval=min_intratask_interval)
            citc_task.iti_variableamount_interval=[0.40,0.80]
            citc_task.iti_fixedamount_values = [0.50, 0.60]


            raise Exception("need to pass value in here to set whether to use blocked or interleaved")
            citc_task.populate_construal_itc_task_with_parameters(construal_set_ids=balanced_construal_set[r])
            task_filename= dir_to_create + '/subclass' + str(s) + 'r' + str(r)+'.csv'

            metaloop_list.append({
                'LoopFile': task_filename,
                'PreTaskInstructions': standard_pre_task_instructions(citc_task.salience_condition, 8,
                                                                      constant_condition_amount = "$0.50 and $0.60"),
                'DisplayS': 8
            })

            #raise Exception("this function hasn't been tested yet. remove this exception, but test it.")
            citc_task.task_data.to_csv(task_filename,
                                       index=False)
        #one trial from each run is set the reward trial from that run. But we only want one reward trial for BOTH runs.
        #so we need to select a particular run to reward.
        random.seed(citc_task.get_pseudorandom_seed("SelectRunReward", True))
        run_to_select = random.sample([0, 1], 1)[0]

        metaloop_list_df = pandas.DataFrame(metaloop_list)
        metaloop_list_df['RewardRun']=0
        metaloop_list_df.loc[run_to_select+1,'RewardRun'] = 1
        metaloop_list_df.to_csv(metaloop_filename, index=False)


def create_practice_csv(set_label):
    if not os.path.exists('design_csv_files'):
        os.makedirs('design_csv_files')

    dir_to_create = 'design_csv_files/' + set_label + datetime.now().strftime("%Y%m%d%H%M%S")

    if not os.path.exists(dir_to_create):
        os.makedirs(dir_to_create)

    citc_task = ItcConstrualTask(n=72, subid=1, day=(1), runid=(1))
    citc_task.salience_condition
    citc_task.populate_construal_itc_task_with_parameters()

    citc_task.task_data.to_csv('practice.csv',index=False)

def create_conditions_in_separate_folders(set_label,variableamount_interval,fixedamount_values):
    run_ts=datetime.now().strftime("%Y%m%d%H%M%S")
    #copy the HTML folder
    html_template_folder ='/Users/benjaminsmith/GDrive/neural-construal-level/code/SmithAdaptConstrualITCmTurk/html-template'

    html_create_folder = '/Users/benjaminsmith/GDrive/neural-construal-level/code/SmithAdaptConstrualITCmTurk/html-gen/html' + run_ts

    if not os.path.exists(html_create_folder):
        os.makedirs(html_create_folder)


    random.seed(get_pseudorandom_seed(set_label,"condition_strings",subid=0,day=0,runid=0))
    condition_codes=[''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(8)) for x in range(12)]
    subjects_per_condition = 24

    pandas.DataFrame(condition_codes).to_csv (html_create_folder + "_fulllist.csv")

    for i, cc in enumerate(condition_codes):
        sub_id_list=[1+i*subjects_per_condition+x for x in range(subjects_per_condition)]
        sub_class_id=[x for x in range(24)]
        #create the HTML folder
        shutil.copytree(html_template_folder, html_create_folder + "/" + cc)
        #create a folder with
        create_arbitrary_run_in_custom_folder(html_create_folder+"/" + cc + '/resources/', 'design_csv_files',
                                              sub_id_list,sub_class_id,
                                              condition=i,
                                              n=20,set_label='set_label',
                                              n_runs=4,
                                            mean_intertask_interval=1.0,
                                            mean_intratask_interval=0.3,
                                            min_intertask_interval=0.75,
                                            min_intratask_interval=0.2,
                                            variableamount_interval = variableamount_interval,
                                            fixedamount_values = fixedamount_values,
                                              project_base_path=html_create_folder+"/" + cc
                                              )#,
                                              #constant_condition_amount='$0.50 and $0.60')


def create_conditions_in_separate_folders_varyrewards(set_label):
    run_ts=datetime.now().strftime("%Y%m%d%H%M%S")
    #copy the HTML folder
    html_template_folder ='/Users/benjaminsmith/GDrive/neural-construal-level/code/SmithAdaptConstrualITCmTurk/html-template'

    html_create_folder = '/Users/benjaminsmith/GDrive/neural-construal-level/code/SmithAdaptConstrualITCmTurk/html-gen/html' + run_ts

    if not os.path.exists(html_create_folder):
        os.makedirs(html_create_folder)


    random.seed(get_pseudorandom_seed(set_label,"condition_strings",subid=0,day=0,runid=0))
    condition_codes=[''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(8)) for x in range(12)]
    subjects_per_condition = 24

    pandas.DataFrame(condition_codes).to_csv (html_create_folder + "_fulllist.csv")

    for i, cc in enumerate(condition_codes):
        sub_id_list=[1+i*subjects_per_condition+x for x in range(subjects_per_condition)]
        sub_class_id=[x for x in range(24)]
        #create the HTML folder
        shutil.copytree(html_template_folder, html_create_folder + "/" + cc)
        #create a folder with
        create_arbitrary_run_in_custom_folder_varyrewards(html_create_folder+"/" + cc + '/resources/', 'design_csv_files',
                                              sub_id_list,sub_class_id,
                                              condition=i,
                                              n=20,set_label='set_label',
                                              n_runs=4,
                                            mean_intertask_interval=1,
                                            min_intertask_interval=0.75,
                                            mean_intratask_interval=0.6,
                                            min_intratask_interval=0.4,
                                              project_base_path=html_create_folder+"/" + cc
                                              )#,
                                              #constant_condition_amount='$0.50 and $0.60')

def create_arbitrary_run_in_custom_folder_varyrewards(project_resource_path,rel_folder, subject_unique_id, subject_classid_list,n,set_label,
                                                        n_runs=6,
                                                        mean_intertask_interval=1,
                                                        mean_intratask_interval=0.3,
                                                        min_intertask_interval=0.75,
                                                        min_intratask_interval=0,
                                                        design=ItcTaskArrangement.TasksInterleaved,
                                                        condition=None,
                                                      project_base_path=None):

    #two rewardsets
    hypothetical_constant_condition_amount = '$20 and $30'
    hypothetical_fixedamount_values = [20, 30]
    hypothetical_variableamount_interval = [20, 40]
    real_constant_condition_amount = '$0.40 and $0.60'
    real_fixedamount_values = [0.40, 0.60]
    real_variableamount_interval = [0.40, 0.80]

    if not os.path.exists(project_resource_path+rel_folder):
        os.makedirs(project_resource_path+rel_folder)

    if condition is None:
        condition = subject_classid_list

    task_filename_list = []
    for s in subject_classid_list:
        # set the conditions
        condition_design = condition % 3
        condition_task_arrangement = (numpy.floor(condition / 3)) % 2
        condition_reward_schedule = (numpy.floor(condition / 6)) % 2

        if condition_reward_schedule == RewardSchedule.LargeHypothetical:
            practice_file='practice_largeamounts.csv'
        elif condition_reward_schedule == RewardSchedule.SmallReal:
            practice_file = 'practice.csv'
        metaloop_list = []
        metaloop_list.append({
            'LoopFile': practice_file,
            'PreTaskInstructions': 'You will now see two practice trials before you get started.',
            'DisplayS': None})
        metaloop_filename = rel_folder + '/metaloop_subclass' + str(s) + '.csv'


        #this will be set by subject*group
        condition_salience_on_first_run = numpy.floor((condition) / 6 + s) % 2

        print (str(s) + ":" + str(condition_reward_schedule) + ", " +
               str(condition_task_arrangement) + ","+ str(condition_design) + ","+ str(condition_salience_on_first_run) +",")

        random.seed(get_pseudorandom_seed("balancedConstrualSet",set_label,s,0))
        if condition_design == ItcConstrualConditionDesign.RandomCounterbalanced:
            construal_set = get_balanced_construal_set_2(n, 4, n_repeats=2,monotonic_construal_sets_only=True)

        elif [ItcConstrualConditionDesign.BlockDesignConcreteFirst,
              ItcConstrualConditionDesign.BlockDesignAbstractFirst].__contains__(condition_design):
            construal_set = get_construal_set_block(n, 4, condition_design,monotonic_construal_sets_only=True)

        # THERE WILL BE 6 RUNS
        # WITHIN EACH SUBJECT, REWARDSCHEDULE WILL HAVE TO BE CONFLATED WITH THE LEVELS. BUT WE CAN ALTERNATE IT SO IT WON'T BE TOO BAD.
        for r in range(0, n_runs):
            run_salience_condition = (condition_salience_on_first_run + r) % 2

            citc_task = ItcConstrualTask(n=n, subid=s, day=0, runid=r,
                                         mean_intertask_interval=mean_intertask_interval,
                                         mean_intratask_interval=mean_intratask_interval,
                                         min_intertask_interval=min_intertask_interval,
                                         min_intratask_interval=min_intratask_interval,
                                         salience_condition=run_salience_condition,
                                         construal_mean_rule=ItcConstrualMeanRule.StdDevMethod)

            #citc_task.iti_fixedamount_values = [25, 30]
            #citc_task.iti_variableamount_interval = [20, 40]
            citc_task.iti_fixeddelay_values = [5, 50]

            if condition_reward_schedule==RewardSchedule.LargeHypothetical:
                citc_task.iti_variableamount_interval = hypothetical_variableamount_interval#[0.40, 0.80]
                citc_task.iti_fixedamount_values = hypothetical_fixedamount_values#[0.50, 0.60]
                constant_condition_amount=hypothetical_constant_condition_amount
            elif condition_reward_schedule==RewardSchedule.SmallReal:
                citc_task.iti_variableamount_interval = real_variableamount_interval  # [0.40, 0.80]
                citc_task.iti_fixedamount_values = real_fixedamount_values  # [0.50, 0.60]
                constant_condition_amount = real_constant_condition_amount
                #need to change
                replace_text_in_file(
                    script_to_fix_filepath=project_base_path+"/customjs/construal_itc_logic.js",
                    find_text="var reward_condition=REWARD_CONDITION_LARGE_HYPOTHETICAL;",
                    replace_text="var reward_condition=REWARD_CONDITION_SMALL_REAL;"
                                     )


            citc_task.condition_design = condition_design
            citc_task.task_arrangement=condition_task_arrangement
            citc_task.subjectclass_seed=s

            # raise Exception(
            #    "ALSO NEED TO REMEMBER: HOWEVER MANY CONDITION FILES WE GENERATE, THEY SOMEHOW NEED TO BE STAGGERED SO THEY'RE NOT CONFLATED WITH CONDITION")
            # RandomCounterBalanced
            citc_task.populate_construal_itc_task_with_parameters(construal_set_ids=construal_set[r])
            task_filename = rel_folder + '/subclass' + str(s) + 'r' + str(r) + '.csv'
            task_filename_list = task_filename_list + [task_filename]

            # "On this block, you will always be choosing between $25 and $30 but the delay to get the money will vary."
            # "On this block, you will always be choosing between getting money in 5 days or 90 days but how much money will vary."
            metaloop_list.append({
                'LoopFile': task_filename,
                'PreTaskInstructions': standard_pre_task_instructions(citc_task.salience_condition, delay=None, constant_condition_amount=constant_condition_amount),
                'DisplayS': None
            })


            citc_task.task_data.to_csv(project_resource_path+task_filename,
                                       index=False)
        # one trial from each run is set the reward trial from that run. But we only want one reward trial for BOTH runs.
        # so we need to select a particular run to reward.
        random.seed(citc_task.get_pseudorandom_seed("SelectRunReward", True))
        run_to_select = random.sample([0, 1], 1)[0]

        metaloop_list_df = pandas.DataFrame(metaloop_list)
        metaloop_list_df['RewardRun'] = 0
        metaloop_list_df.loc[run_to_select + 1, 'RewardRun'] = 1
        metaloop_list_df.to_csv(project_resource_path+metaloop_filename, index=False)

    return task_filename_list

####replace text in a file, using specified find text and applying certain escape functions.
def replace_text_in_file(script_to_fix_filepath,find_text,replace_text):
    #open the file we're editing
    script_text = open(script_to_fix_filepath).read()
    #find_text = open(find_replace_location + frpair[0]).read()
    #escape
    find_text_re=re.escape(" ".join(find_text.split())).replace('\\ ','\s+')
    #replace_text=open(file_to_edit).read()
    #search for location to replace
    textLocation = re.search(find_text_re, script_text)
    print '----'+'\n'+find_text + "\nat " + str(textLocation) + "->\n"+replace_text +'\n----\n'
    script_text=re.sub(find_text_re, replace_text, script_text)
    f = open(script_to_fix_filepath, 'w')
    f.write(script_text)
    f.close()



def create_arbitrary_run_in_custom_folder(project_resource_path,rel_folder, subject_unique_id, subject_classid_list,n,set_label,
    n_runs=6,
    mean_intertask_interval=1,
    mean_intratask_interval=0.3,
    min_intertask_interval=0.75,
    min_intratask_interval=0,
    design=ItcTaskArrangement.TasksInterleaved,
    condition=None,
    constant_condition_amount='$25 and $30',
    variableamount_interval=[0.40, 0.80],
    fixedamount_values=[0.50, 0.60]):
    if not os.path.exists(project_resource_path+rel_folder):
        os.makedirs(project_resource_path+rel_folder)

    if condition is None:
        condition = subject_classid_list

    task_filename_list = []
    for s in subject_classid_list:

        metaloop_list = []
        metaloop_list.append({
            'LoopFile': 'practice.csv',
            'PreTaskInstructions': 'You will now see two practice trials before you get started.',
            'DisplayS': None})
        metaloop_filename = rel_folder + '/metaloop_subclass' + str(s) + '.csv'

        # set the conditions
        condition_design = condition % 3
        condition_task_arrangement = (numpy.floor(condition/3))%2
        condition_salience_on_first_run = (numpy.floor(condition / 6)) % 2

        print (str(s) + ":" + str(condition_salience_on_first_run) + ", " +
               str(condition_task_arrangement) + ","+ str(condition_design) +",")

        random.seed(get_pseudorandom_seed("balancedConstrualSet",set_label,s,0))
        if condition_design == ItcConstrualConditionDesign.RandomCounterbalanced:
            construal_set = get_balanced_construal_set_2(n, 4, n_repeats=2,monotonic_construal_sets_only=True)

        elif [ItcConstrualConditionDesign.BlockDesignConcreteFirst,
              ItcConstrualConditionDesign.BlockDesignAbstractFirst].__contains__(condition_design):
            construal_set = get_construal_set_block(n, 4, condition_design,monotonic_construal_sets_only=True)

        # THERE WILL BE 6 RUNS
        # WITHIN EACH SUBJECT, REWARDSCHEDULE WILL HAVE TO BE CONFLATED WITH THE LEVELS. BUT WE CAN ALTERNATE IT SO IT WON'T BE TOO BAD.
        for r in range(0, n_runs):
            run_salience_condition = (condition_salience_on_first_run + r) % 2

            citc_task = ItcConstrualTask(n=n, subid=s, day=0, runid=r,
                                         mean_intertask_interval=mean_intertask_interval,
                                         mean_intratask_interval=mean_intratask_interval,
                                         min_intertask_interval=min_intertask_interval,
                                         min_intratask_interval=min_intratask_interval,
                                         salience_condition=run_salience_condition,
                                         construal_mean_rule=ItcConstrualMeanRule.StdDevMethod)
            citc_task.iti_variableamount_interval = variableamount_interval#[0.40, 0.80]
            citc_task.iti_fixedamount_values = fixedamount_values#[0.50, 0.60]
            citc_task.condition_design = condition_design
            citc_task.task_arrangement=condition_task_arrangement
            citc_task.subjectclass_seed=s

            # raise Exception(
            #    "ALSO NEED TO REMEMBER: HOWEVER MANY CONDITION FILES WE GENERATE, THEY SOMEHOW NEED TO BE STAGGERED SO THEY'RE NOT CONFLATED WITH CONDITION")
            # RandomCounterBalanced
            citc_task.populate_construal_itc_task_with_parameters(construal_set_ids=construal_set[r])
            task_filename = rel_folder + '/subclass' + str(s) + 'r' + str(r) + '.csv'
            task_filename_list = task_filename_list + [task_filename]

            # "On this block, you will always be choosing between $25 and $30 but the delay to get the money will vary."
            # "On this block, you will always be choosing between getting money in 5 days or 90 days but how much money will vary."
            metaloop_list.append({
                'LoopFile': task_filename,
                'PreTaskInstructions': standard_pre_task_instructions(citc_task.salience_condition, delay=None, constant_condition_amount=constant_condition_amount),
                'DisplayS': None
            })


            citc_task.task_data.to_csv(project_resource_path+task_filename,
                                       index=False)


        # one trial from each run is set the reward trial from that run. But we only want one reward trial for BOTH runs.
        # so we need to select a particular run to reward.
        random.seed(citc_task.get_pseudorandom_seed("SelectRunReward", True))
        run_to_select = random.sample([0, 1], 1)[0]

        metaloop_list_df = pandas.DataFrame(metaloop_list)
        metaloop_list_df['RewardRun'] = 0
        metaloop_list_df.loc[run_to_select + 1, 'RewardRun'] = 1
        metaloop_list_df.to_csv(project_resource_path+metaloop_filename, index=False)

    return task_filename_list



def create_two_independent_runs_itc_construal_script_set(subid_list,day_count,run_count,n,set_label,
                                                         practice_as_separate_run=False,
                                                         mean_intertask_interval=2,
                                                         mean_intratask_interval=1,
                                                         min_intertask_interval=0.5,
                                                         min_intratask_interval=0.5,
                                                         require_balance_from_trial=None):
    if not os.path.exists('design_csv_files'):
        os.makedirs('design_csv_files')

    dir_to_create = 'design_csv_files/' + set_label + datetime.now().strftime("%Y%m%d%H%M%S")

    if not os.path.exists(dir_to_create):
        os.makedirs(dir_to_create)

    task_filename_list = []
    for s in subid_list:
        print s
        for d in range(0,day_count):
            random.seed(get_pseudorandom_seed('ConstrualSet','generic',s,d))
            if d==0:
                balanced_construal_set = get_balanced_construal_set_2([n,n,12,12],4,n_repeats=2,require_balance_from_trial=require_balance_from_trial)
            else:
                balanced_construal_set = get_balanced_construal_set_2([n, n, 4, 4], 4,n_repeats=2,require_balance_from_trial=require_balance_from_trial)

            r_set=range(1,run_count+1)
            # if practice_as_separate_run:
            #     r_set=r_set+['practice1','practice2']
            #and once to create real sets. ALL need to be considered within the total number of runs this subject does.
            for r in r_set:
                #note that here, the meta-loop only contains one block. That's because we're doing blocks as separate runs.
                metaloop_list = []
                if practice_as_separate_run==False:
                    metaloop_list.append({
                        'LoopFile': 'practice.csv',
                        'PreTaskInstructions': 'You will now see two preview trials before you get started.\\n'})

                citc_task = ItcConstrualTask(n=n, subid=s, day=(d+1), runid=(r),
                 mean_intertask_interval=mean_intertask_interval,
                 mean_intratask_interval=mean_intratask_interval,
                 min_intertask_interval=min_intertask_interval,
                 min_intratask_interval=min_intratask_interval,
                 require_balance_from_trial=require_balance_from_trial)
                #citc_task.salience_condition
                citc_task.populate_construal_itc_task_with_parameters(construal_set_ids= balanced_construal_set[r-1])

                metaloop_filename = dir_to_create + '/metaloop_sub' + str(s) + 'd' + str(d+1) + 'r' + str(r) +'.csv'
                task_filename= dir_to_create + '/sub' + str(s) + 'd' + str(d+1) + 'r' + str(r) +'.csv'
                task_filename_list = task_filename_list + [task_filename]

                metaloop_list.append({
                        'LoopFile': task_filename,
                        'PreTaskInstructions': standard_pre_task_instructions(citc_task.salience_condition, 10)
                    })


                metaloop_list_df = pandas.DataFrame(metaloop_list)
                metaloop_list_df.to_csv(metaloop_filename,index=False)

                citc_task.task_data.to_csv(task_filename,index=False)

            # loop once to create practice set (which includes TWO runs)
            metaloop_list_practice = []
            if practice_as_separate_run:
                for r in range(1,3):
                    if d==0:
                        n_trials=12
                    else:
                        n_trials=4
                    #note that here, because we're doing a meta-loop with TWO runs.
                    #we have to do the same n in order to make the randomization work; if we don't, we might get some practice trials that are the same as the real trials.
                    citc_task = ItcConstrualTask(n=n_trials, subid=s, day=(d+1), runid=(r+2))
                    #citc_task.salience_condition
                    citc_task.populate_construal_itc_task_with_parameters(construal_set_ids=balanced_construal_set[r-1+2])

                    #because this is a practice round, truncate the number of trials
                    # if d==0:#on the first day do more trials
                    #     citc_task.task_data=citc_task.task_data[0:12]
                    # else:#on subsequent days, just a few.
                    #     citc_task.task_data = citc_task.task_data[0:4]
                    metaloop_filename = dir_to_create + '/metaloop_sub' + str(s) + 'd' + str(d+1) + 'rpractice.csv'
                    task_filename= dir_to_create + '/sub' + str(s) + 'd' + str(d+1) + 'rpractice' + str(r) +'.csv'

                    metaloop_list_practice.append({
                        'LoopFile': task_filename,
                        'PreTaskInstructions': standard_pre_task_instructions(citc_task.salience_condition, 10)
                    })

                    citc_task.task_data.to_csv(task_filename, index=False)


                metaloop_list_df = pandas.DataFrame(metaloop_list_practice)
                metaloop_list_df.to_csv(metaloop_filename,index=False)

    return task_filename_list







def create_itc_construal_script_set(subid_list,day_count,run_count,n,set_label):
    if not os.path.exists('design_csv_files'):
        os.makedirs('design_csv_files')

    dir_to_create = 'design_csv_files/' + set_label + datetime.now().strftime("%Y%m%d%H%M%S")

    metaloop_list=[]
    metaloop_list.append({
        'LoopFile':'practice.csv',
        'PreTaskInstructions':'You will now see two practice trials before you get started.'})
    if not os.path.exists(dir_to_create):
        os.makedirs(dir_to_create)
    for s in subid_list:
        print s
        for d in range(0,day_count):
            for r in range(0,run_count):
                citc_task = ItcConstrualTask(n=n, subid=s, day=(d+1), runid=(r+1))

                citc_task.populate_construal_itc_task_with_parameters()
                task_filename= dir_to_create + '/sub' + str(s) + 'd' + str(d+1) + 'r' + str(r+1) +'.csv'

                metaloop_list.append({
                'LoopFile':task_filename,
                'PreTaskInstructions':standard_pre_task_instructions(citc_task.salience_condition,10)
                })


                citc_task.task_data.to_csv(task_filename,
                                           index=False)


#create_itc_construal_script_set([1,2,3,4,5],2,2,72,'test_citcs')

def standard_pre_task_instructions(salience_condition,delay,constant_condition_amount='$20 and $30'):
    if salience_condition == ItcSalienceCondition.Amount:  # SALIENCE_CONDITION_AMOUNT:
        varying_condition = 'amount of money'
        constant_condition = 'money in 5 days or 50 days'
    elif salience_condition == ItcSalienceCondition.Delay:  # SALIENCE_CONDITION_DELAY:
        varying_condition = 'delay to get the money'
        constant_condition = constant_condition_amount

    fulltext = (
        ' Are you ready?\\nIn this set of choices,\\nyou will always choose between\\ngetting ' + constant_condition +
        ',\\nbut the ' + varying_condition + ' will go up or down each time.')
    if delay!=None:
        fulltext = fulltext + ('\\nThis screen displays for ' + str(delay) + ' seconds.')

    return(fulltext)
