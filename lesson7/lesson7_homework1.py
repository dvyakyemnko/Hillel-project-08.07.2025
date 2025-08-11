def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"


assert say_hi("Den", 23) == "Hi. My name is Den and I'm 23 years old", 'Test1'
assert say_hi("Rex", 501) == "Hi. My name is Rex and I'm 501 years old", 'Test1'

print('ОК')