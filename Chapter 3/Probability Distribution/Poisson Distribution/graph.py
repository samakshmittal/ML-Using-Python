from scipy import stats
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
pmf_df=pd.DataFrame({'success':range(0, 30), 'pmf': list(stats.poisson.pmf(range(0, 30), 10))})
sn.barplot(x=pmf_df.success, y=pmf_df.pmf)
plt.ylabel('pmf')
plt.xlabel('Number of calls received')
plt.show()
