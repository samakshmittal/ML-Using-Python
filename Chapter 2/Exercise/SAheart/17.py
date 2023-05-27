import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd
SAheart=pd.read_csv("SAheart.data", sep=",")
print(SAheart[['sbp', 'obesity', 'age', 'ldl']].corr())
sn.heatmap(SAheart[['sbp', 'obesity', 'age', 'ldl']].corr(), annot=True)
plt.show()
