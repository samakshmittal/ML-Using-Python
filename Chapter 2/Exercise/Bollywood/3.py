import pandas as pd
bollywood=pd.read_csv("bollywood.csv")
print(pd.crosstab(bollywood['Genre'], bollywood['ReleaseTime']))
