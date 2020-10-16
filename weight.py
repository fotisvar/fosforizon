weight= int(input("What is your Weight? "))
unit=input("(L)bs or (K)g? ")
units=unit.upper()
converted=[]

if units=="L":
    converted=weight*0.453592
    print(f"Your weight is {converted} kg")
elif units=="K":
    converted=weight/0.453592
    print(f"Your weight is {converted} lbs")
else:
    print("Unit not correct")
