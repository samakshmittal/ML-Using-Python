import pandas as pd
import numpy as np
import warnings
import matplotlib.pyplot as plt
import seaborn as sn
beml_df=pd.read_csv('BEML.csv')
glaxo_df=pd.read_csv('GLAXO.csv')
beml_df=beml_df[['Date', 'Close']]
glaxo_df=glaxo_df[['Date', 'Close']]
glaxo_df=glaxo_df.set_index(pd.DatetimeIndex(glaxo_df['Date']))
beml_df=beml_df.set_index(pd.DatetimeIndex(beml_df['Date']))
glaxo_df['gain']=glaxo_df.Close.pct_change(periods=1)
beml_df['gain']=beml_df.Close.pct_change(periods=1)
glaxo_df=glaxo_df.dropna()
beml_df=beml_df.dropna()
print('Daily gain of Glaxo')
print('--------------------')
print('Mean: ', round(glaxo_df.gain.mean(), 4))
print('Standard Deviation: ', round(glaxo_df.gain.std(), 4))
print('Daily gain of BEML')
print('--------------------')
print('Mean: ', round(beml_df.gain.mean(), 4))
print('Standard Deviation: ', round(beml_df.gain.std(), 4))
