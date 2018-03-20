import pandas

construal_data = pandas.read_csv('spunt_dataset/data.csv')
construal_seeker = pandas.read_csv('spunt_dataset/seeker.csv')
#put the data in order
cdata_in_order = construal_data.loc[construal_seeker.Stimulus]

#now check how different portions of this add up in terms of....

pandas.concat([cdata_in_order.iloc[0:72].mean(0),cdata_in_order.iloc[72:144].mean(0),
               cdata_in_order.iloc[0:32].mean(0),cdata_in_order.iloc[72:(72+32)].mean(0)],1)

#create two random selections of trials
import random

def get_balanced_construal_set(n_trials=32,n_runs=2):
    #construal_seeker = pandas.read_csv('spunt_dataset/seeker.csv')
    construal_data = pandas.read_csv('spunt_dataset/data.csv')

    all_db_means=construal_data.mean(0)


    candidate_set_qualifies=False
    while candidate_set_qualifies==False:
        #get a random sample of all of the construal trials
        whole_sample=random.sample(range(0,143),n_trials*n_runs)
        #benefit of the doubt
        candidate_set_qualifies=True
        #iterate through each of the portions in our sample
        candidate_set=[]
        for portion_i in range(0,n_runs):

            #portion_i=0
            sample_portion=whole_sample[(portion_i*n_trials):((portion_i+1)*n_trials)]
            candidate_set.append(sample_portion)
            #check to see that portion's balance score

            differences=abs(((all_db_means - construal_data.iloc[sample_portion].mean(0)) / all_db_means)[[1, 2, 7, 15]])
            #print differences
            #each portion should differ by less than 2% on every measure from the population.
            if any(differences>0.02):
                #repeat
                candidate_set_qualifies=False
                break
    #we got to the end; that means we found a good set!
    return candidate_set
        #if it is sufficient, pass the selection out.

print get_balanced_construal_set()
