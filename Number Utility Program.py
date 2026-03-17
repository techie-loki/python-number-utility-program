while True:

    print("\nNumber Utility Program")
    print("1. Even or Odd")
    print("2. Factorial")
    print("3. Sum of numbers")
    print("4. Multiplication Table")
    print("5. Exit")

    user_input = int(input("Choose Option : "))

    if user_input == 1:
        print("Welcome to Even or Odd checker")
        number = int(input("Enter the number : "))
        if number%2 == 0:
            print("Even")
        else:
            print("Odd")

    elif user_input == 2:
        print("Welcome to Factorial Checker")
        number = int(input("Enter the number : "))
        total = 1
        for i in range(1,number+1):
            total*=i
        print(f"Factorial : {total}")

    elif user_input == 3:
        print("Welcome to Sum of numbers")
        number = int(input("Enter the number : "))
        total = 0
        for i in range(1,number+1):
            total+=i
        print(f"Sum of number : {total}")

    elif user_input == 4:
        print("Welcome to mathematical tables")
        number = int(input("Enter the number : "))
        for i in range(1,11):
            print(f"{number} * {i} = {number*i}")

    elif user_input == 5:
        print("Exit Programming .............")
        break
    else:
        print("Invalid Input")