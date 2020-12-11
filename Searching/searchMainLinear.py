import random
from search import linear_search, binary_search
from datetime import datetime

data = random.sample(range(10000000), 1000000)
linearStartBest = datetime.now()
linearIndexBest = linear_search(data, data[0])
linearEndBest = datetime.now()
linearTimeBest = linearEndBest - linearStartBest

linearStartAvg = datetime.now()
linearIndexAvg = linear_search(data, data[50000])
linearEndAvg = datetime.now()
linearTimeAvg = linearEndAvg - linearStartAvg

linearStartWorst = datetime.now()
linearIndexWorst = linear_search(data, data[-1])
linearEndWorst = datetime.now()
linearTimeWorst = linearEndWorst - linearStartWorst

print(f'For Index of {linearIndexBest}.Time taken by linear search {linearTimeBest}')
print(f'For Index of {linearIndexAvg}.Time taken by linear search {linearTimeAvg}')
print(f'For Index of {linearIndexWorst}.Time taken by linear search {linearTimeWorst}')


