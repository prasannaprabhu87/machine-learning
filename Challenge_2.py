ipaddress=input("plase enter the IP address \n")
seglen=0
segment=''
dotcount=0
totaldotcount=0
countdot=0
countipp=0
for k in ipaddress:
    if k  in '.':
        countdot+=1
        countipp+=1
    else:
        countipp+=1

if (countdot == 3) and (countipp >= 7) and (ipaddress[0] in '0123456789') and (ipaddress[-1] in '0123456789'):

    for i in ipaddress:

        if i in '.':
            seglen=0
            segment=''
            dotcount +=1
            totaldotcount+=1
            if (dotcount > 1) or (totaldotcount > 3):
                print("Invalid IP")
                break
        elif i in '0123456789':
            seglen += 1
            segment += i
            dotcount=0
            if (seglen > 3) or (int(segment) > 255):
                print ("invalid IP")
                break
        elif i in '\n':
            print ("Not valid")
        else:
            print ("Not a valid IP")
            break
    else:
        print ("U have entered valid IP {}".format(ipaddress))

else:
    print ("invalid IP address")