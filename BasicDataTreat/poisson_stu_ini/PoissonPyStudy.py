#from scipy.stats import poisson 

def factCalc(num):
    if num != 0:
        new_num = num
        while num != 1:
            num -= 1
            new_num *= num 
        return new_num
    return 1

def poisCalc(poi_op, poi_x, poi_lam):
    if poi_op == "=":
        first_in_e = e ** -(poi_lam)
        sec_in = poi_lam ** poi_x
        denom = factCalc(poi_x)
        final_calc = (first_in_e * sec_in)/denom
        return final_calc

    elif poi_op == "<":
        divid = 0
        for num_x in range(poi_x):
            first_in_e = e ** -(poi_lam)
            sec_in = poi_lam ** num_x
            denom = factCalc(num_x)
            final_calc = (first_in_e * sec_in)/denom
            divid += final_calc
        return divid

    elif poi_op == ">":
        poi_x_i = poi_x
        first_in_e = e ** -(poi_lam)
        sec_in = poi_lam ** poi_x_i
        denom = factCalc(poi_x_i)
        final_calc = (first_in_e * sec_in)/denom
        divid = final_calc

        for num_x in range(poi_x):
            first_in_e = e ** -(poi_lam)
            sec_in = poi_lam ** num_x
            denom = factCalc(num_x)
            final_calc = (first_in_e * sec_in)/denom
            divid += final_calc

e = 2,71828
poisson_entry = input().split(" ")
poi_x = int(poisson_entry[0])
poi_op = poisson_entry[1]
poi_lam = int(poisson_entry[2])


