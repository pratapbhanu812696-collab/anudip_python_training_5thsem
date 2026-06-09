#from geometry import *

while True:
    print("\n===== 2D FIGURE MENU =====")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:  # Circle
        while True:
            radius = float(input("Enter radius: "))

            print("\n1. Area")
            print("2. Perimeter")
            print("3. Back")

            op = int(input("Select operation: "))

            if op == 1:
                print("Area =", circle_area(radius))
            elif op == 2:
                print("Perimeter =", circle_perimeter(radius))
            elif op == 3:
                break
            else:
                print("Invalid Choice!")

    elif choice == 2:  # Rectangle
        while True:
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))

            print("\n1. Area")
            print("2. Perimeter")
            print("3. Back")

            op = int(input("Select operation: "))

            if op == 1:
                print("Area =", rectangle_area(length, width))
            elif op == 2:
                print("Perimeter =", rectangle_perimeter(length, width))
            elif op == 3:
                break
            else:
                print("Invalid Choice!")

    elif choice == 3:  # Square
        while True:
            side = float(input("Enter side: "))

            print("\n1. Area")
            print("2. Perimeter")
            print("3. Back")

            op = int(input("Select operation: "))

            if op == 1:
                print("Area =", square_area(side))
            elif op == 2:
                print("Perimeter =", square_perimeter(side))
            elif op == 3:
                break
            else:
                print("Invalid Choice!")

    elif choice == 4:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
