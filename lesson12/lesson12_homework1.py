import codecs

def delete_html_tags(html_file: str, result_file: str = 'cleaned.txt') -> None:
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html: str = file.read()

    cleaned_text: list[str] = []
    inside_tag: bool = False

    for char in html:
        if char == '<':
            inside_tag = True
        elif char == '>':
            inside_tag = False
        elif not inside_tag:
            cleaned_text.append(char)

    text: str = ''.join(cleaned_text)
    lines: list[str] = [line.strip() for line in text.splitlines() if line.strip()]
    result: str = "\n".join(lines)

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(result)