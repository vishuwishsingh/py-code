grade_1 = [9.5,8.5,6.45,21]

grade_1_sum = sum(grade_1)
print(grade_1_sum)
grade_1_len = len(grade_1)
print(grade_1_len)
grade_avg = grade_1_sum/grade_1_len
print(grade_avg)


# create Function 

def mean(myList):
    the_mean = sum(myList) / len(myList)
    return the_mean

print(mean([10,1,1,10]))


def mean_1(value):
    if type(value)== dict:
        the_mean = sum(value.values())/len(value)
        return the_mean
    else:
        the_mean = sum(value) / len(value)
        return the_mean

dic = {"1":10,"2":20}
LIS = [10,20]

print(mean_1(dic))
print(mean_1(LIS))

def mean_2(value):
    if isinstance(value , dict):
        the_mean = sum(value.values())/len(value)
        return the_mean
    else:
        the_mean = sum(value) / len(value)
        return the_mean   

dic_1 = {"1":10,"2":20}
LIS_1 = [10,20]

print(mean_2(dic))
print(mean_2(LIS_1))


def foo(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"




