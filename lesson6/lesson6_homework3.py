number = int(input("Введіть число: "))

while number > 9:
    product = 1
    while number > 0:
        digit = number % 10
        product *= digit
        number //= 10
    number = product

print(number)