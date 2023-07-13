from pandas as pd
from sklearn.model_selection import train_test_split

# function to read the data
def read_data(file_path, **kwargs):
    '''This function reads data from the given filepath and returns a pandas dataframe

    Args:
        file_path(str) : path to file
    '''
    raw_data = pd.read_csv(file_path, **kwargs)
    return raw_data