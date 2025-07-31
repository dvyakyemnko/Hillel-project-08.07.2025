seconds = int(input("Введіть кількість секунд (0–8640000): "))

day_sec = 24 * 60 * 60  # 86400

days, remainder = divmod(seconds, day_sec)

hours, remainder = divmod(remainder, 3600)

minutes, seconds = divmod(remainder, 60)

if days == 1:
    day_word = "день"
elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
    day_word = "дні"
else:
    day_word = "днів"

print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")