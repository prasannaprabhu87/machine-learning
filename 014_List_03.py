menu=[]
menu.append(["a","b","c"])
menu.append(["b","c","d"])
menu.append(["c","d","e","f"])
menu.append(["z","x","y"])
k=0
for i in menu:

    if "d" not in i:
        print (i , k)

    k+=1
