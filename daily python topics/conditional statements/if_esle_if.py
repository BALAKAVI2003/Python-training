#program to find biggest of 4 nos.
a,b,c,d=10,102,10,10
if a==b and b==c and c==d:
    print("all numbers are equal")
elif a>b and a>c and a>d:
    print(a,"is big number")
elif b>c and b>d :
    print(b,"is big number")
elif c>d:
    print(c, "is big number")
else:
    print(d, "is the biggest number")
print("end of the program")