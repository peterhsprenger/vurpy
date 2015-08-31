
'''
Define a function called count that has two arguments called sequence and item.
Return the number of times the item occurs in the list.

For example: count([1,2,1,1], 1) should return 3 (because 1 appears 3 times in the list).

There is a list method in Python that you can use for this, but you should do it the long way for practice.
Your function should return an integer.
The item you input may be an integer, string, float, or even another list!
Be careful not to use list as a variable name in your code - it's a reserved word in Python!
'''


def count(sequence, item):
    count = 0
    for element in sequence:
        print "Item", item, "Element", element
        if item == element:
            count = count + 1
    print count
    
    
    
s = [1, 4, 3, 4, 5, 6, 4, 4, 1.098, 'a', 'c', 'a', 'd', 'a', 'Verlag', 'Hauptschule', 'Schule', 'Verlag', 'Schule']  
# "4" 4mal, "a" 3mal, "Schule" und "Verlag" 2mal

i = "Schule"

count(s, i)