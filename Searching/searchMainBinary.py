import random
from search import binary_search
from datetime import datetime

data = random.sample(range(10000000), 1000000)
data = sorted(data)
middle = data[(len(data) - 1) // 2]
binaryStartBest = datetime.now()
binaryIndexBest = binary_search(data, 0, len(data) -1, middle)
binaryEndBest = datetime.now()
binaryTimeBest = binaryEndBest - binaryStartBest

binaryStartAvg = datetime.now()
binaryIndexAvg = binary_search(data, 0, len(data)-1, data[24000])
binaryEndAvg = datetime.now()
binaryTimeAvg = binaryEndAvg - binaryStartAvg

binaryStartWorst = datetime.now()
binaryIndexWorst = binary_search(data, 0, len(data)-1, -1)
binaryEndWorst = datetime.now()
binaryTimeWorst = binaryEndWorst - binaryStartWorst

print(f'For Index of {binaryIndexBest}.Time taken by binary search {binaryTimeBest}')
print(f'For Index of {binaryIndexAvg}.Time taken by binary search {binaryTimeAvg}')
print(f'For Index of {binaryIndexWorst}.Time taken by binary search {binaryTimeWorst}')


