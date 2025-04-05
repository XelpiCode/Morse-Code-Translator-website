from operator import index

from flask import Flask, render_template
from Forms import InputForm
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ':'/'}

def encrypt(text):
    encryptedTextlist = []
    for letter in text.upper():
        morseLetter = MORSE_CODE_DICT[letter]
        encryptedTextlist.append(morseLetter)
        encryptedTextlist.append(" ")

    encryptedText = "".join(encryptedTextlist)
    return encryptedText

def decrypt(text):
    pass


@app.route("/", methods=["GET", "POST"])
def translate_morse():
    form = InputForm()
    output = "Submit your text"

    if form.validate_on_submit():
        if form.text.data:
            output = encrypt(form.text.data)

        return render_template("index.html", form=form, output=output)

    return render_template("index.html", form=form, output=output)

if __name__ == "__main__":
    app.run(debug=True)
