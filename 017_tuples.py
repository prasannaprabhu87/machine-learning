#tuples
tuples= "a","b","c"
print(tuples)

# to get the item
print (tuples[1])

# to change the tuple (i.e. u need to create new oject)
tuples=tuples[0],"p",tuples[2],tuples[1]
print(tuples)

#unpacking the tuples
music="sitar","flute","tabla"
string,wind,leather=music
print(wind)
print(string)
print(leather)

#Challemge
artist="vilayat","khan","1920",((1970,"USA"),(1980,"london"),(1990,"Delhi"))

player,player2,year,nation=artist
print (player)
print (player2)
print (year)
for k in nation:
    year,country=k
    print (year)
    print (country)
