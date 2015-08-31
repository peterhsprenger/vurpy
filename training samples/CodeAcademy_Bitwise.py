def check_bit(input):
    mask = 0b1000
    desired = input & mask
    if desired > 0:
        return "on"
    else:
        return "off"
i = 15
check_bit(i)


result = 0b1010101 ^ 3
print bin(result)
'''
def flip_bit(number, n):
    result = number << n * -1
    print bin(result)

number = 0b111
n = 2
flip_bit(number, n)
'''