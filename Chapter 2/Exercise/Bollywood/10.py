import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
bollywood=pd.read_csv("bollywood.csv")
bollywood['ROI']=(bollywood['BoxOfficeCollection']-bollywood['Budget'])/bollywood['Budget']
print(bollywood[['BoxOfficeCollection', 'YoutubeLikes']].corr())
sn.heatmap(bollywood[['BoxOfficeCollection', 'YoutubeLikes']].corr(), annot=True)
plt.show()
