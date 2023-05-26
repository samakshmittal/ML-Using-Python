import pandas as pd
autos=pd.read_csv("auto-mpg.data", sep='\s+', header=None)
autos.columns=['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'year', 'origin', 'name']
print(autos.info())
