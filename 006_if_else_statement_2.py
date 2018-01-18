age=int(input("Enter Now the age \n"))
# this is to test 'and' & 'or' with the if statement
if (age > 15) and (age  < 60):
    print ("go to the work")


if (age < 15) or (age > 60):
    print ("time to enjoy")

# there is no boolena datatype in python
# if string is passed to if statement to check true or false, then it is always true
var="true"

if var:
    print ("name")

#using 'not' in the if
if not(age <18):
    print("eligible for the vote. Vote for BJP")

else:
    print ("come after {} to vote".format(18-age))
