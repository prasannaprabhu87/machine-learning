age =input("enter the age")
print ("your age is " + age)

# integer to string converstion
age1=30
print ("your age is " + str(age1))

# replacing the field
print ("there are {0} months with 31 days which includes {1} {2} {3} {4} {5} {6}  " .format(7, "jan","mar","May","Jul","Aug","Oct","Dec"))

print("my %s is %d and %d %s" % ("age",int(age),6,"month"))

# space adding ib formating
for i in range(1, 12):
    print ("%2d sqaure is %4d and cube is %5d" %(i,i**2,i**3))

#decimal point prescribtion
print ("pi value is %.50f" %(22/7))

#OTHER mathod {0:4} means value from 0th position with 4 space
for i in range(1, 12):
    print ("{0:2}sqaure is {1:6} and cube is {2:4}" .format(i,i**2,i**3))


#testing
print ("ths value is {0}".format(22/7))

