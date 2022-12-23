import statistics   # imports all the methods  in the statistics module

from statistics import mean  # imports only the mean method

# mean is the method in the statistics module that calculates aveage
# the mean() method takes a Python list as a parameter, calcs average.
print(mean([100, 90]))  # 95

# also works
print(statistics.mean([100, 90]))  # also 95
