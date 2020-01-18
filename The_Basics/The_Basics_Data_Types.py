import datetime

mynow = datetime.datetime.now()
print("My datetime is " , mynow)

mynumber = 10 
mytext = "Hello"

print(mynumber, mytext)

x = 10
y = "10"
z = 10.1
sum1 = x+x
sum2 = y+y

print(sum1 , sum2)
print(type(x), type(y), type(z))

## List Type 
grade = [9.5,8.5,6.45]
## range - We can use ragne to create list automatically 
test_range = list(range(1,10))
print(test_range)

test_range_by_3 = list(range(1,20,2))
print(test_range_by_3)

rainfall = [10.0,10,'Test',[1,2,3,4]]
print(rainfall[2])

######### use dir() for help(str.upper)  ## use q for quit help 

## built in function dir(__builtins__)

grade_1 = [9.5,8.5,6.45,21]

grade_1_sum = sum(grade_1)
print(grade_1_sum)
grade_1_len = len(grade_1)
print(grade_1_len)
grade_avg = grade_1_sum/grade_1_len
print(grade_avg)


## dict 
dict_grade = {"Kar":10,"Tes":10,"Vis":10}
dict_grade_sum = sum(dict_grade.values())
dict_grade_len = len(dict_grade.values())
dict_grade_avg = dict_grade_sum/dict_grade_len 

print(dict_grade_avg)

## tuple has () and cannot add any new valuse  ... 

day_temperatures = {'morning': (1.1 , 2.2, 3.4), 'noon': (2.3, 4.5, 3.1), 'evening': (2.4, 3.5, 6.5)}














