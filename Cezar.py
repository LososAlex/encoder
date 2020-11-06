def cezar_encode(text, key):
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
                'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    text = text.split()
    text_encode = []
    for i in text:
        i = list(i)
        word = ''
        for j in i:
            if j.isalpha():
                index = alphabet.index(j)
                if index + key >= len(alphabet):
                    index = index + key - len(alphabet)
                else:
                    index += key
                word += alphabet[index]
            else:
                word += j
        text_encode.append(word)
    return text_encode


def cezar_decode(text, key):
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
                'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    text = text.split()
    text_decode = []
    for i in text:
        i = list(i)
        word = ''
        for j in i:
            if j.isalpha():
                index = alphabet.index(j)
                if index - key < 0:
                    index = index - key + len(alphabet)
                else:
                    index -= key
                word += alphabet[index]
            else:
                word += j
        text_decode.append(word)
    return text_decode
