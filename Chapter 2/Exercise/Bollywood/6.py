import pandas as pd
bollywood=pd.read_csv("bollywood.csv")
bollywood['ROI']=(bollywood['BoxOfficeCollection']-bollywood['Budget'])/bollywood['Budget']
print(bollywood[['ROI','MovieName']].sort_values('ROI', ascending=False).head(10))
