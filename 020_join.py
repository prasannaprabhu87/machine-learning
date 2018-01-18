a='abcdefghijklmnopqrstuvwxyz'
b=','.join(a)
print(b)
d='1234567890'
e=' number '.join(d)
print(e)

# this is he game
place={6:"u are in Hegde",
       1: "U r in kumta",
       2:"u r in karki",
       3: "u r in bangalore",
       4:"u r in sirsi",
       5: "U are in Tumkur",
       0:"you are about to quit"}
direction=[{"Q":0},{"H":6,"K":1,"B":3,"S":4},{"K":2,"H":6},{"T":5},{"S":4,"T":5}, {"T":5,"Q":0},{"B":3}]
startat=1
while True:
    present_palce=''
    for item in direction[startat].keys():
        present_palce+= ' ' + item

    if startat==0:
        break
    print ("enter the place u want to go" + present_palce)
    place_test=input().upper()
    if place_test in direction[startat]:
        palace_value=direction[startat][place_test]
        print ("you are in " + place[palace_value])
        print(palace_value)
        startat=palace_value
    else:
        print ("not valid ")

