def my_function (list_num=[1,2,5]):
    var=0
    for i in list_num:
        var+=i
    return var/len(list_num)
print(my_function())