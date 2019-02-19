#!/usr/local/bin/python3

print ("Pandas Processing for conflict")

import sys
print (sys.path)

import numpy as np
import pandas as pd

data = np.array(['a','b','c','d'])
s = pd.Series(data)
print (s)


#s = pd.Series([1, 3, 5, np.nan, 6, 8])
#print ("Series:", s)


dates = pd.date_range('20130101', periods=6)

print ("Dates:", dates)













