import numpy as np
import pandas as pd
import re
import os
from typing import List
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

### Helper Functions
def load_data() -> pd.DataFrame:
    """
    ===================================================================
    Load data from a directory and covert into a single dataframe.
    """
    # load the csv files in the 'data' directory and save it in a list
    files = [file for file in os.listdir('data/')]
    all_df = pd.DataFrame()  # empty dataframe
    for file in files:
        df = pd.read_csv(f'data/{file}')   # read each file 
        all_df = pd.concat([all_df, df], axis='index')  # concatenate each file
    # filter out duplicated records
    all_df = all_df[all_df.duplicated(keep='first')]
    return all_df 

def get_address(addr: str) -> str:
    """ 
    =====================================================================
        Extract the address.
    """
    result = addr.split(',')[-2:-1]  # select the city
    result = [x.strip() for x in result]  # remove the white spaces
    result = ', '.join(result)  # join on spaces (no longer a list)
    return result

def clean_text(text: str) -> str:
    """
    ====================================================================
        Clean the text.
    """
    pattern = r"\D+"  # non-digits
    result = re.sub(pattern, '', text, flags=re.I)
    return result

def load_estimator() -> 'estimator':
    """
    ====================================================================
    Load the trained model
    """ 
    # load the model
    with open('./model/estimator.pkl', 'rb') as f:
        loaded_estimators = pickle.load(f)
    return loaded_estimators

###############################################################################################################################################
# main function
def clean_data_n_return_estimator(data: pd.DataFrame):
    """
    ====================================================================
    Clean and tranform the features.
    """        
    df = data.copy()
    ### drop the missing values
    df = df.dropna()
    # clean the data
    for col in df.columns:
        if col == 'address':
            df[col] = df[col].apply(get_address)
        elif col != 'title':
            df[col] = df[col].apply(clean_text)
                
    # convert to numeric data type
    for col in ['bed', 'bath', 'toilet', 'pkn_space', 'price']:
        df[col] = pd.to_numeric(df[col])

    df = df.drop(columns=['title'])
    # select houses with bedrooms between 2 and 7
    df = df.loc[(df['bed'] > 1) & (df['toilet'] < 8)]
    # select houses with bathrooms between 2 and 7
    df = df.loc[(df['bath'] > 1) & (df['bath'] < 8)]
    # select houses with pkn_space between 1 and 10
    df = df.loc[(df['pkn_space'] > 2) & (df['pkn_space'] < 11)]
    #  outliers for price
    cut_off = np.percentile(df['price'], 97)  # remove prices above the 97th percentile
    df = df.loc[df['price'] <= cut_off]      
    # fill the missing values in 'pkn_space' with the median value
    median = df['pkn_space'].median()
    df['pkn_space'] = np.where(pd.isna(df['pkn_space']), median, df['pkn_space']) 

    # rename column
    df = df.rename(columns={'address': 'location'}) 
    locations = ['Lekki','Ajah','Ikeja','Ikoyi','Victoria Island (VI)','Ibeju Lekki','Isheri North','Magodo','Maryland',
             'Ikorodu','Surulere','Ojodu','Ipaja','Ikotun','Isolo']

    # Filter out locations with fewer counts
    df = df.loc[df['location'].isin(locations)]
    le_location = LabelEncoder()
    df['location'] = le_location.fit_transform(df['location'])
    # transform the price
    df['log_price'] = df['price'].apply(lambda price: np.log(price + 1))
    # drop the 'price'
    df = df.drop(columns=['price'])
    X = df.drop(columns=['log_price'])
    y = df['log_price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)
    # train the model with the optimal hyperparameters
    reg = RandomForestRegressor(max_depth=14, n_estimators=160, random_state=123)
    # fit 
    reg.fit(X_train, y_train)  

    # save the model
    model = {}
    model['reg'] = reg
    model['location'] = le_location
    with open('./model/estimator.pkl', 'wb') as f:
        pickle.dump(model, f)


if __name__ == "__main__":
    # load the data
    df = load_data()
    # clean the data and return an estimator
    clean_data_n_return_estimator(df)
