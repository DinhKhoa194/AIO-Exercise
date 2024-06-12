# data[:3] lay cac gia tri thu tu 0,1,2
data=[4,5,6,7,8,9]
print(data[:3])
print(data[2:4])
print(data[::2])
print(data[3])
print(data[-2:5])
# append(a) them gia tri a vao data
data.append(3)
print(data)
# insert(a,b) a: vi tri can them, b gia tri them
data.insert(3,4)
print(data)
# extend(a,b,..) them cac gia tri tren mo rong vao data
data.extend([3,1])
print(data)

# cap nhat gia tri tuong ung
data [0:3]=[1,4,5]
print(data)

# ham pop(x) xoa vi tri index x
data.pop(2)
print(data)

# ham remove(x) xoa gia tri x dau tien
data.remove(1)
print(data)

#ham del

del data[1:3]
print(data)

#ham clear
#data.clear()
#print(data)

data.index(4)
print(data.index(8))

#count
data.count(3)

# Reverse- dao lai thu tu
#data.reversed()
#print(data)

data.sort(reverse=2)
print(data)

#ham sum data
sum=sum(data)
print(sum)

#ham zip 
data1=[1,5,2,3,1,2]
data2=[2,1,9,3,6,1]
for v1, v2 in zip(data1,data2):
    print(v1,v2)

#Ham zip de kiem tra gia tri khac
data1=[1,5,2,3,1,2]
data2=[1,5,2,3,6,1]

tg = True
for v1, v2 in zip(data1,data2):
    if v1!=v2:
        tg= False
        print(v1,v2)
# emnum
data3=['thai','khoa','hoa']
for index, value in enumerate(data3):
    print(index,value)

#sum so chan
def function_sum_chan (data):
    sum1=0
    for value in data:
        if value%2==0:
            sum1= sum1+ value
        return sum1
data3=[1,2,33,2,4]
print(function_sum_chan(data3))

#sum so chan
def sum_1(data):
    result=0
    index=0
    
    while index < len(data):
        if data[index]%2==0:
            result=result+ data[index]
            index+=1
        return result
data3=[1,2,33,2,4]
print(sum_1(data3))

#two_sum
def two_sum (data,target):
    for i, num in enumerate(data):
        complement= target- num
        if complement in data:
            index_comp=data.index(complement)
            return [i,index_comp]
    return []
data=[6,1,2]
target=8
print(two_sum(data,target))
