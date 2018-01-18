fruits={"orange":"Orange fruit",
        "apple":"Red fruit",
        "pear":"green fruit",
        "banana":"yellow fruit"}
veg={"cabbage":"white veg",
     "tomato":"red veg",
     "chilli":"green veg"}

veg.update(fruits)
print (veg)
print (veg.keys())
print(sorted(veg.keys()))