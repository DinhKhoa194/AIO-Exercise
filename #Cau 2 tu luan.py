import math

def activation_function (name,x):
  # Chuyển đổi x sang kiểu float
    try:
        x = float(x)
    except ValueError:
        print('Input x is not a valid float')
        return
    # Kiểm tra tên hàm kích hoạt
    valid_functions = ['sigmoid', 'relu', 'elu']
    if name not in valid_functions:
        print(f'{name} is not supported')
        return
  # Giá trị alpha cho hàm ELU
    alpha = 0.01
    # Tính toán theo hàm kích hoạt tương ứng
    if name == 'sigmoid':
        result = 1 / (1 + math.exp(-x))
    elif name == 'relu':
        result = max(0, x)
    elif name == 'elu':
        result = x if x >= 0 else alpha * (math.exp(x) - 1)
      # Print ra kết quả
    print(f'Result for {name} with input {x}: {result}')

 # Lấy giá trị x và tên hàm kích hoạt từ người dùng
x_input = input("Enter the value of x: ")
function_name = input("Enter the activation function (sigmoid, relu, elu): ")

while True:
    # Lấy giá trị x và tên hàm kích hoạt từ người dùng
    x_input = input("Enter the value of x: ")
    function_name = input("Enter the activation function (sigmoid, relu, elu): ")

    # Gọi hàm activation_function với giá trị đầu vào từ người dùng
    activation_function(function_name, x_input)
    
    # Hỏi người dùng có muốn tiếp tục tính toán không
    continue_calculation = input("Do you want to continue? (yes/no): ").strip().lower()
    if continue_calculation != 'yes':
        break

print("Goodbye!")