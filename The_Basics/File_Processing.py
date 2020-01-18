myfile = open("fruits.txt")

print(myfile.read()) 

# store content in veriable to print multiple times 

file = open("fruits.txt")
read_1 = file.read()
print(read_1)

# print first 90 char  
file = open("fruits.txt")
content = file.read()
file.close()
print(content[:90])


# number of character in file 
def foo(character, filepath="fruits.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character)


## open file with   -- no need to close after that 

with open("fruits.txt") as myfile:
    content = myfile.read()

print("----")
print(content)


## file in diffrent payth 

mynew_file = open("new/fruits_1.txt")
print(mynew_file.read())

## write data 

my_date = open("new/veg.txt" , 'w')
my_date.write("pppppp")


with open("new/veg_1.txt" , 'w') as new_file:
    new_file.write("Hi \n My \n name \n is")
    new_file.write("VishvaJeet")


### seek to reset the curser  
with open("data.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.seek(0)
    file.write(content)
    file.write(content)

    