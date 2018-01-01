name =input("please enter the name \n")
age = int(input("HI " + name + " enter ur age \n"))
print (age)

if age >=18:
    print("vote for BJP")
else:
    print ("better luck nexttime {0}, becaue u are {1}".format(name,age))


print ("enter the number between 1 to 10:")
number=int(input())
if number != 5:
    if number < 5:
        print ("please enter the higher number")
    else:
        print ("enter lower number")

    num2=int(input("Enter now \n"))
    if num2 == 5:
        print("yes, u entered it right")
    else:
        print ("oh oh sorry, u missed the chance")

else:
    print ("u gussed it 1st time.....")