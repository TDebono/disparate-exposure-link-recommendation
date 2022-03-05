import pandas as pd
import numpy as np
from operator import itemgetter
import os

def load_profile_data(dir_string):

    directory = os.fsencode(dir_string)

    profile_array = []
    COL_INDICES = [0, 3, 7]
        
    for profile_data_file in os.listdir(directory):
        with open(dir_string + (str(profile_data_file)[2:-1])) as f:
            for line in f:
                profile_array.append(itemgetter(*COL_INDICES)(line.split("\t")))
    
    return np.array(profile_array)

def profile_data_to_df(profile_array, replace_null_strings=True):
    
    profile_df = pd.DataFrame(data=profile_array[0:,0:], 
                  index=[i for i in range(profile_array.shape[0])],
                  columns=['user_id', 'gender', 'age'])
    
    if replace_null_strings:
        profile_df.replace('null', -999999, inplace=True)
        profile_df.astype(int)
        profile_df.replace(-999999, np.nan, inplace=True)
    
    return profile_df