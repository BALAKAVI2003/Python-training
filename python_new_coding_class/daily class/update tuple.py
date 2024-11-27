#value can be changed in tuple by changing the tuple to list data type

t=("apple","juice","banana")
l=list(t)
l[1]="avocado"
print(l)
print(t)
t=tuple(l)
print(t)