import pandas as pd
data = pd.read_excel("data/baza_produktow.xlsx")

def addFood(food, grams):
    intake = []
    series = data[data.produkt == food]
    intake.extend(series.calories * float(grams)/100)
    intake.extend(series.carbs * float(grams)/100)
    intake.extend(series.protein * float(grams)/100)
    intake.extend(series.fat * float(grams)/100)
    intake.extend(series.fiber * float(grams)/100)
    
    return intake
