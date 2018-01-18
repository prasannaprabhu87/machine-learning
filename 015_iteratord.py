string='0123456789'
my_string=iter(string)
print(my_string)
print (next(my_string))
print (next(my_string))
#chanllenge
lenght=len(string)
print(lenght)

for char in string:
    print (char)

#same code as above written using iter function
for char in iter(string):
    print (char)


# challenge
day=["mon","the","wed","thr","fir","sat","sun"]
days=iter(day)
for item in range(0,len(day)):
    newname=next(days)
    print (newname)