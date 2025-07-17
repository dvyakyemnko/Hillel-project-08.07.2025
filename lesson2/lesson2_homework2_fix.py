number = int(input("Введіть число з 5-ти цифр: "))

digit5 = number % 10
digit4 = number % 100 // 10
digit3 = number % 1000 // 100
digit2 = number % 10000 // 1000
digit1 = number % 100000 // 10000

reversed = digit5 * 10000 + digit4 * 1000 + digit3 * 100 + digit2 * 10 + digit1

print(reversed)