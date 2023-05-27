import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
bollywood=pd.read_csv("bollywood.csv")
bollywood['ROI']=(bollywood['BoxOfficeCollection']-bollywood['Budget'])/bollywood['Budget']
sn.distplot(bollywood[bollywood['Genre']=='Comedy']['ROI'], color='y', label='Comedy')
sn.distplot(bollywood[bollywood['Genre']==' Drama ']['ROI'], color='b', label='Drama')
plt.legend()
plt.show()
