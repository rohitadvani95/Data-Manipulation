import pandas as pd
import random


data = pd.DataFrame({
    'C' : [random.choice(('a','b','c')) for i in range(1000000)],
    'A' : [random.randint(1,10) for i in range(1000000)],
    'B' : [random.randint(1,10) for i in range(1000000)]


    })



data.groupby('C')["A"].mean()
mean = data.groupby('C')["A"].mean().rename("N").reset_index()
df_1 = data.merge(mean)

print(df_1)


data['N3'] = data.groupby(['C'])['A'].transform('mean')

print(data['N3'])
