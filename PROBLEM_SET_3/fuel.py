#Take x/y format input from user
#divide the x with y and round off to .2f and *100 add %sign
#if %1 or less output E
#if %99 or more output F
#Catch errors like zerodivision error and valuerror

def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percent = calculate_percent(fraction)
            break
        except (ValueError, ZeroDivisionError):
            pass

    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{round(percent)}%")


def calculate_percent(f):
    x, y = f.split("/")
    x = int(x)
    y = int(y)
    
    if x > y:
        raise ValueError
    return (x / y) * 100

main()
        