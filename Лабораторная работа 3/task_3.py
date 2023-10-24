def count_letters(text):
    text = text.lower()
    lower_dict = {}
    for letter in text:
        if letter.isalpha():
            new_element = {letter: text.count(letter)}
            lower_dict.update(new_element)
    return lower_dict


def calculate_frequency(lower_dict):
    amount = sum(lower_dict.values())
    frequency = {}
    for letter in lower_dict:
        new_element = {letter: format((lower_dict.get(letter) / amount), '.2f')}
        frequency.update(new_element)
    return frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

lower_dict = count_letters(main_str)
result_dict = calculate_frequency(lower_dict)

print('\n'.join(f'{key}: {value}' for key, value in result_dict.items()))
