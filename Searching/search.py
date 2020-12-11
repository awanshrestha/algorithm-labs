
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i

    return -1

def binary_search(data, lower, higher, target): 
    if higher >= lower: 
        middle = (higher + lower) // 2

        if data[middle] == target: 
            return middle 

        elif data[middle] > target: 
            return binary_search(data, lower, middle - 1, target) 

        else: 
            return binary_search(data, middle + 1, higher, target) 

    else: 
        return -1
