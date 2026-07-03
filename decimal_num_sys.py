
    num = int(input("Enter decimal number: "))

while True:
    print("\n----- Decimal Number System Menu -----")
    print("1. Decimal to Binary")
    print("2. Decimal to Octal")
    print("3. Decimal to Hexadecimal")
    print("4. Exit")

    choice = int(input("Enter your choice: "))


    if choice == 1:
        print("Binary =", bin(num))

    elif choice == 2:
        print("Octal =", oct(num))

    elif choice == 3:
        print("Hexadecimal =", hex(num))
      
    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
