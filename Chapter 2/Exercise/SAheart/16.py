import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd
SAheart=pd.read_csv("SAheart.data", sep=",")
print(SAheart[['tobacco', 'chd']].corr())
sn.heatmap(SAheart[['tobacco', 'chd']].corr(), annot=True)
plt.legend()
plt.show()
