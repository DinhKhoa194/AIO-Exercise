# Review
# List (Tạo, thêm, sửa, xóa)
# Built-in Functions
# Practice
# B1: input số, output số chẵn, số lẻ
def function_chan_le (n):
    if n%2==0:
        return f"{n}, Chẵn"
    return f"{n},Lẻ"
print(function_chan_le(27))
# B2: tinh tong trong set
def Tong(lst):
    sum=0
    for i in lst:
        sum+=i
    return sum
list1={1,3,3,45,1,2}
print(Tong(list1))
print(list1)

# B3: Loai bo cac so chan ra khoi list


# Slicing: list[start:end"step]


        