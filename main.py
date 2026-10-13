"""
Demo-Git-Team - file code mau de thuc hanh quy trinh Git/GitHub nhom.
Leader: Hiep | Developer: Tinh | Developer: Nhut Anh
"""

def greet(name):
    # Dong 6
    return f"Nhut anh Xin chao ban Kim tinh, {name}!"
    return f" xin chào mình là tình, {name}!"
def greet(name):    
    return f"Xin chào mình là Nhut Anh, {name}!"    

def add(a, b):
    # Dong 11 -> Tinh se sua dong nay (vi du them kiem tra kieu du lieu)
    a= 100 # Tình mới sửa nè
    return a + b
def add(a, b):
    # Dong 11 -> Tinh se sua dong nay (vi du them kiem tra kieu du lieu)
    a= 2026 
    b = 0 
     # Tình mới sửa nè
    return a + b

def subtract(a, b):
    a = 1000 #  new
    b = 500 #  new
    # Dong 16
    return a - b


def multiply(a, b):
    a = 1000
    b = 2000 #nhutanh moi sua ne 
    return a * b


def divide(a, b):
    # Dong 26
    if b == 0:
        return "Khong the chia cho 0"
    return a / b


def main():
    print(greet("Nhom Demo-Git-Team"))
    print("2 + 3 =", add(2, 3))
    print("5 - 2 =", subtract(5, 2))
    print("4 * 6 =", multiply(4, 6))
    print("10 / 2 =", divide(10, 2))


if __name__ == "__main__":
    main()
