import json
from difflib import SequenceMatcher
from difflib import get_close_matches

# load JSON File 
data = json.load(open("data.json","r"))

# Function to return value for key as user input
def key_value(u_input):
    u_input = u_input.lower()
    if u_input in data:
        return data[u_input]
    elif len(get_close_matches(u_input , data.keys())) > 0 :  
        u_input_y_n = input("Did you mean %s insted Enter Y for Yes or No to Exit :" % get_close_matches(u_input , data.keys())[0]) 
        if u_input_y_n == "Y" or u_input_y_n == "y":
            return data[get_close_matches(u_input , data.keys())[0]]
        elif u_input_y_n == "N" or u_input_y_n == "n" :
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry"
    else:
        return "Word Does not exist"
    
 
# user input
user_input = input("Say Somthing :")
#print(key_value(user_input))
output = key_value(user_input)

if type(output)== list:
    for item in output:
        print(item)
else:
    print(output)


