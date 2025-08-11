def correct_sentence(text: str) -> str:
    # Перша літера робиться великою, решта тексту залишається без змін
    text = text[0].upper() + text[1:]

    # Якщо в кінці немає крапки, додаємо її
    if not text.endswith('.'):
        text += '.'

    return text


# Тести для перевірки
assert correct_sentence("greetings, dudes") == "Greetings, dudes.", 'Test1'
assert correct_sentence("hi") == "Hi.", 'Test2'
assert correct_sentence("Ciao. Guys") == "Ciao. Guys.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'

print('OK')