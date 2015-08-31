l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print l[2:9:2]

to_21 = [x for x in range(1,22)]

odds = to_21[::2]
middle_third = to_21[(len(to_21)/3):2*len(to_21)/3:]

print odds
print middle_third

my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

squares = [x**2 for x in range(1,11)]
print squares
print filter(lambda x: x>=30 and x<=70, squares)


threes_and_fives = [x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]
print "threes_and_fives", threes_and_fives

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x != "X", garbled)
print message

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]




