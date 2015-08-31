'''
    Write a function called median that takes a list as an input and returns the median value of the list.

    For example: median([1,1,2]) should return 1.

    The list can be of any size and the numbers are not guaranteed to be in any particular order.
    If the list contains an even number of elements, your function should return the average of the middle two.

'''

def median(nl):                         # nl = numberlist
    if len(nl) == 0:
        print len(nl)

    else: 
        for n in nl:
            snl = sorted(nl)
    
        if len(snl) % 2 != 0:
            median = float( snl[ (len(snl) - 1) / 2 ] )
            print median
        else:
            middle1 = float(snl[len(snl) / 2 - 1 ])
            middle2 = float(snl[ len(snl) / 2 ])
            median = (middle1 + middle2) / 2
            print median
    
    
    
numbers1 = [5, 2, 3, 1, 4]             # median: 3 (weil 3 die mittlere Zahl der Liste ist)
numbers2 = [7,3,1,4]                 # median: 3.5 (weil der Mittelwert der beiden mittleren Zahlen 3 und 4 = (3+4)/2 ist
numbers3 = [7,12,3,1,6]              # median: 6 (weil 6 die mittlere Zahl der Liste ist)
numbers0 = []
median(numbers3)