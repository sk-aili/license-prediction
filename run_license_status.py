import os
from src import utils, preprocessing

parent_dir = os.path.dirname(os.getcwd())
data_path = "/ml/input/license.csv"

df = utils.read_data(parent_dir+data_path)

# review gist of the data
utils.data_gist(df)

# change the columns name
df.columns = preprocessing.replace_char(df.columns, " ", "_")

