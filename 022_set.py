# creating the set
farm_animal={"cow","sheep","Hen"}
print(farm_animal)

for animal in farm_animal:
    print (animal)

wild_animal=set(["tiger","lion","elephant"])
print(wild_animal)
for animal in wild_animal:
    print(animal)

# add to set
farm_animal.add("horse")
wild_animal.add("panta")

print (farm_animal,wild_animal)

# union of the set
even=set(range(0,40,2))
print (even)
odd=set(range(1,40,2))
print (odd)
unioneo=even.union(odd)
print (unioneo)
# intersect
intset=set([0,1,3,5,6,23,55])
print(unioneo.intersection(intset))
#Sorted
print(sorted(unioneo))

# set difference
print (unioneo-intset)
print (unioneo.difference(intset))

print (intset-unioneo)

# find differnce and update the set
print (even)
sampleset=set([2,4,6,10])
print (even.difference_update(sampleset))
print(even)

# symmetric difference
print (even.symmetric_difference(sampleset))

#remove the item from set
finalset=set([1,4,9,16,25])
finalset.remove(16)
finalset.discard(9)
print (finalset)


# to check super set and subset
superset=set([2,4,6,8,10])
subset=set([2,4])
if subset.issubset(superset):
    print ("subset is subset of super set")

if superset.issuperset(subset):
    print ("yes correct")
























