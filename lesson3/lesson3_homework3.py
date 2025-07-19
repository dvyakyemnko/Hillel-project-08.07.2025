lst = [1, 2, 3]

n = len(lst)
half = (n + 1) // 2

left = lst[:half]
right = lst[half:]

result = [left, right]

print(result)