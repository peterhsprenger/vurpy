year_of_birth = raw_input("What is your year of birth? ")
try:
    year_of_birth = int(year_of_birth)
    your_age = 2015 - year_of_birth
except:
    print "This was not a number"
    continue in line 1