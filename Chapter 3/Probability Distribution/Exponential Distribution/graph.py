from scipy import stats
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
pdf_df=pd.DataFrame({'success':range(0, 5000, 100), 'pdf': list(stats.expon.pdf(range(0,5000, 100), loc=1/1000, scale=1000))})
sn.barplot(x=pdf_df.success, y=pdf_df.pdf)
plt.ylabel('pdf')
plt.xticks(rotation=90)
plt.xlabel('Time to failure')
plt.show()
