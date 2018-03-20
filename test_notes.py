import pandas
from ItcConstrualTaskManager import *
#we will actually need to test everything as a result of all of this.

#changes to the script potentially changes things for everyone so we need a test script to
#test all the possible use cases.

test_range = range(42000,42006)
#These are:



fMRI_files=create_two_independent_runs_itc_construal_script_set(
    test_range,3,2,n=60,set_label='testcase_fMRI',practice_as_separate_run=True,
    mean_intertask_interval=2,
    mean_intratask_interval=2,
    min_intertask_interval=1,
    min_intratask_interval=1,
    require_balance_from_trial=[24,30,36,42,48,54,60])#[30,42,54,60])



salienceConditionList_fMRI=[]
construal_condition_count_fMRI = []
for f in fMRI_files:
    print f
    df = pandas.read_csv(f)
    print str(df.ITI.mean(0)) + ", " + str(df.TaskInterval.mean(0))
    assert(df.ITI.mean(0)>1.9 and df.ITI.mean(0)<2.1)
    assert (df.TaskInterval.mean(0) > 1.9 and df.TaskInterval.mean(0) < 2.1)


    amountSalient=(df.SSamount.hasnans and len(df.LLamount.unique())>1 and len(df.LLdelay.unique())==1 and len(df.SSdelay.unique())==1)
    delaySalient=(df.SSdelay.hasnans and len(df.LLdelay.unique()) > 1 and len(df.LLamount.unique())==1 and len(df.SSamount.unique())==1)
    print amountSalient
    print delaySalient
    # test that this is either Amount Salient or DelaySalient condition.
    #assert(amountSalient != delaySalient)
    if amountSalient != delaySalient:
        print amountSalient
        print delaySalient

    if amountSalient:
        print "amountSalient"
        salienceConditionList_fMRI = salienceConditionList_fMRI + ["amountSalient"]
        print df.LLamount.mean(0)
        assert (df.LLamount.mean(0)<30*1.1 and df.LLamount.mean(0) >30*0.9)

    if delaySalient:
        print "delaySalient"
        salienceConditionList_fMRI = salienceConditionList_fMRI + ["delaySalient"]
        print df.SSdelay.mean(0)
        assert (df.SSdelay.mean(0) > 4 and df.SSdelay.mean(0) < 5)

    #construal.
    cd=get_construal_data_with_means()
    construal_condition_count_fMRI = construal_condition_count_fMRI + [len(unique(df.Construal_Condition))]
    for r_n in range(0,len(df.Construal_Condition)/2):
        if df.Construal_Condition[r_n*2]!=df.Construal_Condition[r_n*2+1]:
            print df.Construal_Condition
            assert(df.Construal_Condition[r_n*2]==df.Construal_Condition[r_n*2+1])

print construal_condition_count_fMRI # should be all 6's
assert ([x==6 for x in construal_condition_count_fMRI])
print salienceConditionList_fMRI #should be mix of both.
assert (salienceConditionList_fMRI.count("delaySalient")==salienceConditionList_fMRI.count("amountSalient"))

#- mturk task (the three conditions; we haven't got the interleaved setup yet)
#   - each three conditions come out correctly.
mturk_files = create_itc_construal_mturk_script_set_interleaveddesign(
    test_range,n=12,set_label='testcase_mturk',
    mean_intertask_interval=1,
    mean_intratask_interval=0.3,
    min_intertask_interval=0.75,
    min_intratask_interval=0)
#- scanner task
#   should be able to compare to last time because this is supposed to generate the same value each time due to the use of random seeds.
#   should run 2 subjects, 3 days, 2 runs, plus the random versions and make sure that:
#   - construal appears in pairs
#   - the two ITI means are meaned properly
#   - the SS and LL values are meaned properly
#   - we have the right balance between amount and delay salience

salienceConditionList=[]
construal_condition_count = []
for f in mturk_files:
    print f
    df = pandas.read_csv(f)
    print str(df.ITI.mean(0)) + ", " + str(df.TaskInterval.mean(0))
    assert(df.ITI.mean(0)>0.9 and df.ITI.mean(0)<1.1)
    assert (df.TaskInterval.mean(0) > 0.2 and df.TaskInterval.mean(0) < 0.4)


    amountSalient=(df.SSamount.hasnans and len(df.LLamount.unique())>1 and len(df.LLdelay.unique())==1 and len(df.SSdelay.unique())==1)
    delaySalient=(df.SSdelay.hasnans and len(df.LLdelay.unique()) > 1 and len(df.LLamount.unique()) == 1 and len(
            df.SSamount.unique()) == 1)
    # test that this is either Amount Salient or DelaySalient condition.
    #assert(amountSalient != delaySalient)
    if amountSalient != delaySalient:
        print amountSalient
        print delaySalient

    if amountSalient:
        print "amountSalient"
        salienceConditionList = salienceConditionList + ["amountSalient"]
        print df.LLamount.mean(0)
        assert (df.LLamount.mean(0)>0.55 and df.LLamount.mean(0) <0.65)

    if delaySalient:
        print "delaySalient"
        salienceConditionList = salienceConditionList + ["delaySalient"]
        print df.SSdelay.mean(0)
        assert (df.SSdelay.mean(0) > 4 and df.SSdelay.mean(0) < 5)

    #construal.
    cd=get_construal_data_with_means()
    construal_condition_count = construal_condition_count + [len(unique(df.Construal_Condition))]
    for r_n in range(0,len(df.Construal_Condition)/2):
        if df.Construal_Condition[r_n*2]!=df.Construal_Condition[r_n*2+1]:
            print df.Construal_Condition
            assert(df.Construal_Condition[r_n*2]==df.Construal_Condition[r_n*2+1])

print salienceConditionList
#we should have some a consecutive series of blocks that have 6 construal conditions and TWO consecutive series of blocks that have only 1 construal condition.
assert salienceConditionList.count(6)*2==salienceConditionList.count(1)
print construal_condition_count
assert construal_condition_count.count("amountSalient")==salienceConditionList.count("delaySalient")
    #   - we have the right balance between amount and delay salience
    #is this amount salience or delay salience?



