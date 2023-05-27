import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
bollywood=pd.read_csv("bollywood.csv")
bollywood['ROI']=(bollywood['BoxOfficeCollection']-bollywood['Budget'])/bollywood['Budget']
plt.hist(bollywood['Budget'])
sn.distplot(bollywood['Budget'])
plt.show()
