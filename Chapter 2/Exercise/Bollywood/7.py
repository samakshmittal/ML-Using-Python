import pandas as pd
bollywood=pd.read_csv("bollywood.csv")
bollywood['ROI']=(bollywood['BoxOfficeCollection']-bollywood['Budget'])/bollywood['Budget']
print(bollywood.groupby(['ReleaseTime'])['ROI'].mean().sort_values(ascending=False).head(10))
