from flask import Flask, render_template, flash, request
from formsBMR import BMRForm
from functionBMR import BMR
from functionProducts import addFood
from formsProducts import ProductForm
from formsBMI import BMIForm
import copy

app = Flask(__name__)
app.secret_key = 'development key'

# zmienne globalne
prodSum = [0, 0, 0, 0, 0]
mealCount = 1

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/produkty/', methods = ['GET', 'POST'])
def exportProducts(productsSum = prodSum):
    global mealCount
    prod_form = ProductForm()

    if request.method == 'POST':
        if prod_form.validate() == False:
            flash('All fields are required.', 'danger')
            return render_template('products1.html', form = prod_form)

        else:
            if request.form['submit_button'] == 'Zatwierdz':
                food = request.form['food']
                grams = request.form['grams']
                intake = addFood(food,grams)
                labels = ['Białko', 'Tłuszcze', 'Węglowodany']
                values = [(intake[2]*4 / intake[0])*100, (intake[3]*9 / intake[0])*100, (intake[1]*4 / intake[0])*100]
                valuesRound = ['%.0f' % el for el in values]
                colors = ["#ABCDEF", "#DDDDDD", "#ABCABC"]
                intakeRound = [ '%.2f' % elem for elem in intake ]
                return render_template('resultProd1.html', intakeRound = intakeRound, set = zip(valuesRound, labels, colors) )

            elif request.form['submit_button'] == 'Dodaj':
                food = request.form['food']
                grams = request.form['grams']
                intake = addFood(food, grams)
                productsSum[0] = productsSum[0] + intake[0]
                productsSum[1] = productsSum[1] + intake[1]
                productsSum[2] = productsSum[2] + intake[2]
                productsSum[3] = productsSum[3] + intake[3]
                productsSum[4] = productsSum[4] + intake[4]
                success = "Dodałeś produkt " + str(mealCount) + " do listy"
                mealCount = mealCount + 1
                return render_template('products2.html', form = prod_form, success = success)

            elif request.form['submit_button'] == 'Oblicz':
                if productsSum[0] == 0:
                    alert = "Nie dodałeś żadnych produktów do listy"
                    return render_template('products2.html', form = prod_form, alert = alert)
                else:
                    productsSumCopy = copy.deepcopy(productsSum)
                    productsSum[0] = 0
                    productsSum[1] = 0
                    productsSum[2] = 0
                    productsSum[3] = 0
                    productsSum[4] = 0
                    mealCount = 1
                    labels = ['Białko', 'Tłuszcze', 'Węglowodany']
                    values = [(productsSumCopy[2]*4 / productsSumCopy[0])*100, (productsSumCopy[3]*9 / productsSumCopy[0])*100, (productsSumCopy[1]*4 / productsSumCopy[0])*100]
                    valuesRound = ['%.0f' % el for el in values]
                    colors = ["#ABCDEF", "#DDDDDD", "#ABCABC"]
                    productsSumCopyRound = ['%.2f' % elem for elem in productsSumCopy]
                    return render_template('resultProd2.html', productsSumCopyRound = productsSumCopyRound, set = zip(valuesRound, labels, colors))

    elif request.method == 'GET':
        return render_template('products1.html', form = prod_form)


@app.route('/BMR/', methods = ['GET', 'POST'])
def formBMR():
    form = BMRForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.', 'danger')
            return render_template('BMR.html', form = form)
        else:
            gender = request.form['gender']
            weight = request.form['weight']
            height = request.form['height']
            age = request.form['age']
            activity = request.form['activity']
            deficit = request.form['deficit']
            result = BMR(gender, weight, height, age, activity, deficit)
            protein = round(0.15*result / 4, 2)
            fat = round(0.3*result / 9, 2)
            carbs = round(0.55*result / 4, 2)
            labels = ['Białko', 'Tłuszcze', 'Węglowodany']
            values = [15,30,55]
            colors = [ "#ABCDEF", "#DDDDDD", "#ABCABC"]
            return render_template('resultBMR.html', result = result, protein = protein, fat = fat, carbs = carbs, set = zip(values, labels, colors))

    elif request.method == 'GET':
        return render_template('BMR.html', form = form)

@app.route('/BMI/', methods = ['GET', 'POST'])
def formBMI():
    form_BMI = BMIForm()

    if request.method == 'POST':
        if form_BMI.validate() == False:
            flash('All fields are required.', 'danger')
            return render_template('BMI.html', form = form_BMI)
        else:
            weight_BMI = request.form['weight_BMI']
            height_BMI = request.form['height_BMI']
            min_weight = round(18.5*(float(height_BMI)/100)**2)
            max_weight = round(24.99*(float(height_BMI)/100)**2)
            def BMI(weight, height):
                return float(weight)/(float(height)/100)**2
            result_BMI = round(BMI(weight_BMI, height_BMI),2)
            return render_template('resultBMI.html', result_BMI = result_BMI, form = form_BMI, height_BMI = height_BMI, min_weight = min_weight, max_weight = max_weight)
    elif request.method == 'GET':
        return render_template('BMI.html', form = form_BMI)

if __name__ == '__main__':
    app.run(debug=True)
