def my_function(n):
    max=n[0]
    for i in n:
        if i>max:
            max=i
    return max
my_list=[1,2,3,-1]
print(my_function(my_list))
    
