from ItcConstrualTask import *
n=36;s=1;d=0;r=0
balanced_construal_set = get_balanced_construal_set_2([n,n,12,12],4,n_repeats=2,require_balance_from_trial=[24,36])


citc_task = ItcConstrualTask(n=n, subid=s, day=(d + 1), runid=(r),
                             mean_intertask_interval=2,
                             mean_intratask_interval=2,
                             min_intertask_interval=0.5,
                             min_intratask_interval=0.5,
                             require_balance_from_trial=[24,36])
citc_task.task_arrangement=ItcTaskArrangement.TasksBlocked
citc_task.populate_construal_itc_task_with_parameters(construal_set_ids= balanced_construal_set[0])

citc_task.task_data.to_csv("test_tasksblocked.csv")