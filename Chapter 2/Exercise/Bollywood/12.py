import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
bollywood=pd.read_csv("bollywood.csv")
bollywood['ROI']=(bollywood['BoxOfficeCollection']-bollywood['Budget'])/bollywood['Budget']
sn.heatmap(bollywood[['Budget', 'BoxOfficeCollection', 'YoutubeViews', 'YoutubeLikes', 'YoutubeDislikes']].corr(), annot=True)
sn.pairplot(bollywood[['Budget', 'BoxOfficeCollection', 'YoutubeViews', 'YoutubeLikes', 'YoutubeDislikes']])
plt.show()
