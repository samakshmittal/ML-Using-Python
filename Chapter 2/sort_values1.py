import pandas as pd
ipl_auction_df=pd.read_csv("IPL IMB381IPL2013.csv")
print(ipl_auction_df[['PLAYER NAME', 'SOLD PRICE']].sort_values('SOLD PRICE', ascending=False)[0:5])
