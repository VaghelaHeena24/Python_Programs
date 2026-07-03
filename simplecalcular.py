a=int(input("Enter no 1:"))
b=int(input("Enter no 2:"))

while True:
    print("1. Addition \n 2. Subtraction \n 3.Multiplication \n 4.Division \n 5.Exit")
    ch=int(input("Enter Choice: "))

    if ch==1:
        print("Addition is: ",a+b)
    elif ch==2:
        print("Subtraction is: ",a-b)
    elif ch==3:
        print("Multiplication is: ",a*b)
    elif ch==4:
        print("Division is: ",a//b)
    elif ch==5:
        exit(0)
    else:
        print("Enter Valid Choice")
        
        
        
