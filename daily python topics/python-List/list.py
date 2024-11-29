# list -collection of data which can be either of sdame type or different type
# same type : [1,5,7,9]
# different type :[1,0.5,"apple iphone"]
# enclosed within square bracket []
# syntax for creating a normal variable
x = 5
# syntax for creating a list
movies = [1, 2, 3, 4, "sarvesh", "Deepak"]
# syntax for printing a list
print(movies)
# syntax to access a single element in the list
print(movies[0])
print(movies[1])
print(movies[2])
# for loop to access elemnts in the list- iterable
for i in movies:
    print(i)
for i in range(0, len(movies)):
    print(movies[i])

#list allow duplicates - here 67 is repeated
x=[67,2,3,4,67,55,67,67,5]

#list is ordered - here 10  is at index 0, 2 is at index 1, 4 is at index 2,...
y=[10,2,4,1]

#modify list items
movies=["2.0","enthiran","bladerunner"]
movies[1]="saguni"
print(movies)
movies[0:2]=["tamil","kollywood"]
print(movies)

#insert item in the list at the last position : append
movies.append("ocean")
print(movies)

#insert list items  : insert
movies.insert(8,"man vs wild")
print(movies)
movies.insert(10,"avagado")
print(movies)
#add one list to another list at the end : extend
cities=["goa","pirates"]
movies.extend(cities)
print(movies)

#remove item from the list AT THE LAST POSITION : pop
movies.pop()
print(movies)


#remove the first occurence of the specific item : remove
movies.remove("man vs wild")
#remove item at specified index : del keyword
del movies[0]
movies.pop(1)
print(movies)

#clear the VALUES of a list-- clear
movies.clear()
print(movies)

#to delete the entire list
del movies
print(movies)

#
cooling=[1,2,3,"good","bad"]
i=0
for i in cooling:
    print(i)
for i in range(3, len(cooling)):
    print(cooling[i])



