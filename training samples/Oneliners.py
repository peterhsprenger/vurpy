choice = raw_input('Enjoying the course? (y/n)')
print choice

while choice != 'y' and choice != 'n':  
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")

print "Thanks"

def digit_sum(n):
    n = str(n)
    digitsum = 0
    for i in n:    
        digitsum += int(i)
    print digitsum
        
number = 12345
digit_sum(number)

def factorial(x):
    factorial = x
    while x > 1:
        factorial = factorial * (x - 1)
        x = x - 1
    print factorial
