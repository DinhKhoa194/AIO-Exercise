def max_kernel(num_list,k):
    result=[]
    for i in range(len(num_list)-k+1):
        max=num_list[i]
        for j in range(1,k):
         if num_list[i+j]>max:
            max=num_list[i+j]
        result.append(max)
    return result
num_list=[3,4,5,1,-44,5,10,12,33,1]
k=3
print(max_kernel(num_list,k))