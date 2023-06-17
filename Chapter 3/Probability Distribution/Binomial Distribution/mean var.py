from scipy import stats
mean, var=stats.binom.stats(20, 0.1)
print(mean, var)
