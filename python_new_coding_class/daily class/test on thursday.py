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
