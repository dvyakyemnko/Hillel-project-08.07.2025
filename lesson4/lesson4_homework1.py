lst = [0, 5, 6, 0, 9, 55, 43, 19, 0, 0, 5, 3, 6, 18]

non_zeros = [x for x in lst if x != 0]

zero_count = len(lst) - len(non_zeros)

result = non_zeros + [0] * zero_count

print(result)