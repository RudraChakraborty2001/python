weight = float(input("Enter you weight: "))
unit = input("Kilogams o Pounds? (K or L): ")

if unit=="K":
    weight=weight*2.205
    unit="Lbs."
elif unit=="L":
    weight=weight/2.205
    unit="Kgs."
else:
    print(f"{unit} was not valid")    
print(f"Your weight is: {weight}{unit}") 