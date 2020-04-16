import pandas as pd
import numpy as np
import csv

df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]), columns=['a','b','c'])

print(df)

NewArray = df.transform(func = lambda x : x*10)

print(NewArray)

df1 = df.groupby('a')["b"].mean()

print(df1)

mean_weight = df.groupby('a')["b"].mean().rename("Mean_Weight").reset_index()
df_1 = df.merge(mean_weight)

print(df_1)

df['d'] = df.apply(lambda row: row.a + row.b + row.c, axis = 1)

print(df['d'])
