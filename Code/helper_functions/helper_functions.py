

# general data analysis functions
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#importing metrics
from sklearn import metrics
from sklearn.metrics import mean_squared_error, mean_absolute_error,max_error
#unsure
# from scipy import stats


#function to create a dataframe of specific characteristics

#Note: The above function was built off inspiration from a more visually appealing percent formula that I was constantly creating so created this function
# so I can easily just filter based on characteristics I was most interested. I will use this data frame while I perform EDA.
#[Stack Overflow Inspiration-'find percent missing values']
# link: (https://stackoverflow.com/questions/51070985/find-out-the-percentage-of-missing-values-in-each-column-in-the-given-dataset)
def character_df(dataframe):
    ''' Argument: dataframe= 'whatever data frame you select'   ,
    This function returns a dataframe of null counts per column, percent missing, and if categorical its unique values.
    '''
    #create a column of null counts per feature
    isnull_cnt    = dataframe.isnull().sum()
    only_isnull_cnt=[isnull_cnt[null_cnt] for null_cnt in range(len(isnull_cnt))]
    # looking at dtypes
    charac_append = list(dataframe.dtypes)
    #create a column of percentage missing per features
    prct_missing = round(dataframe.isnull().sum() * 100 / len(dataframe),2)
    only_prct=[prct_missing[percent] for percent in range(len(prct_missing))]

    # create a column that lists different variables held within categorical variables
    cat_list=[dataframe[column].unique() if str( dataframe[column].dtype )=='object' else 'not cat.'  for column in dataframe  ]

    #create a df from all the series outputed above
    df_characteristics = pd.DataFrame({'column_name':dataframe.columns ,'null_count': only_isnull_cnt, 'percent_missing': only_prct, 'categorical_unique': cat_list,'dtypes':charac_append})

    return df_characteristics

# Original Code Inspiration df['z'].fillna(dff.groupby('x')['z'].transform('mean'))
# A function to utilize fillna and transform function to quickly replace NaN values within a dataframe
def fillna_centrl_tendcy(dataframe,change_column,groupby_column,function):
    '''
    Arguments: dataframe = df ,   change_column='column to change', groupby_column = 'column_name' , function = 'mean'
    Note about Function:
    Function to use for transforming the data.
    If a function, must either work when passed a DataFrame or when passed to DataFrame.apply. If func is both list-like and dict-like, dict-like behavior takes precedence(from transform documentation).
    The function allows for easy fills of na given a dataframe, column to group by, and the function you want to perform('mean','mode','median'),'''
    dataframe[change_column] = dataframe[change_column].groupby( dataframe[groupby_column] ).transform(function)
    return dataframe




# function to print out quick null summary details
def null_reminders(dataframe,column_name,features_to_drop,value_cnt):
    ''' dataframe = df, column_name = 'name', featires_to_drop = list of columns names not wanted , value_cnt=='Yes'
    Note: returns a seperate dataframe
    '''
    # providing reminder of what needs to be replaced/filled
    print('is null sum: ',dataframe[column_name].isnull().sum() )

    #checking if value counts are wanted
    if value_cnt=='Yes':
        print(dataframe[column_name].value_counts() )

    #filter to peek at df potentially looking for a method to fill these 55 observations
    df_column_null = dataframe[   dataframe[column_name].isnull()   ].drop(columns=features_to_drop)
    print('df_column_ shape',df_column_null.shape)
    return df_column_null


# medium article inspiration for function: https://hersanyagci.medium.com/detecting-and-handling-outliers-with-pandas-7adbfcd5cad8#:~:text=As%20you%20can%20see%20this,best%20way%20to%20see%20outliers.
# the function below is to return columns and indexes of outliers based on the Turkey rule (described in article)
# the purpose is to reduce the sifting of each feature'
def turkey_outliers(datframe):
    # want to make sure only looking at numerical catergories (https://stackoverflow.com/questions/25039626/how-do-i-find-numeric-columns-in-pandas)
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

    newdf = datframe.select_dtypes(include=numerics)

    # column names for two seperate dataframes and their respective outlier index lists
    column_name=[]
    column_name2=[]
    lwr_outlier_index=[]
    upr_outlier_index=[]

    #passes through each column in out numerical data frame
    for column in newdf.columns:
        # quartile calculations from each column
        Q25 = float(newdf[column].quantile(0.25))
        Q75 = float(newdf[column].quantile(0.75))

        # establishing bounds for reference based on Turkey's rule to detect outliers from medium article above
        IQR = Q75 - Q25
        acceptable_lower = Q25 - 1.25*(IQR)
        acceptable_upper = Q75 + 1.25*(IQR)

        # storing actual min/max values for outlier evaluation below
        min_series = newdf[column].min()
        max_series = newdf[column].max()

        # checking if the max and mins per column are greater than the acceptable bounds above
        if min_series > acceptable_lower:
            # appends the index of the first minimum value in the dataframe to the list
            column_name.append(column)
            lwr_outlier_index.append(newdf[column].idxmin(axis=0))
        if max_series > acceptable_upper:
            # appends the index of the first max value in the dataframe to the list
            column_name2.append(column)
            upr_outlier_index.append(newdf[column].idxmax())


    # creates data frames for each case of outliers to view column_names to minimize searching through all 65 features
    lwr_out_dict = {'column_name':column_name,'lwr_min_outlr_indx':lwr_outlier_index}
    lwr_out_df = pd.DataFrame(lwr_out_dict,columns=['column_name','lwr_min_outlr_indx'])

    upr_out_dict = {'column_name':column_name2,'upr_max_outlr_index':upr_outlier_index}
    upr_out_df = pd.DataFrame(upr_out_dict,columns=['column_name','upr_max_outlr_index'])

    return lwr_out_df, upr_out_df


# this is a mertic function used to quickly append to a an exisitng dataframe to easily compare iterations
def metric_reg(model,X_train,y_train,X_test,y_test):
    #regular R2 value
    R2_train = model.score(X_train,y_train)
    R2_test = model.score(X_test,y_test)


    #manual adjusted r2 score
    k= X_train.shape[1] # returns the # of features in model
    n=len(y_train)      # returns the # of rows/observations
    R2_train_adj = 1 - ((1-R2_train)*(n-1)/(n-k-1))
    #manual adjusted r2 score
    kt= X_test.shape[1] # returns the # of features in model
    nt=len(y_test)      # returns the # of rows/observations
    R2_test_adj = 1 - ((1-R2_test)*(nt-1)/(nt-kt-1))


    # MSE
    y_pred = model.predict(X_train)
    mse_train = mean_squared_error(y_train, y_pred)
    # MSE
    y_predt = model.predict(X_test)
    mse_test = mean_squared_error(y_test, y_predt)

    # Training RMSE
    RMSE_train = (mean_squared_error(y_train, y_pred, squared = False))
    # Testing RMSE
    RMSE_test = (mean_squared_error(y_test, y_predt, squared = False))

    #MAE
    mae_train = mean_absolute_error(y_train, y_pred)
    mae_test = mean_absolute_error(y_test, y_predt)


    # calculate residuals
    residuals  = y_train - y_pred
    residualst = y_test - y_predt

    #SSE
    SSE_train = sum(residuals**2)
    SSE_test = sum(residualst**2)

    #max error (max residual error captues worst case error b./w perdicted values and true value)
    max_error_train = max_error(y_train, y_pred)
    max_error_test = max_error(y_test, y_predt)

    column_names=['R2_train','R2test','R2_adj_train','R2_test_adj','mse_train',
    'mse_test','RMSE_train','RMSE_test','max_error_train','max_error_test']

    list_metric = [R2_train,R2_test,R2_train_adj,R2_test_adj,mse_train,mse_test,RMSE_train,
    RMSE_test,RMSE_test,max_error_train,max_error_test]


    dictionary = dict(zip(column_names,list_metric))
    #print(dictionary)

    df =  pd.DataFrame([dictionary])

    return df
