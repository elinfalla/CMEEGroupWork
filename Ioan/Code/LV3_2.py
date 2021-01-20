#!/usr/bin/env python3

"""Defining and plotting a discrete-time version of the Lotka-Volterra model of population dynamics for inputted parameters."""

### The Lotka-Volterra model

## Imports
import scipy as sc
import numpy as np
import scipy.integrate as integrate
import matplotlib.pylab as p
import sys

# Define the function
def dCR_dt(pops):
    R = pops[0]
    C = pops[1]
    Rnext = R * (1 + r * (1 - R / K) - a * C)
    Cnext = C * (1 - z + e * a * R)
    return np.array([Rnext, Cnext])


def plot1(pops, t): 
    """Plot lines showing consumer and resource population dynamics against time"""
    # create an empty figure object
    f1 = p.figure()
    # plot consumer density and resource density
    p.plot(t, pops[:,0], 'g-', label = 'Resource density')
    p.plot(t, pops[:,1], 'b-', label = 'Consumer density')
    p.grid()
    p.legend(loc='best')
    p.xlabel('Time')
    p.ylabel('Population density')
    p.title('Consumer-Resource population dynamics')
    # save the figure as a pdf
    f1.savefig('../Results/LV3_model1.pdf')


def plot2(pops): 
    """ """
    # create an empty figure object
    f2 = p.figure()
    # plot consumer density and resource density in another way
    p.plot(pops[:,0], pops[:,1], 'r-')
    p.grid()
    p.xlabel('Resource density')
    p.ylabel('Consumer density')
    p.title('Consumer-Resource population dynamics')
    # save the figure as a pdf
    f2.savefig('../Results/LV3_model2.pdf')

def main(argv):
    
    """main function of the program"""

    # Read parameters from command line
    global r, a, z, e, K
    r = 0.05
    a = 0.05
    z = 0.05
    e = 0.02
    K = 10000

    # Set the initial conditions for the two populations, convert the two into an array
    R0 = 10
    C0 = 5
    RC0 = np.array([R0, C0])
    
    # Define population density array
    pops = np.array([[R0, C0]])
    
    # Define starting point of time
    t = 0
    
    # Create 1000 density data of each population
    while t < 999:
        RC0 = dCR_dt(RC0)
        pops = np.append(pops, [[RC0[0], RC0[1]]], axis = 0)
        t = t + 1
    
    # Define total t series
    t = np.array(range(1000))
    
    # Plot population dynamic of consumer and resource and save to Results
    plot1(pops, t)
    plot2(pops)


if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)