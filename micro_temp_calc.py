import numpy as np
import pandas as pd
import math as m
import datetime

# Function to calculate c_p_values for water
def c_p_calc(T):
    T = T + 273.15 # convert temperature from C to K

    a = 32.24
    b = 0.1923 * 10**(-2)
    c = 1.055 * 10**(-5)
    d = -3.595 * 10**(-9)

    water_mol_mass = 18.015 # molecular mass of water in g/mol

    c_p = (a + b*T + c*T**2 + d*T**3)*(1/water_mol_mass)

    return c_p


T_amb = 20 # ambient temperature in degrees C
T_des = int(input('Enter desired temperature of water in C: '))

power = int(input('Enter power of microwave in W: '))

vol_ml = int(input('Enter volume of water in mL: '))
vol_l = vol_ml/1000 # volume of water in m^3

rho = 997.048 # density of water in both kg/m^3 and g/L

water_mass = vol_l*rho # mass of water in kg

temp_range = np.linspace(T_amb, T_des, 100) # range of temperatures from ambient to desired

c_p_avg = c_p_calc(temp_range).mean() # average c_p value for water

time = (c_p_avg*water_mass*(T_des - T_amb))/power # time in seconds

time_conv = datetime.timedelta(seconds=round(time))

print('Time required in h:m:s: ', str(time_conv))
