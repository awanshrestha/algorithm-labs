import itertools

def get_strings(n):
    return [bin(x)[2:].rjust(n,'0') for x in range(2**n)]

def bruteforce(p, w, m):
    n = len(p)
    bit_strings = get_strings(n)
    max_profit = 0
    solution = ''

    for s in bit_strings:
        profit = sum([int(s[i]) * p[i] for i in range(n)])
        weight = sum([int(s[i]) * w[i] for i in range(n)])
    
        if weight <=m and profit > max_profit:
            max_profit = profit
            solution = s
    
    return (solution, max_profit)



def bruteforce_fractional(p, w, m):
    n = len(p)
    ratio = [0] * n
    for z in range(n):
        ratio[z] = p[z] / w[z]
    
    temp = []
    for weight in w:
        bit_strings = get_strings(weight)
        temp.append(bit_strings)
    combination = list(itertools.product(*temp))

    max_profit = 0
    solution = []
    
    for c in combination:
        profit = 0
        weight = 0
        for i in range(n):
            profit += sum([int(c[i][j]) * ratio[i] for j in range(w[i])])
            weight += sum([int(c[i][j]) for j in range(w[i])])

        if weight <=m and profit > max_profit:
            max_profit = profit
            solution = c

    ans = []
    for i in range(n):
        weight_ratio = sum([int(solution[i][j]) / w[i] for j in range(w[i])])
        ans.append(round(weight_ratio,2))
    return(ans, max_profit)


def greedy(profit, weight, Max):
    n = len(profit)
    index = list(range(n))

    priority = [0] * n
    for z in range(n):
        priority[z] = profit[z] / weight[z]
    index.sort(key=lambda i: priority[i], reverse=True)
 
    max_profit = 0
    fractions = [0] * n
    for i in index:
        if weight[i] <= Max:
            fractions[i] = 1
            max_profit += profit[i]
            Max -= weight[i]
        else:
            fractions[i] = Max / weight[i]
            max_profit += profit[i] * (Max/weight[i])
            break
 
    return ( fractions, max_profit )


def dynamic(profit, weight, Max): 
    n = len(profit)
    V = [[0 for x in range(Max + 1)] for x in range(n + 1)] 
    keep = [[0 for x in range(Max + 1)] for x in range(n + 1)] 

    for i in range(n + 1): 
        for x in range(Max + 1): 
            profit1 = profit[i-1] + V[i-1][x-weight[i-1]]
            profit2 =  V[i-1][x]
            if i == 0 or x == 0: 
                V[i][x] = 0
            elif weight[i-1] <= x: 
                V[i][x] = max(profit1, profit2) 
                if (profit1 > profit2):
                    keep[i][x] = 1
            else: 
                V[i][x] = profit2 

    picks = []
    K = Max
    for i in range(n,0,-1):
        if keep[i][K] == 1:
            picks.append(i)
            K -= weight[i-1]
    picks.sort()
    picks = [x-1 for x in picks]
    
    final = ['0' for i in range(n)]
    for z in range(n):
        if z in picks:
            final[z] = '1'
    final = ''.join(final)     

    return (final, V[n][Max])  


#PSEUDO CODE

#BruteForce Pseudo code
# function bruteforce(p, w, m):
#     n = number of items
#     bit_strings = list of strings of length n with all possible combinations of 0 and 1
#     maximumProfit = 0
#     solution = ''

#     for s = 0 to (2^n)
#         profit = sum([int(s[i]) * p[i] for i = 0 to n-1])
#         weight = sum([int(s[i]) * w[i] for i = 0 to n-1])
    
#         if weight <=m AND profit > max_profit then
#             maximumProfit = profit
#             solution = s
#         endif
#     return (solution, maximumProfit)


# function bruteforce_fractional(p, w, m):
#     n = number of items
#     ratio = [0] * len(p)
#     for z = 0 to n
#         ratio[z] = p[z] / w[z]
    
#     temp = []
#     for weight in w:
#         bit_strings = get_strings(weight)
#         temp.append(bit_strings)
#     combination = list(itertools.product(*temp))
#     max_profit = 0
#     solution = []
#     for c in combination
#         profit = 0
#         weight = 0
#         for i = 0 to n
#             profit = profit + sum([int(c[i][j]) * ratio[i] for j in range(w[i])])
#             weight = weight + sum([int(c[i][j]) for j in range(w[i])])

#         if weight <=m AND profit > max_profit:
#             max_profit = profit
#             solution = c
#         endif
#     ans = []
#     for i= 0 to n
#         weight_ratio = sum([int(solution[i][j]) / w[i] for j in range(w[i])])
#         ans.append(round(weight_ratio,2))
#     return(ans, max_profit)



#Greedy ALgo Pseudocode
# function greedy(profit, weight, Max):
#     n = number of items
#     index = list of length n
#     priority = [0] * n
#     for z = 0 to n
#         priority[z] = profit[z] / weight[z]
#     index.sort(key=lambda i: priority[i], reverse=True)
#     max_profit = 0
#     fractions = [0] * n
#     for i in index
#         if weight[i] <= Max then
#             fractions[i] = 1
#             max_profit = max_profit + profit[i]
#             Max = Max - weight[i]
#         else
#             fractions[i] = Max / weight[i]
#             max_profit = max_profit + profit[i] * (Max/weight[i])
#             break
#         endif
#     return ( fractions, max_profit )


# DYnamic Programming Pseudocode
# function dynamic(profit, weight, Max)     
#     n = number of items
#     V = table of n+1 rows and Max+1 columns
#     for i = 0 to n 
#         for x = 0 to Max 
#             if i == 0 OR x == 0 then
#                 V[i,x] = 0
#             else if weight[i-1] <= x then 
#                 V[i,x] = max( V[i-1,x], profit[i-1] + V[i-1, x-weight[i-1]] ) 
#             else 
#                 V[i,x] = V[i-1, x] 
#             endif
#     return V[n,Max]  




