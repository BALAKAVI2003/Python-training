#remove function
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#using disscard we cant find error
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#pop
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#clear function

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#del function

thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)