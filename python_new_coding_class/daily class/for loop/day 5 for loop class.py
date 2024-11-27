#even no.
#odd no.
#print natural no.
#from 1 - n
#print whole no.
#from 0 - n

#even no.
for i in range(2,101,2):
    print(i)
#odd no.
for i in range(1,101,2):
    print(i)

#natural no.
n=int(input("enter the last natural no. to be printed:"))
for i in range(1,n+1):
    print(i)
#print whole no.
n=int(input("enter the last whole no. to be printed:"))
for i in range(n+1):
    print(i)