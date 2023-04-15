"""
Lambda

You are given code that should calculate the corresponding percentage of a price.
Somebody wrote a lambda function to accomplish that, however the lambda is wrong.
Fix the code to output the given percentage of the price.
"""
price = int(input())
perc = int(input())

res = (lambda x,y:x*y/100)(price, perc)

print(res)
