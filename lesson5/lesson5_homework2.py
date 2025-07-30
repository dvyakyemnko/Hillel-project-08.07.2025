while True:
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))
    operation = input("Введіть дію (+, -, *, /): ")

    if operation == "+":
        result = a + b
        print("Результат:", result)
    elif operation == "-":
        result = a - b
        print("Результат:", result)
    elif operation == "*":
        result = a * b
        print("Результат:", result)
    elif operation == "/":
        if b == 0:
            print("Помилка! Ділення на нуль неможливе.")
        else:
            result = a / b
            print("Результат:", result)
    else:
        print("Невідома операція!")

    cont = input("Бажаєте продовжити (y/n)? ")
    if cont.lower() != "y":
        print("Калькулятор завершив роботу.")
        break