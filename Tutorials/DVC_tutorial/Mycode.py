import pandas as pd
import os

data  = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
         'Age': [28, 24, 35, 32],
         'Location': ['New York', 'Paris', 'Berlin', 'London']}

df = pd.DataFrame(data)



data_dir = 'data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

df.to_csv(os.path.join(data_dir, 'example_data.csv'), index=False)

print("Data saved to 'data/example_data.csv'")