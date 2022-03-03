#%%
import numpy as np
import pandas as pd
import pickle
import os

#%% ------------load data------------
with open('../ML_projects_data/Lending_Club/original_lending_club_data.pickle','rb') as f:
    data_dic,lending_data=pickle.load(f)
#%%

lending_data.shape

#%%------------data dictionary------------
data_dic[data_dic['LoanStatNew']=='id']

#%%
np.unique([i for i in lending_data['id']])

