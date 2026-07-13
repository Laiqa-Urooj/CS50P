#Taking user input for mass
mass = int(input("Enter mass(kg):"))
#Initializing the speed of light
c=300000000
#Calculation E=mc^2
#Spaces around operators is good practice
energy = mass * (c ** 2)
#Printing energy
print(f"Energy is : {energy:,}")