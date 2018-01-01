#continue
shopping_item=["banana","apple","orange","spam","mango"]
for item in shopping_item:
    if item == "spam":
        print ("ignore the {}".format(item))
        continue
    print (item)


# break=
meal=["papad","rice","sambar","spam","rasum"]
for item1 in meal:
    if item1=="spam":
        print("item is " + item1)
        break
    print (item1)

# Else
meal=["papad","rice","sambar","pickle","rasum"]
for item1 in meal:
    if item1=="spam":
        print("item is " + item1)
        break
else:
    print ("I did not broke it and list time i checked in {}".format(item1))

