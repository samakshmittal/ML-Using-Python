import pandas as pd
count=0
SAheart=pd.read_csv("SAheart.data", sep=",")
for x in SAheart.transpose():
    count+=1
print(count)
print(SAheart.shape)
print(SAheart.info())
