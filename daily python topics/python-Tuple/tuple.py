t=("apple","banana","cherry")
print(t)
print(type(t))
#tuples are ordered

print(t[1])
print(t[0])
print(t[2])
#for loop used
for i in t:
    print(i)

#tuple can have duplicate items

t=("apple","guava","banana","apple")
print(t)

#tuple can have different datatypes
t=("apple",1,3.4,2)
print(t)

#lenght of the tuple
print(len(t))

#nested tuple
t=("apple",("guava","wow"),"banana","apple")
print(t)
print(t[1][1])
#reverse order la printing an element
t=("apple",("guava","wow"),"banana","apple")
print(t[-2])

t=("apple",("cool","wow"),"banana","apple")
print(t[-3][-2])
#check if an item is present in the tuple or not
if "apple" in t:
    print("yes")
if 5 not in t:
    print("no")