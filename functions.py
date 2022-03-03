import pandas as pd
import numpy as np
import pickle
import os

def data_int():
    '''
    import original data and save it as pickle
    data derived from Kaggle: 
    https://www.kaggle.com/ethon0426/lending-club-20072020q1 
    '''
    lending_data=pd.read_csv('../ML_projects_data/Lending_Club/Loan_status_2007-2020Q3.gzip',index_col=0)
    data_dic=pd.read_excel('../ML_projects_data/Lending_Club/LCDataDictionary.xlsx')
    with open('../ML_projects_data/Lending_Club/raw_lending_club_data.pickle','wb') as f:
        pickle.dump([data_dic,lending_data],f)

def preprocessing(df):
    '''
    preprocessing data:
        1. delete meaningless data
        2. modify data to proper format
        3. 
    ---
    df: raw data
    '''
    # delete data whose id had invalid value



if __name__=="__main__":
    '''
    main programs
    '''
    data_int()