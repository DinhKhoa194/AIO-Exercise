def my_function(n):
    min=n[0]
    for i in n:
        if i<min:
            min=i
    return min
list=[1,9,9,0]
print(my_function(list))