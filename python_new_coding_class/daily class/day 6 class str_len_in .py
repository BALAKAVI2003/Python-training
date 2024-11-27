#count number of vowels in a string
#count number of consonants
vowels='aeiouAEIOU'
text=input("enter the text:")
vowel_count=0
consonant_count=0
for i in text:
    if i.isalpha():
      if i in vowels:
        vowel_count+=1 #(vowel_count+1)
      else:
        consonant_count +=1
print("vowel count-",vowel_count)
print("consonant_count-",consonant_count)

#deepak and sarvesh mobile number 986798 8767896
text= "deepak and sarvesh@mobile$%%^number986798 8767896"
alpha_count=0
digit_count=0
for i in text:
    if i.isalpha():
       alpha_count+=1
    if i.isnumeric():
        digit_count+=1
print("alpha count-", alpha_count)
print("digit count-", digit_count)

#slicing
college="SRM Ramapuram"
print(college[1:8:2])
#slice syntax : [start:ed:step]
#by default start is 0, end is last
#character, step is 1
print(college[])