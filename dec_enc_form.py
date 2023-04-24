from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, validators, SelectField


class EncryptionForm(FlaskForm):
    ciphers_list = SelectField('Шифры', choices=[(0, 'Цезарь'), (1, 'Шифр'), (2, 'Квадратный'),
                                                 (3, 'Транскрипция1'), (4, 'Транскрипция2'), (5, 'Геошифр')])
    keys_encryption = TextAreaField("Введите переменную", [validators.InputRequired(),
                                                           validators.Length(max=100)], render_kw={'rows': 1, 'cols': 5})
    text_input = TextAreaField("Введите текст (макс символов: 1000)", [validators.InputRequired(),
                                                                       validators.Length(max=1000,
                                                                                         message='Макс. символов: 1000')],
                               render_kw={'rows': 15, 'cols': 60})
    cipher_btn = SubmitField('Зашифровать')


class DecryptionForm(FlaskForm):
    ciphers_list2 = SelectField('Шифры', choices=[(0, 'Цезарь'), (1, 'Шифр'), (2, "Квадратный"),
                                                  (3, 'Транскрипция1'), (4, 'Транскрипция2'), (5, 'Геошифр')],
                                default=0)
    keys_encryption2 = TextAreaField("Введите переменную", [validators.InputRequired(),
                                                           validators.Length(max=100)], render_kw={'rows': 1, 'cols': 5})
    text_input2 = TextAreaField("Введите текст (макс символов: 1000)", [validators.InputRequired(),
                                                                        validators.Length(max=1000,
                                                                                          message='Макс. символов: 1000')],
                                render_kw={'rows': 15, 'cols': 60})
    decipher_btn = SubmitField('Расшифровать')