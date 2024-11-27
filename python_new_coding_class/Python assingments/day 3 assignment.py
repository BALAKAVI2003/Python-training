#1 sum assignment pdf
x=input("would you like some advice:")
if x=="Y":
    print("If you sleep until lunchtime,you can save your breakfast money")
else:
    print("you don't need advice")

#2 sum assignment pdf
x=int(input("Please enter your score:"))
if x>100 or x<10:
    print("What a great score! Well done")
else:
        print("you need practice")

#3 sum assignment pdf

x=int(input("Please enter the first amount:"))
y=int(input("Please enter the second amount:"))
z=int(input("Please enter the third amount:"))
if x+y+z>1000 or x+y+z==1000:
    print(f"A total of",x+y+z,"was raised")
    print(f"this will be doubled",2*(x+y+z))
else:
    print("the amount was less than 1000 dollars")


# 4 sum assignment pdf

# 4b
    print("Please enter the following values in cm")
    length1 = float(input("Enter the length of rectangle 1: "))
    width1 = float(input("Enter the width of rectangle 1: "))
    area1 = length1 * width1

    length2 = float(input("Enter the length of rectangle 2: "))
    width2 = float(input("Enter the width of rectangle 2: "))
    area2 = length2 * width2

    print(f"Area of rectangle 1: {area1} square units")
    print(f"Area of rectangle 2: {area2} square units")

    if area1 > area2:
        print("Rectangle 1 has a larger area.")
    else:
        if area1 < area2:
            print("Rectangle 2 has a larger area.")



# 5 sum assignment pdf
x=input("would you like some advice?")
if x=="Y" and  "N":
    print("take this advice")
else:
    print("sorry you were asked to enter Y or N")

#6 sum assingment
speed = int(input("Enter the speed you were traveling at (mph): "))
distance = float(input("Enter the stopping distance (m): "))

recommended_distances = {
    20: 6,
    30: 14,
    40: 24,
    50: 38,
    60: 55,
    70: 75
}

if speed in recommended_distances:
    if distance > recommended_distances[speed]:
        print("Warning: Your stopping distance is longer than recommended. Please check your tyres and brakes.")
    else:
        print("Your stopping distance is within the recommended range.")
else:
    print("Invalid speed entered.")

#7 sum
temperature = float(input("Enter the temperature in °C: "))
if temperature <= 0:
    print("The state of water is: Solid")
else:
    if temperature >= 100:
        print("The state of water is: Gas")
    else:
        print("The state of water is: Liquid")

#8  sum
amount = float(input("Enter the amount raised for charity: "))
if amount < 1000:
    total = amount + 100
else:
    if 1000 <= amount <= 2000:
        total = amount * 2
    else:
        total = 2 * 2000 + (amount - 2000)

print(f"The total collected amount after adjustments is: £{total}")



