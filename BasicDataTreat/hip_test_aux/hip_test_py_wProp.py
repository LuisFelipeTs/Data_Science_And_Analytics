#hip_test_py_wProp

import pandas as pd
import statistics as st
#import matplotlib.pyplot as mp
import math as math

data_base_old = pd.read_csv("", sep = ";") #old hip database
alf = 0.05
data_base_new = pd.read_csv("", sep = ";") #new hip database
col_name = "" #Nome da coluna em ambas

x = data_base_old[col_name]
y = data_base_new[col_name]

p0_med = st.mean(x)
p_med = st.mean(y)
y_dvp = st.stdev(y)
n = len(y)

result = (p_med - p0_med)/(math.sqrt(p0_med * (1 - p0_med)/ n ))
print(result)