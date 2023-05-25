import pandas as pd
ipl_auction_df=pd.read_csv("IPL IMB381IPL2013.csv")
print(ipl_auction_df.COUNTRY.value_counts(normalize=True)*100)
