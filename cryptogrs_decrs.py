import json
import requests

key1 = 'qwertyuiopasdfghjklzxcvbnm'
key2 = 'ёйцукенгшщзхъфывапролджэячсмитьбю'


def caesar_cipher(text, shift):
    shift = int(shift)
    encrypted_text = ""
    for char in text:
        if char.lower() in key1 or char.lower() in key2:
            if char.lower() in key1:
                if char.isupper():
                    new_char = chr((ord(char.lower()) - 97 + shift) % 26 + 97).upper()
                    encrypted_text += new_char
                else:
                    new_char = chr((ord(char) - 97 + shift) % 26 + 97)
                    encrypted_text += new_char
            elif char.lower() in key2:
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
    shift = int(shift)
    decrypted_text = ""
    for char in text:
        if char.lower() in key1 or char.lower() in key2:
            if char.lower() in key1:
                if char.isupper():
                    new_char = chr((ord(char.lower()) - 97 - shift) % 26 + 97).upper()
                    decrypted_text += new_char
                else:
                    new_char = chr((ord(char) - 97 - shift) % 26 + 97)
                    decrypted_text += new_char
            elif char.lower() in key2:
                if char.isupper():
                    new_char = chr((ord(char.lower()) - 1072 - shift) % 33 + 1072).upper()
                    decrypted_text += new_char
                else:
                    new_char = chr((ord(char) - 1072 - shift) % 33 + 1072)
                    decrypted_text += new_char
        else:
            decrypted_text += char
    return decrypted_text


def encrypt(text):
    global key1, key2
    cipher_dict = {}
    cipher_dict2 = {}
    for i in range(len(key1)):
        cipher_dict[chr(i + 97)] = key1[i]
    for i in range(len(key2)):
        if (i + 1072 > 1078) and i + 1072 < 1105:
            cipher_dict2[chr(i + 1071)] = key2[i]
        elif i + 1072 == 1078:
            cipher_dict2[chr(1105)] = key2[i]
        elif i + 1072 < 1078:
            cipher_dict2[chr(i + 1072)] = key2[i]
    cipher_text = ''
    for char in text:
        if char.lower() in key1 or char.lower() in key2:
            if char.lower() in key1:
                if char.isupper():
                    cipher_text += cipher_dict[char.lower()].upper()
                else:
                    cipher_text += cipher_dict[char]
            elif char.lower() in key2:
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
            decipher_dict2[key2[i]] = chr(i + 1072)
    text = ''
    for char in cipher_text:
        if char.lower() in key1 or char.lower() in key2:
            if char.lower() in key1:
                if char.isupper():
                    text += decipher_dict[char.lower()].upper()
                else:
                    text += decipher_dict[char]
            elif char.lower() in key2:
                if char.isupper():
                    text += decipher_dict2[char.lower()].upper()
                else:
                    text += decipher_dict2[char]
        else:
            text += char
    return text


def split_len(text, length):
    return [text[i:i + length] for i in range(0, len(text), length)]


def encode(key, text):
    key = int(str(key))
    cells = {int(i): r for r, i in enumerate(range(key))}
    encrypted = ''
    for index in sorted(cells.keys()):
        for part in split_len(text, key):
            try:
                encrypted += part[cells[index]]
            except IndexError:
                continue
    return encrypted


def deencode(key, text):
    key = int(key)
    number = 0
    cells = {int(i): r for r, i in enumerate(range(key))}
    for _ in sorted(cells.keys()):
        for _ in split_len(text, key):
            try:
                number += 1
            except IndexError:
                continue
    return encode(int(number / key), text)


def transcription1(text):
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
    if q[-1] == '-':
        return ' '.join(q)[0:-1]
    else:
        return ' '.join(q)


def transcription2(text):
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
    if ' '.join(q)[-1] == '-':
        return ' '.join(q)[0:-1]
    else:
        return ' '.join(q)


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
    if q[-1] == '-':
        return ' '.join(q)[0:-1]
    else:
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
    if ' '.join(q)[-1] == '-':
        return ' '.join(q)[0:-1]
    else:
        return ' '.join(q)


def geoshifr(text, city):
    q = []
    e = []
    d = {}
    for r, char in enumerate(text):
        if char.lower() in key1 or char.lower() in key2:
            if char.lower() in key1:
                if char.isupper():
                    q.append(key1.index(char.lower()) + 26)
                else:
                    q.append(key1.index(char.lower()))
            elif char.lower() in key2:
                if char.isupper():
                    q.append(key2.index(char.lower()) + 33 + 52)
                else:
                    q.append(key2.index(char.lower()) + 52)
        else:
            d[r] = char
    geocoder_request = f"http://geocode-maps.yandex.ru" \
                       f"/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={city}&format=json"
    response = requests.get(geocoder_request)
    for i in q:
        e.append(chr(sorted(set(response.content))[i]))
    variable = '-'.join(e) + " |/_ " + '#&'.join(list(map(lambda x: str(x)+'-'+d[x], d)))
    return variable


def degeoshifr(text, city):
    w = []
    d = {}
    if len(str((text.split(' |/_ ')[1]))) > 1:
        d = dict(map(lambda x: (int(str(x).split('-')[0]), str(x).split('-')[1]), str(text.split(' |/_ ')[1]).split('#&')))
    encrypted_text = ''
    geocoder_request = f"http://geocode-maps.yandex.ru" \
                       f"/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={city}&format=json"
    response = requests.get(geocoder_request)
    for i in ''.join(text.split(' |/_ ')[0]).split('-'):
        w.append(sorted(set(response.content)).index(ord(i)))
    c = [0, 0, False]
    for r, i in enumerate(w):
        c[0] = r
        if (c[0] in d.keys()) and not c[2]:
            c[2] = True
        while c[1] + c[0] in d.keys():
            encrypted_text += d[c[1] + c[0]]
            c[1] += 1
        if i <= 52:
            if i > 26:
                encrypted_text += key1[i - 26].upper()
            else:
                encrypted_text += key1[i]
        else:
            if i > 33 + 52:
                encrypted_text += key2[i - 33 - 52].upper()
            else:
                encrypted_text += key2[i - 52]
    if len(encrypted_text) in d.keys():
        for i in list(d.keys()):
            if i > len(encrypted_text) - 1:
                encrypted_text += d[i]
    return encrypted_text
