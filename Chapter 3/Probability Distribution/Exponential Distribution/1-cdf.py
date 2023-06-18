from scipy import stats
print(1-stats.expon.cdf(1000, loc=1/1000, scale=1000))
