#take input of number of units consumed from the user
units= int(input("Please enter number of units you consumed: "))

#check conditions of the units consumed
# then calculate amount of surcharge accordingly
#surcharge is the tax charge

# check for units less than 50 
if(units < 50):
    amount=units*2.60
    surcharge=25

# check for the units less than or equal to 100
elif(units <= 100):
    amount=130+((units -50)*3.25)
    surcharge=35

#check for the units less than or equal to 200
elif(units<= 200):
    amount=130+162.50+((units-100)*5.26)
    surcharge=45

#check for all the cases other than mentioned
#toal amount= amount+surcharge
total=amount+surcharge
print("\nElectricity Bill=%.2f" %total)