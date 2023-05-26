import pandas as pd
ipl_auction_df=pd.read_csv("IPL IMB381IPL2013.csv")
print(ipl_auction_df.columns)
ipl_auction_df.drop('Sl.NO.', inplace=True, axis=1)
print(ipl_auction_df.columns)
