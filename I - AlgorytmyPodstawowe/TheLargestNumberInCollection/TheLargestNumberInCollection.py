file = open("inputdata.txt", 'r')
lines = file.readlines()
lines = [float(x.strip()) for x in lines]
max = lines[0]
for x in lines:
    if x > max:
        max = x
print("The largest number: " + str(max))

