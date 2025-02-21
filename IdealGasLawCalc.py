print("Varible must be capital.")

Unknown = input("What is the unknown variable?:")
if Unknown == "P":

    v = float(input("What is the volume in L?"))
    n = float(input("How many moles of the gas are there?"))
    r = float(0.082)
    t = float(input("What temperature is the gas  in K?"))
    Answer = (n * r * t) / v
    RoundAnswer = round(Answer, 4)
    print(RoundAnswer)
elif Unknown == "V":
    p = float(input("What is the pressure in atm?"))
    n = float(input("How many moles of the gas are there?"))
    r = float(0.082)
    t = float(input("What temperature is the gas  in K?"))
    Answer = (n * r * t) / p
    RoundAnswer = round(Answer, 4)
    print(RoundAnswer)
elif Unknown == "N":
    p = float(input("What is the pressure in atm?"))
    v = float(input("What is the volume in L?"))
    r = float(0.082)
    t = float(input("What temperature is the gas in K?"))
    Answer = (p * v) / (r * t)
    RoundAnswer = round(Answer, 4)
    print(RoundAnswer)
elif Unknown == "T":
    p = float(input("What is the pressure in atm?"))
    v = float(input("What is the volume in L?"))
    r = float(0.082)
    t = float(input("What temperature is the gas  in K?"))
    Answer = (p * v) / (n * r)
    RoundAnswer = round(Answer, 4)
    print(RoundAnswer)
else:
    print("Please enter P, V, N, or T")