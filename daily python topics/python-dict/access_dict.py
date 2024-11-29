d={"key":"good",
   "joj":67}
print(d)
print(d.keys())
print(d.values())
#access only the keys in the dict
for k in d.keys():
    print(k)
for k in d.values():
    print(k)

#access both keys and values in the dict
#for k,v, d.items():

for k,v in d.items():
    print(k,"=",v)


#printing fav outcome
print(d[joj])


#use the get method to get the value of the key
