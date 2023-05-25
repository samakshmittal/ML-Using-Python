import pandas as pd
ipl_auction_df=pd.read_csv("IPL IMB381IPL2013.csv")
soldprice_by_age=ipl_auction_df.groupby('AGE')['SOLD PRICE'].mean().reset_index()
soldprice_by_age_role=ipl_auction_df.groupby(['AGE', 'PLAYING ROLE'])['SOLD PRICE'].mean().reset_index()
soldprice_comparison=soldprice_by_age_role.merge(soldprice_by_age, on='AGE', how='outer')
soldprice_comparison.rename(columns={'SOLD PRICE_x':'SOLD_PRICE_AGE_ROLE', 'SOLD PRICE_y':'SOLD_PRICE_AGE'}, inplace=True)
soldprice_comparison['CHANGE']=soldprice_comparison.apply(lambda rec:(rec.SOLD_PRICE_AGE_ROLE-rec.SOLD_PRICE_AGE)/rec.SOLD_PRICE_AGE, axis=1)
print(soldprice_comparison.head(5))
