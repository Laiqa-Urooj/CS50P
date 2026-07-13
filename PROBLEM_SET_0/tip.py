def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

#Function which removes leading $ sign 
def dollars_to_float(dollars):
    d=float(dollars.removeprefix("$"))
    return d
    
#Function which removes trailing % sign and converts the percentage to float
def percent_to_float(percent):
    removed_percent=float(percent.removesuffix("%"))
    p=removed_percent/100
    return p


main()