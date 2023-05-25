import pandas as pd
ipl_auction_df=pd.read_csv("IPL IMB381IPL2013.csv")
soldprice_by_age=ipl_auction_df.groupby('AGE')['SOLD PRICE'].mean().reset_index()
soldprice_by_age_role=ipl_auction_df.groupby(['AGE', 'PLAYING ROLE'])['SOLD PRICE'].mean().reset_index()
soldprice_comparison=soldprice_by_age_role.merge(soldprice_by_age, on='AGE', how='outer')
print(soldprice_comparison)
