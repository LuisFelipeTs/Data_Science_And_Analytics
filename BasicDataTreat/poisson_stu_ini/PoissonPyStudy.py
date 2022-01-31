#from scipy.stats import poisson 

def factCalc(num):
    if num != 0:
        new_num = num
        while num != 1:
            num -= 1
            new_num *= num 
        return new_num
    return 1

def poisCalcaux(poi_x, poi_lam):
    e = 2.71828
    first_in_e = e ** -(poi_lam)
    sec_in = poi_lam ** poi_x
    denom = factCalc(poi_x)
    final_calc = (first_in_e * sec_in)/denom
    return final_calc

def poisCalc(poi_op, poi_x, poi_lam):
    #e = 2.71828
    if poi_op == "=": return poisCalcaux(poi_x, poi_lam)
    elif poi_op == "<":
        poi_som = 0
        for num_x in range(poi_x): poi_som += poisCalcaux(num_x, poi_lam)
        return poi_som

    elif poi_op == ">":
        poi_x_i = poi_x
        divid = poisCalcaux(poi_x_i, poi_lam)
        poi_som = 0
        for num_x in range(poi_x): poi_som += poisCalcaux(num_x, poi_lam)
        return 1 - (poi_som + divid)

    else: return "something is wrong with the entry try like this 2 > 4."

import tkinter as tk
from tkinter import simpledialog

tktk_v = tk.Tk()
tktk_v.withdraw()
options = simpledialog.askstring(title="Poisson choice",
                                  prompt="What's your Poisson situation?(Like: x = lambda)(=/</>)")
poisson_entry =options.split(" ")
 
poi_x = int(poisson_entry[0])
poi_op = poisson_entry[1]
poi_lam = int(poisson_entry[2])

print(poisCalc(poi_op, poi_x, poi_lam))
