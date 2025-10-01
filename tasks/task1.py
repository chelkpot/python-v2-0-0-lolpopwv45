# tasks/task1.py

def solve():
# Ниже пишите решение задачи
    s = int(input("Введите число:"))
    a = s//2//2
    b = a
    c = s-a-b
    print(a, c, b)
    
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()