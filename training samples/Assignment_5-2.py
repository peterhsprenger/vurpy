# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except 
# and put out an appropriate message and ignore the number. 
# Enter the numbers from the book for problem 5.1 and Match the desired output as shown.
largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : 
        break
    elif largest is None:
        try:
            largest = int(num)
            smallest = int(num)
            # print "Smallest so far 1st =", smallest, "Largest so far 1st =", largest
            continue
        except:
            print "You didn't enter a valid number: "
            continue
    else:
        try:
            largest_so_far = int(num)
            smallest_so_far = int(num)
            if largest < largest_so_far:
                largest = largest_so_far
            elif smallest > smallest_so_far:
                smallest = smallest_so_far
            # print "Smallest so far =", smallest, "Largest so far =", largest
            continue
        except:
            print "You didn't enter a valid number: "
            continue
print "Maximum =", largest, "- Minimum =", smallest