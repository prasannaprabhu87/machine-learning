# creat a list using range

number=list(range(2,10))
print (number)

even=list(range(0,50,2))
odd=list(range(1,50,2))
print(even,odd)
newlist=[even,odd]
print (newlist)

#find the index of the item and item from idenx
aplpha='abcdefghijklmnopqrstuvwxyz'
print(aplpha.index('p'))
print (aplpha[10])

#small program to check whether number is devisible by 7
sevens=range(7,100000,7)
innumber=int(input("enter the number u want\n"))
if innumber  in sevens:
    print ("u have entered correct number")

small_decimal=range(1,100)
samll_decimal2=small_decimal[2:100:3]
print (samll_decimal2)

for i in samll_decimal2:
    print(i)

# reverse the string
string1='python is very powerful'
print (string1[::-1])

# similar to numbers
r=range(0,100,1)
print(r)
for t in r[::-1]:
    print (t)

y=iter(r)
print (y)
for z in y:
    print (z)