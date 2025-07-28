lst = [0, 4, 5, 23, 77, 56, 2, 0 , 2, 6, 0, 3, 0, 67, 78]

original_length = len(lst)
non_zeros = [x for x in lst if x != 0]
zero_count = original_length - len(non_zeros)

lst.clear()
lst.extend(non_zeros)
lst.extend([0] * zero_count)

print(lst)