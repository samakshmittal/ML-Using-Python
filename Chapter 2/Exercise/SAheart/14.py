import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd
SAheart=pd.read_csv("SAheart.data", sep=",")
sn.barplot(x="chd", y="famhist", data=SAheart)
plt.legend()
plt.show()
