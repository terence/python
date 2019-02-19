#!/usr/local/bin/python3

print ("Scipy Processing")

import sys
print (sys.path)

import numpy as np
#import scipy as sp
from scipy.stats import norm
from scipy.stats import uniform




# Statistics
# ==========================
print(norm.cdf(np.array([1,-1., 0, 1, 3, 4, -2, 6])))
print(norm.ppf(0.5))

# Generate uniform distribution
print(uniform.cdf([0, 1, 2, 3, 4, 5], loc = 1, scale = 4))

x = np.array([1,2,3,4,5,6,7,8,9])
print(x.max(),x.min(),x.mean(),x.var())

# Interpolation
# =============================

from scipy import interpolate
import matplotlib.pyplot as plt
x = np.linspace(0, 4, 12)
y = np.cos(x**2/3+4)
print(x,y)

plt.plot(x, y)
plt.show()





