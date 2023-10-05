#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:55:04 2023

@author: rohitadvani
"""



import pandas as pd

import csv

from pathlib import Path 
import os

rawdata = pd.read_csv(r'/Users/rohitadvani/Documents/Service/2039/2039Rows.csv', header=None, skiprows=0)

print(rawdata)
print(type(rawdata))

Cols = rawdata.transpose()

print(Cols)

df_reversed = Cols[::-1]

print(df_reversed)

#df_reversed.to_csv(index=False)
filepath = Path('/Users/rohitadvani/Documents/Service/2039/2039Cols.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
df_reversed.to_csv(filepath)