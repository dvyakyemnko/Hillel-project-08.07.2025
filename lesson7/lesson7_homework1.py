def say_hi(name: str, age: int) -> str:
    """
    Повертає привітання з ім'ям та віком.

    :param name: Ім'я користувача (рядок)
    :param age: Вік користувача (ціле число)
    :return: Рядок у форматі "Hi. My name is {name} and I'm {age} years old"
    """
    return f"Hi. My name is {name} and I'm {age} years old"

# Перевірка роботи функції через тести
assert say_hi(name="Den", age=23) == "Hi. My name is Den and I'm 23 years old", 'Test1'
assert say_hi(name="Rex", age=501) == "Hi. My name is Rex and I'm 501 years old", 'Test2'

print('OK')