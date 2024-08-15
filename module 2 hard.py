def generate_password(n):
    password = ""
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                password += str(i) + str(j)
    return password


n = int(input('Введите число от 1 до 20: '))
if 1 <= n <= 20:
    result = generate_password(n)
    print(result)
else:
    print("Число не подходит")
