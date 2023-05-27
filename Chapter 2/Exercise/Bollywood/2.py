import pandas as pd
bollywood=pd.read_csv("bollywood.csv")
print(bollywood.groupby('Genre')['MovieName'].count())
print(bollywood.groupby(['Genre'])['MovieName'].count().sort_values(ascending=False).head(1))
print(bollywood.groupby(['Genre'])['MovieName'].count().sort_values(ascending=False))
