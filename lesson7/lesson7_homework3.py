def second_index(text: str, some_str: str) -> int | None:
    first: int = text.find(some_str)  # індекс першого входження

    if first == -1:  # якщо не знайдено жодного входження
        return None

    second: int = text.find(some_str, first + 1)  # індекс другого входження

    if second == -1:  # якщо немає другого входження
        return None

    return second


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('OK')