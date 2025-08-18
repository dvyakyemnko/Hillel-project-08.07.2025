def popular_words(text: str, words: list[str]) -> dict[str, int]:
    text_lower: list[str] = text.lower().split()
    result: dict[str, int] = {word: text_lower.count(word) for word in words}
    return result


assert popular_words(
    '''When I was One I had just begun When I was Two I was nearly new ''',
    ['i', 'was', 'three', 'near']
) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'

print('OK')