import random

lst = [random.randint(1, 100) for _ in range(random.randint(3, 10))]

new_lst = [lst[0], lst[2], lst[-2]]

print("Оригінальний список:", lst)
print("Новий список:", new_lst)

