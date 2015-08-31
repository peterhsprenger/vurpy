def computepay(hrs, rate):
    h = float(hrs)
    r = float(rate)
    if h <= 40:
        salary = h*r
        return salary
    else:
        salary = 40*r + (h-40)*(r*1.5)
        return salary

hrs = raw_input("Enter Hours")
rate = raw_input("Enter Rate")
salary = computepay(hrs, rate)
print salary