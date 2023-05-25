import pandas as pd
ipl_auction_df=pd.read_csv("IPL IMB381IPL2013.csv")
soldprice_by_age=ipl_auction_df.groupby('AGE')['SOLD PRICE'].mean().reset_index()
print(soldprice_by_age)
