import statistics as stc
import pandas as pd
import numpy as npy
from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype

#from Tkinter import Tk
#from tkinter.filedialog import askopenfilename
#Tk().withdraw()
#filename = askopenfilename()

file_l = " "
n_data = pd.read_csv(file_l, sep = ";")

def moda_calc(lista):
    #function for the specific pandas case (mode calculation) 
    cases = {} 
    for i in lista:
        if (isinstance(i, float)): continue
        elif i not in cases.keys(): cases[i] = 1
        else : cases[i] += 1
    chave_maj = max(cases, key=lambda key: cases[key])
    print(chave_maj)

colnames = list(n_data.columns)
for col in (colnames):
    if n_data[col].isnull().sum() > 0:
        if is_numeric_dtype(n_data[col]): 
            n_data[col].fillna(stc.median(n_data[col]),inplace = True)
        elif is_string_dtype(n_data[col]):
            mode = moda_calc(n_data[col])
            #n_data[col].fillna(mode), inplace = True)
            #print(n_data.loc[n_data[col] == float, col])
            n_data.loc[n_data[col] == float, col] = mode
    else: ("The column " + col +" is completed.")
print(n_data)
