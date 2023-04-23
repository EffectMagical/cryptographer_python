import json

key1 = 'qwertyuiopasdfghjklzxcvbnm'
key2 = 'ёйцукенгшщзхъфывапролджэячсмитьбю'


def caesar_cipher(text, shift):  # 1 шифр (Цезарь)
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char in key1:
                if char.isupper():
                    new_char = chr((ord(char.lower()) - 97 + shift) % 26 + 97).upper()
                    encrypted_text += new_char
                else:
                    new_char = chr((ord(char) - 97 + shift) % 26 + 97)
                    encrypted_text += new_char
            else:
                if char.isupper():
                    new_char = chr((ord(char.lower()) - 1072 + shift) % 33 + 1072).upper()
                    encrypted_text += new_char
                else:
                    new_char = chr((ord(char) - 1072 + shift) % 33 + 1072)
                    encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text


def caesar_decipher(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char in key1:
                if char.isupper():
                    new_char = chr((ord(char.lower()) - 97 - shift) % 26 + 97).upper()
                    decrypted_text += new_char
                else:
                    new_char = chr((ord(char) - 97 - shift) % 26 + 97)
                    decrypted_text += new_char
            elif char in key2:
                if char.isupper():
                    new_char = chr((ord(char.lower()) - 1072 - shift) % 33 + 1072).upper()
                    decrypted_text += new_char
                else:
                    new_char = chr((ord(char) - 1072 - shift) % 33 + 1072)
                    decrypted_text += new_char
        else:
            decrypted_text += char
    return decrypted_text


def encrypt(text):  # 2 шифр
    global key1, key2
    cipher_dict = {}
    cipher_dict2 = {}
    for i in range(len(key1)):
        cipher_dict[chr(i+97)] = key1[i]
    for i in range(len(key2)):
        if (i + 1072 > 1078) and i + 1072 < 1105:
            cipher_dict2[chr(i + 1071)] = key2[i]
        elif i + 1072 == 1078:
            cipher_dict2[chr(1105)] = key2[i]
        elif i + 1072 < 1078:
            cipher_dict2[chr(i+1072)] = key2[i]
    cipher_text = ''
    for char in text:
        if char.isalpha():
            if char in key1:
                if char.isupper():
                    cipher_text += cipher_dict[char.lower()].upper()
                else:
                    cipher_text += cipher_dict[char]
            elif char in key2:
                if char.isupper():
                    cipher_text += cipher_dict2[char.lower()].upper()
                else:
                    cipher_text += cipher_dict2[char]
        else:
            cipher_text += char
    return cipher_text


def decrypt(cipher_text):
    global key1, key2
    decipher_dict = {}
    decipher_dict2 = {}
    for i in range(len(key1)):
        decipher_dict[key1[i]] = chr(i + 97)
    for i in range(len(key2)):
        if (i + 1072 > 1078) and i + 1072 < 1105:
            decipher_dict2[key2[i]] = chr(i + 1071)
        elif i + 1072 == 1078:
            decipher_dict2[key2[i]] = chr(1105)
        elif i + 1072 < 1078:
            decipher_dict2[key2[i]] = chr(i+1072)
    text = ''
    for char in cipher_text:
        if char.isalpha():
            if char in key1:
                if char.isupper():
                    text += decipher_dict[char.lower()].upper()
                else:
                    text += decipher_dict[char]
            elif char in key2:
                if char.isupper():
                    text += decipher_dict2[char.lower()].upper()
                else:
                    text += decipher_dict2[char]
        else:
            text += char
    return text


def split_len(text, length):  # 3 шифр - ?
    return [text[i:i + length] for i in range(0, len(text), length)]


def encode(key, text):
    number = 0
    cells = {int(i): r for r, i in enumerate(range(key))}
    encrypted = ''
    for index in sorted(cells.keys()):
        for part in split_len(text, key):
            try:
                number += 1
                encrypted += part[cells[index]]
            except IndexError:
                continue
    with open('number.txt', 'w', encoding='utf=8',) as f:
        f.write(str(int(number / key)))
    number /= key
    return encrypted


def transcription1(text):  # 4 шифр
    q = []
    with open('tyu2.json', encoding='utf-8') as f:
        d = json.load(f)[1]
    for i in text.split():
        r = ""
        for j in i:
            if j.upper() not in d:
                r += j
            else:
                if j.isupper():
                    r += d[j].upper() + '-'
                else:
                    r += d[j.upper()].lower() + '-'
        q.append(r)
    return ' '.join(q)[0:-1]


def transcription2(text):  # 5 шифр
    q = []
    with open('tyu2.json', encoding='utf-8') as f:
        d = json.load(f)[0]
    for i in text.split():
        r = ""
        for j in i:
            if j.upper() not in d:
                r += j
            else:
                if j.isupper():
                    r += d[j].upper() + '-'
                else:
                    r += d[j.upper()].lower() + '-'
        q.append(r)
    return ' '.join(q)[0:-1]


def detranscription1(text):
    q = []
    with open('tyu2.json', encoding='utf-8') as f:
        d = json.load(f)[1]
    for i in text.split():
        r = ""
        for j in i.split('-'):
            if j.upper() not in d.values():
                r += j
            else:
                if j.isupper():
                    for p, g in enumerate(d.values()):
                        if g == j:
                            r += list(d.keys())[p]
                            break
                else:
                    for p, g in enumerate(d.values()):
                        if g == j.upper():
                            r += list(d.keys())[p].lower()
                            break
        q.append(r)
    return ' '.join(q)


def detranscription2(text):
    q = []
    with open('tyu2.json', encoding='utf-8') as f:
        d = json.load(f)[0]
    for i in text.split():
        r = ""
        for j in i.split('-'):
            if j.upper() not in d.values():
                r += j
            else:
                if j.isupper():
                    for p, g in enumerate(d.values()):
                        if g == j:
                            r += list(d.keys())[p]
                            break
                else:
                    for p, g in enumerate(d.values()):
                        if g == j.upper():
                            r += list(d.keys())[p].lower()
                            break
        q.append(r)
    return ' '.join(q)
