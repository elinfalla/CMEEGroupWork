#!/usr/bin/env python3

""""Stochastic implementation of the Ricker model and a vectorised version"""

__appname__ = "Vectorise2.py"
__author__ = "Elin Falla, ef16@ic.ac.uk"  # change - ADD NAMES
__version__ = "0.0.1"

# Imports
import numpy as np
import sys
import time


def stochrick(p0=np.random.uniform(.5, 1.5, 1000), r=1.2, K=1, sigma=0.2,
              numyears=100):  # change - i have numyears as 10?
    """"Runs the stochastic Ricker equation with Gaussian fluctuations"""

    N = np.zeros((numyears, len(p0)))  # initialize empty matrix with numyears rows and len(p0) columns #change

    N[0] = p0

    for pop in range(len(p0)):  # loop through the populations #change - don't need 0

        for yr in range(1, numyears):  # for each pop, loop through the years

            N[yr, pop] = N[yr - 1, pop] * np.exp(r * (1 - N[yr - 1, pop] / K) + np.random.normal(0, sigma,
                                                                                                 1))  # add one fluctuation from normal distribution

    return N


# Now write another function called stochrickvect that vectorizes the above
# to the extent possible, with improved performance: 


def stochrickvect(p0=np.random.uniform(.5, 1.5, 1000), r=1.2, K=1, sigma=0.2, numyears=100):
    """"Runs vectorised version of stochastic Ricker equation with Gaussian fluctuations"""
    N = np.zeros((numyears, len(p0)))  # initialize empty matrix

    N[0] = p0

    for yr in range(1, numyears):  # for each pop, loop through the years

        N[yr] = N[yr - 1] * np.exp(r * (1 - N[yr - 1] / K) + np.random.normal(0, sigma, len(
            p0)))  # add one fluctuation from normal distribution #change
        # change, remove commas as not needed, change 1 to len(p0)
    return N


def main(argv):
    """"Main function: times stochrick and stockrickvect and outputs result to console"""

    start = time.time()
    T = stochrick()
    end = time.time()
    print("Non-vectorized Stochastic Ricker takes:")
    print(end - start)

    start = time.time()
    T = stochrickvect()
    end = time.time()
    print("Vectorized Stochastic Ricker takes:")
    print(end - start)

    print("Script done!")

    return 0


if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)
