monday_temps = [9.1,8.5,6.8,6.3]

for temp in monday_temps:
    print(round(temp))


for C in "mynameis vishvajeet singh":
    print(C.title())


colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    print(color)

colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    if color > 50:
        print(color)


colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors:
    if isinstance(color, int):
        print(color)

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors:
    if isinstance(color, int) and color > 50:
        print(color)

S_G = {"Hi":1,"Hello":2,"W":3}

for s in S_G.keys():
    print(s)


for s in S_G.items():
    print(s)

for s in S_G.values():
    print(s)   

#############

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print("%s: %s" % (key, value))



##########

print("New")
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for value in phone_numbers.values():
    print(value.replace("+", "00"))