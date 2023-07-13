# function to read the data
def read_data(file_path, **kwargs):
    '''This function reads data from the given filepath and returns a pandas dataframe

    Args:
        file_path(str) : path to file
    '''
    import pandas as pd

    raw_data = pd.read_csv(file_path, **kwargs)
    return raw_data


# function to get gist of a dataframe
def data_gist(dataframe, head=True, tail=False, describe=True):
    """This function provides a gist of the data
    
    Args:
        dataframe(dataframe) : data
        head(boolean) : default is True, used to print top 5 observations in the data
        tail(boolean) : default is False, used to print bottom 5 observations in the data
        describe(boolean) : default is False, used to provide descriptive summary of the data
    """
    import pandas as pd

    print("Data gist:")
    print("Columns: ", dataframe.columns.tolist())
    
    if head:
        print("Top 5 observations:")
        print(dataframe.head(5))
    if tail:
        print("Bottom 5 observations:")
        print(dataframe.tail(5))
    if describe:
        print("Descriptive summary of the data:")
        print(dataframe.describe())

    return


# function to split data into training and testing set
def data_split(X, y, size=0.3):
    """This function splits data into 70:30. It will return 4 data frames: X_train, X_test, y_train, y_test
    Args:
        X(dataframe) : X size = NxP where N is number of observations, P is number of independent variables
        y(dataframe) : y size = Nx1 where N is number of observations
    """
    from sklearn.model_selection import train_test_split

    return train_test_split(X, y, test_size=size)