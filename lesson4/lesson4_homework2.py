lst = [1, 2, 3, 4, 5, 6]

if not lst:
    result = 0
else:
    pair_index_sum = 0

    for i in range(0, len(lst), 2):
        pair_index_sum += lst[i]

    result = pair_index_sum * lst[-1]

print(result)



