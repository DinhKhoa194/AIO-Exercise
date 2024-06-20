def my_funcion(data):
    var=[]
    for i in data:
        if i%3==0:
            var.append(i)
    return var
print(my_funcion([1,2,3,5,6,7,8,9]))