def check_the_number(N):
    list_of_numbers=[]
    result=""
    for i in range(1,5):
        list_of_numbers.append(i)
    if N in list_of_numbers:
        results="True"
    if N not in list_of_numbers:
        results="False"
    return results
N=12
results=check_the_number(N)
print(results)

