import pandas as pd
autos=pd.read_csv("auto-mpg.data", sep='\s+', header=None)
print(autos.head(5))
