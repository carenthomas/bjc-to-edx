import random
def testrand(iterations):
    d = {}
    d['iterations'] = iterations
    for i in range(10):
        d[i] = 0
    for i in range(iterations):
        d[random.randrange(10)] += 1
    return(d)

def printhist(histogram):
    for value in range(10):
        print("="* (histogram[value] // (histogram['iterations']//10)))

