fruit= {"apple":"red",
        "orange":"orange",
        "banana":"yellow",
        "mango": "yellow"
        }

print(fruit)
print(fruit["mango"])
# to append the item
fruit["pear"]="Green"

print(fruit)

# to update the dictonari
fruit["banana"]="light yellow"
print(fruit)

# delete the key from dictionary
del fruit["banana"]
print (fruit)


while True:
    entere_fruit=input("enter the fruit \n")
    if entere_fruit=='Q':
        break
    if entere_fruit in fruit:
        descrition=fruit.get(entere_fruit)
        print (descrition)
    else:
        print ("not present")

    description1=fruit.get(entere_fruit,"We dont have it " + entere_fruit)
    print (description1)

for item in fruit:
    print ("item in the bag is " + fruit[item])


# sort the dictionaries with the help of list. as we can sort dictionari directly
sorted_list=list(fruit.keys())
sorted_list.sort()
print (40 * '==')
for i in sorted_list:
        print (i + "   " +fruit[i])


#Same can be done
for k in sorted(fruit.keys()):
    print (fruit[k])

# to get keys and the values
print (fruit.keys())
print(fruit.values())

# we can convert dictionaries to tuple and tuple to dictionaries using .item()
i_tuple =tuple(fruit.items())
print (i_tuple)

i_dic=dict(i_tuple)
print (i_dic)