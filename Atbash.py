def atbash(text):
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
                'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    alt_alphabet = alphabet[::-1]
    text = text.split()
    answer_text = []
    for i in text:
        i = list(i)
        word = ''
        for j in i:
            if j.isalpha():
                word += alt_alphabet[alphabet.index(j)]
            else:
                word += j
        answer_text.append(word)
    return answer_text
