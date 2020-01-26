import time

number = 0 

print("Welcome to Number Counter ")
# input("How Many people wants to play Number Counter :" )
Name = input("What is Your Name :")
Location = input("Where are you from :")
count_by = int(input("Count by ?? "))

print(f"Hi {Name} from {Location} py Number Counter , count by {count_by} ")

 
i = 0 

if count_by == 1:
    i=1
elif count_by ==2: 
    i=2
else:
    i= count_by  

for i in range(i, 101, count_by):
    time.sleep(1)
    print("This is Number :  ",i)