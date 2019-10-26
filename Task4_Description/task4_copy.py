
import numpy as np
import pandas as pd
import feature_engine as fe

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from feature_engine.categorical_encoders import OneHotCategoricalEncoder

import matplotlib.pyplot as plt

%matplotlib inline

np.random.seed(48)

filename = 'csvdata.csv'
df = pd.read_csv(filename)
df.head()


cols = df.columns.tolist()
# remove # from column names
for idc, c in enumerate(cols):
    for idx, char in enumerate(c):
        if char == '#':
            break
    cols[idc] = c[:idx-1]
cols

def redefine_cols(cols):
    cols_asm = [c for c in cols if 'asm_' == c[:4]]
    cols_int = [c for c in cols if 'int_' == c[:4]]
    cols_fin = [c for c in cols if 'fin_' == c[:4]]
    return cols_asm, cols_int, cols_fin
cols_asm, cols_int, cols_fin = redefine_cols(cols)
print("Assembly data columns: {}".format(len(cols_asm)))
print("Initial inspection data columns: {}".format(len(cols_int)))
print("Final inspection data columns: {}".format(len(cols_fin)))

df.columns = cols

# Find Nan
df.isnull().mean()