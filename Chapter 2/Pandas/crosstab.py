import pandas as pd
ipl_auction_df=pd.read_csv("IPL IMB381IPL2013.csv")
print(pd.crosstab(ipl_auction_df['AGE'], ipl_auction_df['PLAYING ROLE']))
