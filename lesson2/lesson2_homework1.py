number = int(input("Введіть ваші 4 числа: "))

digit4 = number % 10
number = number // 10

digit3 = number % 10
number = number // 10

digit2 = number % 10
number = number // 10

digit1 = number % 10

print(digit1)
print(digit2)
print(digit3)
print(digit4)