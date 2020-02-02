# GUI Widfets with Call Back Function 

from tkinter import *

def km_to_miles():
    print(e1_value.get())
    # END is Place to insert text
    miles = float(e1_value.get())*1.6
    t1.insert(END,miles)

window = Tk()

# b1 = Button(window , text="Hello" )

b1 = Button(window , text="Hello" , command= km_to_miles )
# b1.pack()
b1.grid(row=0 , column=0 )

e1_value= StringVar()
e1 = Entry(window , textvariable = e1_value)

e1.grid(row=0 , column=1 )

t1 = Text(window , height = 1 , width = 20)
t1.grid(row=0 , column=2)

window.mainloop()

