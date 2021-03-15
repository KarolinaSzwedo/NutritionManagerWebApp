def BMR(gender, weight, height, age, activity, deficit):
    const = 10*float(weight) + 6.25*float(height) - 5*float(age)

    if gender == 'M':
        if activity == 'very light':
            if ((const + 5)*1.2)-1000*float(deficit) >= 1200:
                return ((const + 5)*1.2)-1000*float(deficit)
            else:
                return 1200

        elif activity == 'light':
            if ((const + 5)*1.375)-1000*float(deficit) >= 1200:
                return ((const + 5)*1.375)-1000*float(deficit)
            else:
                return 1200

        elif activity == 'moderate':
            if ((const + 5)*1.55)-1000*float(deficit) >= 1200:
                return ((const + 5)*1.55)-1000*float(deficit)
            else:
                return 1200

        elif activity == 'heavy':
            if ((const + 5)*1.725)-1000*float(deficit) >= 1200:
                return ((const + 5)*1.725)-1000*float(deficit)
            else:
                return 1200

        elif activity == 'very heavy':
            if ((const + 5)*1.9)-1000*float(deficit) >= 1200:
                return ((const + 5)*1.9)-1000*float(deficit)
            else:
                return 1200

    else:
        if activity == 'very light':
            if ((const - 161)*1.2)-1000*float(deficit) >= 1200:
                return ((const - 161)*1.2)-1000*float(deficit)
            else:
                return 1200

        elif activity == 'light':
            if ((const - 161)*1.375)-1000*float(deficit) >= 1200:
                return ((const - 161)*1.375)-1000*float(deficit)
            else:
                return 1200

        elif activity == 'moderate':
            if ((const - 161)*1.55)-1000*float(deficit) >= 1200:
                return ((const - 161)*1.55)-1000*float(deficit)
            else:
                return 1200

        elif activity == 'heavy':
            if ((const - 161)*1.725)-1000*float(deficit) >= 1200:
                return ((const - 161)*1.725)-1000*float(deficit)
            else:
                return 1200

        elif activity == 'very heavy':
            if ((const - 161)*1.9)-1000*float(deficit) >= 1200:
                return ((const - 161)*1.9)-1000*float(deficit)
            else:
                return 1200
