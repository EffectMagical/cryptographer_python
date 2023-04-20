from flask import Flask, render_template, redirect, make_response, jsonify

from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, InputRequired

from flask_restful import reqparse, abort, Api, Resource

from cryptogrs_decrs import *


class EncryptionForm(FlaskForm):
    text_input = TextAreaField("Поле для ввода", validators=[InputRequired()], render_kw={'rows': 20, 'cols': 100})
    caesar = SubmitField('Цезарь')
    submit2 = SubmitField('Шифр2')
    submit3 = SubmitField('Транскрипция1')
    submit4 = SubmitField('Транскрипция2')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/encryption', methods=['GET', 'POST'])
def encryption():
    form = EncryptionForm()
    if form.validate_on_submit():
        if form.caesar.data:
            pass
            # form.text_input.
        elif form.submit2.data:
            pass
        elif form.submit3.data:
            pass
        elif form.submit4.data:
            pass
    return render_template('encrypt.html', title='Шифрование', form=form)


# @app.errorhandler(404)
# def not_found(error):
#     return make_response(jsonify({'error': 'Not found'}), 404)


# @app.errorhandler(400)
# def bad_request(_):
#     return make_response(jsonify({'error': 'Bad Request'}), 400)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
