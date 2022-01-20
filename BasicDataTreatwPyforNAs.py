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

#function for the specific pandas case (mode calculation) 
def moda_calc(lista):
    cases = {} 
    v_list = []
    for i in lista:
        if (isinstance(i, float)): continue
        elif i not in cases.keys():
            cases[i] = 1
            v_list.append(i)
        else : cases[i] += 1
    chave_maj = max(cases, key=lambda key: cases[key])
    return(chave_maj, v_list)

colnames = list(n_data.columns)
for col in (colnames):
    if n_data[col].isnull().sum() > 0:
        if is_numeric_dtype(n_data[col]): 
            n_data[col].fillna(stc.median(n_data[col]),inplace = True)
        elif is_string_dtype(n_data[col]):
            mode, v_list = moda_calc(n_data[col])
            #n_data[col].fillna(mode), inplace = True
            n_data.loc[~n_data[col].isin(v_list), col] = mode
    else: ("The column " + col +" is completed.")
print(n_data)
