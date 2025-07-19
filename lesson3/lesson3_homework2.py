lst = [8, 12, 5, 6]

if len(lst) > 1:
    last = lst.pop()
    lst.insert(0, last)

print(lst)