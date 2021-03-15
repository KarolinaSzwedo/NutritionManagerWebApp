from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, validators, ValidationError

class BMRForm(FlaskForm):
   gender = RadioField("Płeć:", choices = [('M','Mężczyzna'),('F','Kobieta')], default='M', validators=[validators.Required()])

   weight = IntegerField("Waga (w kg):", [validators.Required("Podano niedopuszczalną wartość."),
                         validators.NumberRange(min=0, max=500, message = 'Podaj wartość z zakresu od 1 do 500')])

   height = IntegerField("Wzrost (w cm):", [validators.Required('Podano niedopuszczalną wartość.'),
                         validators.NumberRange(min=0, max=272, message = 'Podaj wartość z zakresu od 1 do 272')])

   age = IntegerField("Wiek:", [validators.Required("Podano niedopuszczalną wartość."),
                      validators.NumberRange(min=0, max=122, message = 'Podaj wartość z zakresu od 1 do 122')])

   activity = SelectField('Aktywność:', choices = [('very light', 'Bardzo mała aktywność'),
      ('light', 'Mała aktywność'), ('moderate', 'Średnia aktywność'), ('heavy', 'Duża aktywność'), ('very heavy', 'Bardzo duża aktywność')])

   deficit = SelectField("Ile chciałbyś/chciałabyś chudnąć na tydzień?", choices = [('0.25', '0,25 kg'),
      ('0.5', '0,5 kg'), ('1', '1 kg'), ('0', 'Chcę utrzymać wagę')])

   submit = SubmitField("Zatwierdź")
