#Reading1
#Học đặt tên biến
message1="Hello World"
message2="Have a good day"
print(message1)
print(message2)
#Chuoi
student="Mr Khoa"
classname="AIO 2024"
message3=f"{student} hoc tai {classname}"
print( f"{student} hoc tai lap trinh tai {classname}")
print(message3)
lengh=len(message3)
print(lengh)

#Reading2
#Lower/upper/title string
lowermessage3=message3.lower()
uppermessage3=message3.upper()
titlemeseage3=message3.title()
print(lowermessage3)
print(uppermessage3)
print(titlemeseage3)

#Reading3
#Vong lap For
#Cau truc: for variable in iterable :
#Trong đó:
 #• variable là biến sẽ nhận giá trị từng phần tử trong iterable qua mỗi lần lặp.
 #• iterable là một đối tượng có thể lặp, ví dụ như list, tuple, string, dictionary, hoặc range.
for i in range(5):
    print (i)
for i in "Trọng Đạt":
    print (i)
names=["Đạt", "Khoa", "Ngọc"]
for name in names:
    print(name)
student_score={"Khoa":9,"Đat":10,"Ngọc":8}
for student,score in student_score.items():
    print(f"{student}: {score}")
#3. Vòng lặp for trong comprehension
#3.1 List comprehension_Cau truc: [ expression for item in iterable if condition ]
#Trong đó:
#• expression: Biểu thức được áp dụng cho mỗi phần tử.
#• item: Phần tử hiện tại từ iterable.
#• iterable: Bất kỳ đối tượng nào có thể lặp (như danh sách, chuỗi, range, v.v.).
#• condition: (Tùy chọn) Điều kiện để lọc các phần tử.
#Tao danh sach binh phuong so chan
Danhsach=[x**2 for x in range(20) if x%2==0]
print(Danhsach)
#Tao danh sach so chan
Danhsach=[x for x in range(20) if x%2==0]
print(Danhsach)
#3.2 Dictionary comprehension_ Cau truc { key_expression : value_expression for item in iterable if condition }
#Tao dictionary với khóa là số và giá trị là bình phương của số đó
Danhsach_1={x: x**2 for x in range(15)}
print(Danhsach_1)
#4 Vòng lặp for với continue
#In nhung so khong chia het cho 3 tu 1-20
for i in range(20):
    if i%3==0:
        continue
    print(i)
#5 Vòng lặp for với break
#In cac so nho hon 15 tu 1
for i in range(100):
    if i==15:
        break
    print(i)
#6 Vòng lặp for lồng
matrix = [ [1 , 2 , 3,5] ,
           [4 , 5 , 6,1] ,
           [7 , 8 , 9,3]
         ]
for i in range (len ( matrix ) ) :
    for j in range (len ( matrix [ i ]) ) :
        print ( f"Vị trí: ({i} , {j}) , Giá trị: { matrix [i][j]}")
print(len ( matrix ))
print(len ( matrix [i]))

#Reading 4: WHILE LOOP
# cau truc 
#while đ i ề u_ki ệ n :
# Khối code trong while
# VD: nhay 5 lan thi dung lai
has_energy = True
jump_count = 0
while has_energy :
    jump_count += 1
    print ( f" Jump { jump_count } time (s)")
    if jump_count == 5:
       has_energy = False
# Ket hop Break
# In cac so tu 1 den 15
i=1
while i<100:
    print(i)
    if i==15:
        break
    i+=1
# Ket hop Continue
i=1
while i<10:
    print(i*2)
    if i%2==0:
        i+=1
        continue
    i+=1
#Ket hop voi List
fruits = [" apple ", " banana ", " cherry "]
i = 0
while i < len( fruits ) :
    print ( fruits [ i ])
    i += 1

    


