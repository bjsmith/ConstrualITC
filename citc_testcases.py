from ItcConstrualTask import *
from pandas import *
#
citc_task = ItcConstrualTask(n=72, subid=201, day=1, runid=1)
citc_task.populate_construal_itc_task_with_parameters()
citc_task.task_data.to_csv('test_task_output_sub201d1r1.csv')

citc_task = ItcConstrualTask(n=72, subid=202, day=1, runid=1)
citc_task.populate_construal_itc_task_with_parameters()
citc_task.task_data.to_csv('test_task_output_sub202d1r1.csv')

citc_task = ItcConstrualTask(n=72, subid=202, day=2, runid=1)
citc_task.populate_construal_itc_task_with_parameters()
citc_task.task_data.to_csv('test_task_output_sub202d2r1.csv')
citc_task = ItcConstrualTask(n=72, subid=202, day=2, runid=2)
citc_task.populate_construal_itc_task_with_parameters()
citc_task.task_data.to_csv('test_task_output_sub202d2r2.csv')

citc_task = ItcConstrualTask(n=72, subid=203, day=2, runid=2)
citc_task.populate_construal_itc_task_with_parameters()
citc_task.task_data.to_csv('test_task_output_sub203d2r2.csv')