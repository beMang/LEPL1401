def quetelet(height, weight):
    bmi = weight/(height**2)
    if bmi < 20:
        return "thin"
    elif 20 <= bmi <= 25:
        return "normal"
    elif 25 < bmi <= 30:
        return "overweight"
    else:
        return "obese"
