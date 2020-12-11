from knapSack import dynamic, bruteforce, greedy, bruteforce_fractional

def run():
    p = [5, 6, 7, 2] 
    w = [4, 2, 3, 1] 
    m = 8

    print('BruteForce 0/1 : ',bruteforce(p, w, m))
    print('BruteForce Fractional: ',bruteforce_fractional(p, w, m))
    print('Greedy Fractional: ',greedy(p, w, m))
    print('Dynamic Programming 0/1: ',dynamic(p, w, m))

if __name__ == '__main__':
    run()
