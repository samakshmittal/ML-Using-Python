import pandas as pd
import numpy as np
import warnings
import matplotlib.pyplot as plt
import seaborn as sn
beml_df=pd.read_csv('BEML.csv')
#print(beml_df[0:5])
glaxo_df=pd.read_csv('GLAXO.csv')
#print(glaxo_df[0:5])
beml_df=beml_df[['Date', 'Close']]
glaxo_df=glaxo_df[['Date', 'Close']]
glaxo_df=glaxo_df.set_index(pd.DatetimeIndex(glaxo_df['Date']))
beml_df=beml_df.set_index(pd.DatetimeIndex(beml_df['Date']))
#print(glaxo_df.head(5))
plt.plot(glaxo_df.Close)
plt.xlabel('Time')
plt.ylabel('Close Price')
#plt.show()
plt.plot(beml_df.Close)
plt.xlabel('Time')
plt.ylabel('Close Price')
#plt.show()
glaxo_df['gain']=glaxo_df.Close.pct_change(periods=1)
beml_df['gain']=beml_df.Close.pct_change(periods=1)
#print(glaxo_df.head(5))
glaxo_df=glaxo_df.dropna()
beml_df=beml_df.dropna()
plt.figure(figsize=(8,6))
plt.plot(glaxo_df.index, glaxo_df.gain)
plt.xlabel('Time')
plt.ylabel('gain')
#plt.show()
sn.displot(glaxo_df.gain, label='Glaxo')
sn.displot(beml_df.gain, label='BEML')
plt.xlabel('Gain')
plt.ylabel('Density')
plt.legend()
#plt.show()
