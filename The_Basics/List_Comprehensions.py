# inline for loops 

list_1 = [224,225,226,227]
print(list_1)

list_2 = [lis / 10 for lis in list_1]

print(list_2)

def foo(lst):
    return [i if not isinstance(i, str) else 0 for i in lst ]

