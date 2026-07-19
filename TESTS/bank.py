def main():
    greeting=input("How you doing ?")
    output = value(greeting)
    print(f"${output}")

def value(greeting):
    greeting=greeting.strip().lower() 
    if greeting == "hello":
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()