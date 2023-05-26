import pandas as pd
autos=pd.read_csv("auto-mpg.data", sep='\s+', header=None)
autos.columns=['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'year', 'origin', 'name']
autos=autos.fillna(0)
print(autos[autos.horsepower.isnull()])
