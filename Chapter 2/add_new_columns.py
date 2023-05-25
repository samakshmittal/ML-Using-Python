import pandas as pd
ipl_auction_df=pd.read_csv("IPL IMB381IPL2013.csv")
ipl_auction_df['PREMIUM']=ipl_auction_df['SOLD PRICE']-ipl_auction_df['BASE PRICE']
print(ipl_auction_df[['PLAYER NAME', 'BASE PRICE', 'SOLD PRICE', 'PREMIUM']][0:5])
