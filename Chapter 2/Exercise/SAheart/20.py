import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd
SAheart=pd.read_csv("SAheart.data", sep=",")
category=pd.cut(SAheart.age, bins=[0, 15, 35, 55, 200], labels=['young', 'adults', 'mid', 'old'])
SAheart.insert(11, 'agegroup', category)
sn.boxplot(SAheart[['agegroup', 'ldl']])
plt.show()
