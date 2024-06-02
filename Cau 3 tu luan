import random
import math

def calculate_loss(num_samples, loss_name):
    # Kiểm tra tính hợp lệ của num_samples
    if not num_samples.isnumeric():
        print('number of samples must be an integer number')
        return

    # Chuyển đổi num_samples sang kiểu int
    num_samples = int(num_samples)

    # Khởi tạo các danh sách để lưu trữ predict và target
    predicts = []
    targets = []

    # Tạo các giá trị ngẫu nhiên cho predict và target
    for i in range(num_samples):
        predict = random.uniform(0, 10)
        target = random.uniform(0, 10)
        predicts.append(predict)
        targets.append(target)
        print(f'sample-{i}: predict={predict:.2f}, target={target:.2f}')

    # Tính toán loss dựa trên loss_name
    if loss_name == 'MAE':
        loss = sum(abs(p - t) for p, t in zip(predicts, targets)) / num_samples
    elif loss_name == 'MSE':
        loss = sum((p - t) ** 2 for p, t in zip(predicts, targets)) / num_samples
    elif loss_name == 'RMSE':
        mse = sum((p - t) ** 2 for p, t in zip(predicts, targets)) / num_samples
        loss = math.sqrt(mse)
    else:
        print('Unsupported loss function')
        return

    # Print ra kết quả
    print(f'\nLoss name: {loss_name}')
    print(f'Loss: {loss:.2f}')

while True:
    # Nhập số lượng sample và loss name từ người dùng
    num_samples = input("Enter the number of samples: ")
    loss_name = input("Enter the loss function name (MAE, MSE, RMSE): ")

    # Gọi hàm calculate_loss với giá trị đầu vào từ người dùng
    calculate_loss(num_samples, loss_name)
    
    # Hỏi người dùng có muốn tiếp tục tính toán không
    continue_calculation = input("Do you want to continue? (yes/no): ").strip().lower()
    if continue_calculation != 'yes':
        break

print("Goodbye!")
