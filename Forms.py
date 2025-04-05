from wtforms.validators import ValidationError, DataRequired
from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm

def validate_text(form, field):
    allowed_text = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y",
                    "Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x",
                    "y","z","1","2","3","4","5","6","7","8","9","0",".","/","?","-","(",")", " "]
    for letter in field.data:
        if letter not in allowed_text:
            raise ValidationError('Text must only consist of A-Z, a-z, 0-9, ., /, ?, -, (, )')

class InputForm(FlaskForm):
    text = StringField("Input Text", validators=[DataRequired(), validate_text])
    submitText = SubmitField("Translate To Morse Code")
    submitMorse = SubmitField("Translate To English")
