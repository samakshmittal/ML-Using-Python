import math
import pandas as pd
from scipy import stats
passport_df=pd.read_csv('passport.csv')
#print(passport_df.head(5))
#print(list(passport_df.processing_time))
def z_test(pop_mean, pop_std, sample):
    z_score=(sample.mean()-pop_mean)/(pop_std/math.sqrt(len(sample)))
    return z_score, stats.norm.cdf(z_score)
print(z_test(30, 12.5, passport_df.processing_time))
#7051251263
