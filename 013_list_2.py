#creating empty list
list1=[]
list2=list()
print (list1,list2)
#to check list 1 an 2
print (list2 is list1)


#list from the string
print (list("started"))

#assing the list to other and if we update new list, it will show it in 1st list also

even=[2,4,6,8]
neweven=even
print(neweven)
print (neweven is even)
neweven.sort(reverse=True)
print(neweven is even)

#assging the list useing list()
neweven2=list(even)
print(neweven)
print (neweven is even)
neweven.sort(reverse=True)
print(neweven is even)
print(neweven,even)

#list of list
a=[2,4,6,8]
b=[1,3,5,7,9]
aandb=[a,b]
print(aandb)


# using loops
for i in aandb:
    print(i)

    for j in i:
        print (j)