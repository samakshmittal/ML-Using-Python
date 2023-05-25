import pandas as pd
ipl_auction_df=pd.read_csv("IPL IMB381IPL2013.csv")
pd.set_option('display.max_columns', 7)
print(ipl_auction_df.head(5))
