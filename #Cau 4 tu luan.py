import math

# Hàm tính giai thừa
def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Hàm ước lượng sin(x)
def estimate_sin(x, n):
    result = 0
    for i in range(n):
        coef = (-1)**i
        num = x**(2 * i + 1)
        denom = factorial(2 * i + 1)
        result += coef * (num / denom)
    return result

# Hàm ước lượng cos(x)
def estimate_cos(x, n):
    result = 0
    for i in range(n):
        coef = (-1)**i
        num = x**(2 * i)
        denom = factorial(2 * i)
        result += coef * (num / denom)
    return result

# Hàm ước lượng sinh(x)
def estimate_sinh(x, n):
    result = 0
    for i in range(n):
        num = x**(2 * i + 1)
        denom = factorial(2 * i + 1)
        result += num / denom
    return result

# Hàm ước lượng cosh(x)
def estimate_cosh(x, n):
    result = 0
    for i in range(n):
        num = x**(2 * i)
        denom = factorial(2 * i)
        result += num / denom
    return result

# Chương trình chính
def main():
    x = float(input("Enter the value of x (in radians): "))
    n = input("Enter the number of terms (positive integer): ")

    if not n.isnumeric() or int(n) <= 0:
        print("Number of terms must be a positive integer greater than 0")
        return
    
    n = int(n)

    sin_approx = estimate_sin(x, n)
    cos_approx = estimate_cos(x, n)
    sinh_approx = estimate_sinh(x, n)
    cosh_approx = estimate_cosh(x, n)

    print(f"sin({x}) ≈ {sin_approx}")
    print(f"cos({x}) ≈ {cos_approx}")
    print(f"sinh({x}) ≈ {sinh_approx}")
    print(f"cosh({x}) ≈ {cosh_approx}")

if __name__ == "__main__":
    main()
