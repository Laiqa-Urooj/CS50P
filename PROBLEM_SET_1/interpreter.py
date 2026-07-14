def main():
     #Assuming the user's input will be in format x y z
    expression = input("Expression: ")
    result = calculate(expression)
    print(f"{result:.1f}")


def calculate(expression):
    #Splitting the string at each whitespace and storing the objects in x operator and z respectively
    x, operator, z = expression.split(" ")
    #Converting string to float
    x = float(x)
    z = float(z)
    #Performing calculations
    if operator == "+":
        return x + z
    elif operator == "-":
        return x - z
    elif operator == "*":
        return x * z
    elif operator == "/":
        return x / z


main()
 

