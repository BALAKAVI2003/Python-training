#sum of 2 nos.

num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
print("------------------------------------")
print ("sum is",num1+num2)

# day 1 assingments
#no.1 area of triangle
length = int(input("Enter length of the triangle:"))
base = int(input("Enter base of the triangle:"))
area = 1/2 * base * length
print("area of triangle :", area ,"sq units")

#no.2 sum of 3 nos.
num1 = int(input("Enter value of num1:"))
num2 = int(input("Enter value of num2:"))
num3 = int(input("Enter value of num3:"))
sum = num1 + num2 + num3
print("total sum of 3 nos. is =",sum)

#no.3 convert miles into kms
miles = float(input("Enter miles:"))
kms = miles*1.609344
print("converted value of miles to kms =",kms)

#no.4 swap he value of 3 no. in circle order
a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
c = int(input("Enter value of c:"))
a,b,c=b,c,a
print("----------------------------")
print("swaped value of 3 no.s in circle order = ", a,b,c)

#no.5 Find the quotient and remainder
num1 = int(input("Enter value of num1:"))
num2 = int(input("Enter value of num2:"))
quotient = num1//num2
remainder= num1%num2
print("----------------------------")
print("quotient is = ", quotient)
print("remainder is = ", remainder)

#no.6 Join 4 sentences received from the user using four input statement and print it as a paragraph
sentence1 = input("Enter sentence 1:")
sentence2 = input("Enter sentence 2:")
sentence3 = input("Enter sentence 3:")
sentence4 = input("Enter sentence 4:")
paragraph = ' '.join(sentence1+sentence2+sentence3+sentence4)
print("--------------------------")
print("paragraph :",paragraph)

#no.6 edited Join 4 sentences received from the user using four input statement and print it as a paragraph
sentence1 = input("Enter sentence 1:")
sentence2 = input("Enter sentence 2:")
sentence3 = input("Enter sentence 3:")
sentence4 = input("Enter sentence 4:")
paragraph = sentence1+' '+sentence2+' '+sentence3 +' '+sentence4
print("--------------------------")
print("paragraph :",paragraph)


