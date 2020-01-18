## Build a Maker

def sent(input):
    intr =  ("How","Why","Who")
    cap = input.capitalize()
    if cap.startswith(intr):
        return "{} ?".format(cap)
    else :
        return "{}".format(cap)

# print(sent("how are you"))

result = []

while True:
    user_input = input("Say Somthing :")
    if user_input == '\end':
        break
    else:
        result.append(sent(user_input))

print(" ".join(result))


















