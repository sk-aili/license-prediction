import warnings
warnings.filterwarnings("ignore")

# function to change columns name
def replace_char(columns, to_replace, replace_with):
    """This function takes a list of column names in a dataframe
    
    Args:
        columns(list) : list of column names in a dataframe
        to_replace(str) : character to be replaced in each column
        replace_with(str) : character to replace with in each column
    """
    new_col_list = [col.replace(to_replace, replace_with).lower() for col in columns]
    return new_col_list