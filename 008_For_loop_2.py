# for with list
for name in ["prasanna","Divya","Pavan","Aanda","Durgesh"]:
    print ("HI {} thanks for joining us".format(name))


# For with step increase
for i in range(1,100,5):
    print (i)


# Nesting the loopfo
for i in range (1,13):
    for j in range (1,11):
        print ("{} times {} is {}".format(i,j,i*j,end='\t'))
    print ("+++++++++++++++++++++++")