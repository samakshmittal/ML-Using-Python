import pandas as pd
count=0
bollywood=pd.read_csv("bollywood.csv")
for x in bollywood.transpose():
    count+=1
print(count)
print(bollywood.info())
