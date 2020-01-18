def TEMP(input_temp):
    if input_temp > 7:
        return "Hot"
    else:
        return "Cold"


use_input =   int(input("Please input Temp :"))

print(use_input)

print(TEMP(use_input))


### String Formatting 


name_1 = input("Enter Your Name :")
print(f"My Name is  {name_1}")

print("My name 222 %s" % name_1)


####################

f_Name = input("First Name :")
l_Name = input("Last Name :")
m_Name = input("M Name :")

print(f"My name is {f_Name} , {l_Name} ,{m_Name}")

def foo(name):
    return "Hi %s" % name.title() 

print(foo("hhhhi"))

