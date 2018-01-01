name=['prasanna','divya','disha','pavan','pratap','aanda']
#to append the list
name.append('ravi')

for item in name:
    print("the name is {} and next name is".format(item))

even=[0,2,4,6,8]
odd=[1,3,5,7,9]

allnumber=even+odd
print(allnumber)

#to sort
allnumber.sort()
print(allnumber)

#another way to sort
newnumber=sorted(allnumber)

print(newnumber)


#to remove item
allnumber.remove(2)
print(allnumber)



# list compare
if allnumber==newnumber:
    print ("yes matching ")
else:
    print("not matching")
    allnumber.append(2)
    allnumber.sort()
#after adding the removed 2 in the list and sort.
if allnumber==newnumber:
    print ("yes matching ")
else:
    print("not matching")
    allnumber.append(2)
    allnumber.sort()
