"""
Sololearn variant
i = input()
count = 0
for w in i:
  if w=="a" or w=="e" or w=="i" or w=="o" or w=="u":
    count+=1
print(count)
"""
#My variant
string = input()
count = 0
vowels = "aeiou"
for letter in string:
    for i in vowels:
        if letter == i:
            count+=1
print(count)
