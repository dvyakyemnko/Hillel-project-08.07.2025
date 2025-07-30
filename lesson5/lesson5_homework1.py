import string
import keyword

var_name = input("Введіть можливе ім'я змінної: ")

def is_valid_variable(name):

    if name and name[0].isdigit():
        return False

    if any(char.isupper() for char in name):
        return False

    for char in name:
        if char in string.punctuation and char != "_":
            return False
        if char == " ":
            return False

    if name.count("_") > 1 and name.replace("_", "").strip() == "":
        return False

    if name in keyword.kwlist:
        return False

    return True

print(is_valid_variable(var_name))