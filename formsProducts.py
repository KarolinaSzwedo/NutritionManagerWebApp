from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, IntegerField, validators, ValidationError
import pandas as pd

data = pd.read_excel("data\\baza_produktow.xlsx")
products = data['produkt'].tolist()
choices = [(product, product) for  product in products]

class ProductForm(FlaskForm):
    food = SelectField('Wybierz produkt', choices = choices)
    grams = IntegerField("Podaj liczbę gramów produktu", [validators.Required("Nie wpisano liczby.")])
    submit = SubmitField("Zatwierdź")
