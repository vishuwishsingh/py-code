def area(a,b):
    return a*b

print(area(2,3))

# key word args 

print(area(a=2,b=3))



def area_1(a,b=5):
    return a*b

print(area_1(2))

### add n numbers of args 

def mean(*args):
     return args

print(mean(1,23,'hi'))

def mean(*args):
     return sum(args) / len(args)

print(mean(1,23,22))

### keyword Args 
def mean_keys(**kwargs):
    return kwargs

print(mean_keys(a=1,b=2,c=3))



  