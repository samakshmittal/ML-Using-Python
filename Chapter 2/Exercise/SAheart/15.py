import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd
SAheart=pd.read_csv("SAheart.data", sep=",")
print(SAheart[['age', 'sbp']].corr())
sn.heatmap(SAheart[['age', 'sbp']].corr(), annot=True)
plt.legend()
plt.show()
