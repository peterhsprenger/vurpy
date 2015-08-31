def is_prime(x):
    n = 2
    if x < 2:
        print "False"
    else:
        while n <= x :
            if x % n == 0 and x / n != x and x != n:
                print "False, x can be devided by:", n
                break
            else:
                n = n + 1
        else:
            print "True"
        
is_prime(3)

# bei 0 False, bei 1 False, bei 2 True, bei 3 True