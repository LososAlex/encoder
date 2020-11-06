def afin_encode(text, a, b):
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
                'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    text = text.split()
    encode_text = []
    for i in text:
        i = list(i)
        word = ''
        for j in i:
            if j.isalpha():
                index = alphabet.index(j)
                encode_index = (a * index + b) % 33
                word += alphabet[encode_index]
            else:
                word += j
        encode_text.append(word)
    return encode_text


def afin_decode(text, a, b):
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
                'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    text = text.split()
    decode_text = []
    alt_a = 1
    ans = 1
    while (alt_a * a) % 33 != 1:
        if ans % a != 0:
            ans += 33
        else:
            alt_a = int(ans / a)
    for i in text:
        i = list(i)
        word = ''
        for j in i:
            if j.isalpha():
                index = alphabet.index(j)
                decode_index = ((index - b) * alt_a) % 33
                word += alphabet[decode_index]
            else:
                word += j
        decode_text.append(word)
    return decode_text