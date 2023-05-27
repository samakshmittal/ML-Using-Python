import pandas as pd
bollywood=pd.read_csv("bollywood.csv")
bollywood['MonthName']=pd.DatetimeIndex(bollywood['Release Date']).month_name()
bolly=bollywood[bollywood['Budget']>25]
print(bolly.groupby(['MonthName'])['MovieName'].count().sort_values(ascending=False).head(1))
