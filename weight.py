weight= int(input("What is your Weight? "))
unit=input("(L)bs or (K)g? ")
converted=[]

if unit.upper()=="L":
    converted=weight*0.453592
    print(f"Your weight is {converted} kg")
elif unit.upper()=="K":
    converted=weight/0.453592
    print(f"Your weight is {converted} lbs")
else:
    print("Unit not correct, type 'L' for libre and 'K' for kilos")
