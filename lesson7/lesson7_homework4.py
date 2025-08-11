def common_elements() -> set[int]:
    # множина чисел, кратних 3 у діапазоні 0–99
    multiples_of_3: set[int] = {x for x in range(100) if x % 3 == 0}

    # множина чисел, кратних 5 у діапазоні 0–99
    multiples_of_5: set[int] = {x for x in range(100) if x % 5 == 0}

    # перетин двох множин (спільні елементи)
    common: set[int] = multiples_of_3 & multiples_of_5

    return common


assert common_elements() == {0, 15, 30, 45, 60, 75, 90}
print("OK")