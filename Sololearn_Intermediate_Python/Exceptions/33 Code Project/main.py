"""
Registration System

You are making a registration form for a website.
The form has a name field, which should be more than 3 characters long.
Any name that has less than 4 characters is invalid.
Complete the code to take the name as input, and raise an exception if the name is invalid, outputting "Invalid Name". Output "Account Created" if the name is valid.
"""
try:
    name = input()
    count=0
    for i in name:
      count+=1
      
    if count > 3:
      print("Account Created")
    else:
      raise Exception
except:
    print("Invalid Name")
