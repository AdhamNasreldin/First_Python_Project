weight = input("Please enter your weight ")
unit = input("(K)g or (L)bs ")
if unit == "k" or unit == "K":
    print("Weight in pounds = " + str(float(weight)*2.2046))
else:
    weight =float(weight) /2.2046
    print("Weight in pounds = " + str(float(weight)))

height = input('Please enter your height ')
unit = input(" (M) or (i)nche ")
if unit == "m" or unit == "M":
    print("Height in Inches = " + str(float(weight)*3.28084))
else:
    height =float(height) /3.28084
    print("Weight in pounds = " + str(float(weight)))

BMI = float(weight) / (float(height) ** 2)
print("Your BMI is "+ str(BMI))
if BMI < 18.5:
    print("You are under weight , What about having a delicious meal ")
elif  BMI < 25:
    print("You are on a normal body weight, Enjoy your life. ")
else:
    print("You are Overweight I recommend you start a diet plan.")