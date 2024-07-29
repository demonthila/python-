weight = float(input("What is your weight? "))

mode = input("What do you want to convert? Just enter 'K' for pounds to kilograms or 'L' for kilograms to pounds: ").upper()

if mode == "K":
    total = weight * 0.45359237
    print("Weight in kilograms is " + str(total))
elif mode == "L":
    total = weight * 2.20462
    print("Weight in pounds is " + str(total))
else:
    print("Your input is not correct. Please enter 'K' or 'L'.")
