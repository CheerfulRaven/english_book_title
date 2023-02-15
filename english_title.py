"""Скрипт форматирует текст как заголовок на английском языке"""

text = input("Введите текст: ")

new_text = []
text = text.split(" ")
# Исключаем слова, которые пишутся со строчной буквы
conjunctions_prepositions = ['but', 'and', 'уet', 'or', 'for', 'so', 'now', 'as', 'why',
                             'how', 'at', 'bar', 'but', 'by', 'in', 'of', 'off', 'on',
                             'out', 'per', 'pro', 'qua', 'to', 'up', 'via', 'from',
                             'above', 'around']
for word in text:
    if word in ['a', 'an', 'the', 'to'] or word in conjunctions_prepositions:
        new_text.append(word.lower())
    else:
        new_text.append(word.title())

# Первое и последнее слово в заголовке пишется со строчной (заглавной) буквы
new_text[0] = new_text[0].title()
new_text[-1] = new_text[-1].title()

new_text = " ".join(new_text)
# В заголовке не должно быть точек в конце предложения.
new_text = new_text.strip('.')
print(new_text)