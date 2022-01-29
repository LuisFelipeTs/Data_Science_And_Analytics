#TESTE HIP

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

x_med = st.mean(x)
y_med = st.mean(y)
y_dvp = st.stdev(y)
n = len(y)

result = (x_med - y_med)/(y_dvp/math.sqrt(n))
print(result)