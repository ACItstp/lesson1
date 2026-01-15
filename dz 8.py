a = float(input("Введіть число a: "))
b = float(input("Введіть число b: "))
vidpovid = input("Введіть операцію (+, -, *, /): ")

if vidpovid == "+":
    print("Результат:", a + b)
elif vidpovid == "-":
    print("Результат:", a - b)
elif vidpovid == "*":
    print("Результат:", a * b)
elif vidpovid == "/":
    if b == 0:
        print("Ділення на нуль")
    else:
        print("Результат:", a / b)
else:
    print("Невідома операція")
