import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
bollywood=pd.read_csv("bollywood.csv")
bollywood['ROI']=(bollywood['BoxOfficeCollection']-bollywood['Budget'])/bollywood['Budget']
print(bollywood.groupby(['Genre'])['YoutubeLikes'].mean().sort_values(ascending=False).head(1))
sn.boxplot(x='Genre', y='YoutubeLikes', data=bollywood)
plt.show()
