n = int(input())

file = open("numbers.txt", "w+")

for i in range(1, n+1):
    file.write(str(i)+"")
file.close()


f = open("numbers.txt", "r")
print(f.read())
f.close()
