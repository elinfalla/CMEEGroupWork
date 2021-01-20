#!/usr/bin/env R

import numpy as np
import time

M = np.random.rand(1000, 1000)

def SumAllElements(M):
    Dimensions = M.shape
    Tot = 0
    for i in range(0, Dimensions[0]):
        for j in range(0, Dimensions[1]):
            Tot = Tot + M[i, j]
    return Tot

start = time.time()
T = SumAllElements(M)
end = time.time()
print("Using loops, the time taken is:")
print(end - start)

start = time.time()
T = sum(M)
end = time.time()
print("Using the in-built vectorized function, the time taken is:")
print(end - start)

print("Script done!")