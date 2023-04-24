from flask import Flask, render_template, request
from data import db_session
from data.text import Text
from dec_enc_form import *

from cryptogrs_decrs import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main(text_):
    db_session.global_init("db/blogs.db")
    user = Text()
    user.text = text_
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


def last_entry():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    user = db_sess.query(Text).all()
    last = user[-1].text
    db_sess.query(Text).filter(Text.text == user[-1].text).delete()
    db_sess.commit()
    return last


@app.route('/', methods=['GET', 'POST'])
def encryption():
    en_form = EncryptionForm()
    if en_form.validate_on_submit():
        if request.method == 'POST':
            if en_form.ciphers_list.data == '1':
                en_form.text_input.data = encrypt(en_form.text_input.data)
                main(en_form.text_input.data)
            elif en_form.ciphers_list.data == '2':
                en_form.text_input.data = encode(en_form.keys_encryption.data, en_form.text_input.data)
                main(en_form.text_input.data)
            elif en_form.ciphers_list.data == '3':
                en_form.text_input.data = transcription1(en_form.text_input.data)
                main(en_form.text_input.data)
            elif en_form.ciphers_list.data == '4':
                en_form.text_input.data = transcription2(en_form.text_input.data)
                main(en_form.text_input.data)
            elif en_form.ciphers_list.data == '5':
                en_form.text_input.data = geoshifr(en_form.text_input.data, en_form.keys_encryption.data)
                main(en_form.text_input.data)
            else:  # Цезарь
                en_form.text_input.data = caesar_cipher(en_form.text_input.data, en_form.keys_encryption.data)
                main(en_form.text_input.data)
    return render_template('encrypt.html', title='Шифрование', form=en_form)


@app.route('/decryption', methods=['GET', 'POST'])
def decryption():
    de_form = DecryptionForm()
    if de_form.validate_on_submit():
        if request.method == 'POST':
            if de_form.ciphers_list2.data == '1':
                de_form.text_input2.data = decrypt(de_form.text_input2.data)
            elif de_form.ciphers_list2.data == '2':
                de_form.text_input2.data = deencode(de_form.keys_encryption2.data, de_form.text_input2.data)
            elif de_form.ciphers_list2.data == '3':
                de_form.text_input2.data = detranscription1(de_form.text_input2.data)
            elif de_form.ciphers_list2.data == '4':
                de_form.text_input2.data = detranscription2(de_form.text_input2.data)
            elif de_form.ciphers_list2.data == '5':
                de_form.text_input2.data = degeoshifr(de_form.text_input2.data, de_form.keys_encryption2.data)
            else:
                de_form.text_input2.data = caesar_decipher(de_form.text_input2.data, de_form.keys_encryption2.data)
    return render_template('decrypt.html', title='Расшифрование', form=de_form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
