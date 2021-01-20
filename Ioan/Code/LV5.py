#!/usr/bin/env python3

"""Defining and plotting a discrete-time version of the Lotka-Volterra model of population dynamics with a random gaussian fluctuation in resource and consumer growth rate at each time step."""

### To do!!!


### The Lotka-Volterra model

## Imports
from sys import argv

import matplotlib.pylab as p
import numpy as np
import scipy.integrate as integrate
import timeit

## Profile pt1
import time
startTime = time.time()

## Assign arguments of the four LV model parameters
script, r, a, z, e, K = argv

r = float(r) # Growth rate
a = float(a) # Death rate
z = float(z) # 
e = float(e) # 
K = float(K) # Carrying capacity

# 1 0.2 2 0.5 50
ϵ = np.random.normal()

## Define the function
def dCR_dt(pops, t=0):
    """Discrete time version of the Lotka-Volterra model with density dependence and random gaussian fluctuation in resource's growth rate at each time step."""
    R = pops[0]
    C = pops[1]
    dRdt = R * ( 1 + (r + ϵ) * (1 - (R / K)) - (a * C) )
    dCdt = C * (1 - z + (e * a * R))
    
    return np.array([dRdt, dCdt])

## Define the time vector
t = np.arange(0, 100, 0.01)

## Set the initial conditions for the two populations
R0 = 10
C0 = 5 
RC0 = np.array([R0, C0])

## Numerically integrate this system forward from those starting conditions
pops, infodict = integrate.odeint(dCR_dt, RC0, t, full_output=True)

f1 = p.figure()
p.plot(t, pops[:,0], 'g-', label='Resource density') # Plot
p.plot(t, pops[:,1]  , 'b-', label='Consumer density')
p.grid()
p.legend(loc='best')
p.xlabel('Time')
p.ylabel('Population density')
p.title('Consumer-Resource population dynamics')
p.text(82, 5.85, f'r={r}\na={a}\nz={z}\ne={e}\nK={K}')

f1.savefig('../Results/LV4_model1.pdf') #Save figure

f2 = p.figure()
p.plot(pops[:,0], pops[:,1], 'r-') # Plot
p.grid()
p.xlabel('Resource density')
p.ylabel('Consumer density')
p.title('Consumer-Resource population dynamics')
p.text(16.15, 11.15, f'r={r}\na={a}\nz={z}\ne={e}\nK={K}')

f2.savefig('../Results/LV4_model2.pdf') 

## Profile pt2
executionTime = (time.time() - startTime)
print('LV4.py execution time in seconds: ' + str(round(executionTime, 3)) + ".")

print(f"The resource density at the last timepoint in LV4 is {round(pops[9999,0], 3)}.")
print(f"The consumer density at the last timepoint in LV4 is {round(pops[9999,1], 3)}.")