#This is a python project about converting temperature

temp=int(input("What is the temperature today? ")) #an den valeis to int() tha pareis string

unit=input("(F)ahrenheit or (C)elcius? ")

if unit.upper()=="F":
    converted=((temp-32)*5)/9
    print(f"Today is {converted} Celsius")
else:
    converted=(temp/5)*9+32
    print(f"Today is {converted} Fehrenheit")
