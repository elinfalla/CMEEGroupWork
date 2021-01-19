#!usr/bin/env python3

"""Script that runs a discrete-time version of the Lotka-Volterra model"""

__appname__ = "LV3.py"
__author__ = 'Elin Falla (ef16@ic.ac.uk)'
__version__ = '0.0.1'

# Imports #
import numpy as np
import sys
import matplotlib.pylab as p


def run_LV(R=10, C=5, r=1., a=0.2, z=1.5, e=0.5, K=50, generations=10):
    """Runs LV model 'generations' times"""

    pops = np.array([(R, C)], np.float64)  # double square brackets specifies 2D array (ie. matrix)

    print(r,a,z,e)
    for i in range(generations):
        print("i = ",i)
        print("pops[i,0] = ", pops[i, 0])
        print("pops[i,1] = ", pops[i, 1])

        prev_r, prev_c = pops[i, 0], pops[i, 1]

        # prev_r_space_left = 1 - prev_r / K
        # next_r_growth =
        nextR = prev_r * (1 + r * (1 - prev_r / K) - a * prev_c)
        # print(f'prev_r={prev_r}, prev_r_cap={prev_r_space_left}, next_r_growth={next_r_growth}, nextR={nextR}')

        nextC = prev_c * (1 - z + e * a * prev_r)
        # print(f'ear={ear}, nextC={nextC}')

        if nextR < 0:
            nextR = 0
        elif nextC < 0:
            nextC = 0
        pops = np.append(pops, [(nextR, nextC)], axis=0)  # append row to pops
        #print(pops)

    return pops

def main(argv):

    num_gen = 10
    timeframe = range(num_gen+1)

    pops = run_LV(generations=10)
    print(f'pops len={len(pops[:,0])}, timeframe={len(timeframe)}')
    # print final populations
    print("Final R =", round(pops[-1, 0], 3))
    print("Final C =", round(pops[-1, 1], 3))

    p.plot(timeframe, pops[:, 0], 'g-', label="Resource density")
    p.plot(timeframe, pops[:, 1], 'b-', label="Consumer density")
    p.grid()
    p.show()

    return 0

if __name__ == "__main__":
    status = main(sys.argv)
    sys.exit(status)