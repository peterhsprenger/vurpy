hrs = raw_input("Enter Hours:")
h = float(hrs)
if h <= 40:
    salary = h*10.5
else:
    salary = 40*10.5 + (h-40)*(10.5*1.5)
print(salary)