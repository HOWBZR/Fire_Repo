
import pandas as pd
import numpy as np
from imblearn.over_sampling import RandomOverSampler







def over_sampler(df,column_name):
    ''' Params: df,column_name="string" 
    The function will oversample based on the class you want to match. Save as df and then use train_test_split to cut down 
    the data.
      '''
    
    df=df.copy()
    # gathering the classes/counts and respective percentages to convert to dictionary for easy accesiblilty later
    classes = df[column_name].value_counts(normalize=False).index.tolist()
    counts = df[column_name].value_counts(normalize=False).tolist()
    percentages = (round(df[column_name].value_counts(normalize=True)*100,3)).tolist()
    diction=dict(zip(classes,counts))
    
    # getting input data so we can quckly iterate
    input_user = int(input('What class do we want from needs to be an INT(our case ~ 0-9)?'))
    count_goal = diction.get(input_user)
    # creating list of dataframes of randomly oversample observations 
    #            Note: not usable for time series w/o adjustment as to what df passed in 
    df_list = []
    for k,v in diction.items():
        # ensuring oversampling classes w/counts below the designated input class
        if v < count_goal:
            n_samples=count_goal-v
            rows_to_append = df[df[column_name]==k].sample(n =n_samples,replace=True,random_state=42) # oversampling here
            df_list.append(rows_to_append)

    # merging list of dfs into on whole df 
    samples_df = pd.concat(df_list)
    # merging dataframe of oversamples obs to original passed in df to return
    over_sample_class =pd.concat([df,samples_df])
    
    return over_sample_class


        
# use case example
# over_class5 = over_sampler(dummified_1,'fire_class')
# print(over_class5.shape[0])
# over_class5['fire_class'].value_counts()
