for i in range(1,20):
    print (i)

number='9.23.245.45.34.2234.23'
newnum=''
for i in range(0,len(number)):
    if number[i] in '0123456789':
        newnum=newnum+number[i]

print (newnum)

Newnum2=''
# same program can be written as
for char in number:
    if char in '0123456789':
        Newnum2=Newnum2+char


print (Newnum2)

print ('the correct number is {}'.format(Newnum2))