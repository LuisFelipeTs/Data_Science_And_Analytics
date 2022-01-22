import statistics as sts
import pandas as pds
from pandas.api.types import is_numeric_dtype

base_of_data = pds.read_csv("tempo.csv", sep = ";")

n_columns = list(base_of_data.columns)

for col in n_columns:
    if is_numeric_dtype(base_of_data[col]):
        
        if base_of_data[col].isnull().sum() > 0:
            n_median_col = sts.median(base_of_data[col])
            base_of_data[col].fillna(median_col, inplace=True)
        #In progress    
        #if  (max(base_of_data[col]) > (5 * sts.mean(base_of_data[col]))):
        dsvp = 2*(sts.stdev(base_of_data[col]))
        if  dsvp >= (sts.mean(base_of_data[col])):
            median_col = sts.median(base_of_data[col])
            base_of_data.loc[base_of_data[col] > dsvp, col] =  median_col
print(base_of_data)
