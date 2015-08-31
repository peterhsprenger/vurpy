def wage(hours_str, rate_str):
    try:
        hours = float(hours_str)
        rate = float(rate_str)
        salary = hours * rate
        return salary
    except:
        print "You didn't use numbers, try again"
hours_str = raw_input("Enter the hours of your work? \n")
rate_str = raw_input("Enter the rate of your work? \n")
wage(hours_str, rate_str)
print wage(hours_str, rate_str)