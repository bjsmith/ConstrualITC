from ItcConstrualTaskManager import *



mturk_files = create_itc_construal_mturk_script_set(
    range(0,12),n=12,set_label='testcase_mturk',
    mean_intertask_interval=1,
    mean_intratask_interval=0.3,
    min_intertask_interval=0.75,
    min_intratask_interval=0)