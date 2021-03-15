from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, validators, ValidationError

class BMIForm(FlaskForm):
   weight_BMI = IntegerField("Waga (w kg):", [validators.Required("Podano niedopuszczalną wartość."),
                             validators.NumberRange(min=0, max=500, message = 'Podaj wartość z zakresu od 1 do 500')])
   height_BMI = IntegerField("Wzrost (w cm):", [validators.Required('Podano niedopuszczalną wartość.'),
                             validators.NumberRange(min=0, max=272, message = 'Podaj wartość z zakresu od 1 do 272')])
   submit = SubmitField("Zatwierdź")
