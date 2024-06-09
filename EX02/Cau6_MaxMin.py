def my_fuction(data,max,min):
    result=[]
    for i in data:

        if i< min:
            result.append(min)
        elif i>max:
            result.append(max)
        else:
            result.append(i)
    return result
my_list=[10,2,5,0,1]
max=2
min=1
#print(my_fuction(max=max,min=min,data=my_list))
print(my_fuction(my_list,max,min))