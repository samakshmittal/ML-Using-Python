from scipy import stats
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
pmf_df=pd.DataFrame({'success':range(0, 21), 'pmf': list(stats.binom.pmf(range(0,21), 20, 0.1))})
sn.barplot(x=pmf_df.success, y=pmf_df.pmf)
plt.ylabel('pmf')
plt.xlabel('Number of items returned')
plt.show()
