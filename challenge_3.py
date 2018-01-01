import random
highest=10
ran=random.randint(1,highest)
change=3
while change > 0:
    answer=int(input("enter the ur number \n"))
    if answer != ran:
        if answer < ran:
            print ("enter higher number")
        else:
            print ("lower number")

    else:
        print ("your nummber {} and random number {} is matcing ".format(answer,ran))
        break

    change-=1

else:
    print ("chance is over.... Sorry !!!!!!!!! number was {}".format(ran))