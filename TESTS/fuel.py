def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percent = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            pass
    print(gauge(percent))

def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if x > y:   
        raise ValueError
    percent =  (x / y) * 100
    return int(percent)

def gauge(percent):
    if percent <= 1:
        return "E"
    elif percent >= 99:
        return "F"
    else:
        return f"{percent}%"

if __name__ == "__main__":
    main()