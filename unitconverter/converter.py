def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def m_to_yards(meters):
    return meters * 1.09361

def yards_to_m(yards):
    return yards / 1.09361

def m_to_km(meters):
    return meters / 1000

def km_to_m(km):
    return km * 1000

def miles_to_yards(miles):
    return miles * 1760

def yards_to_miles(yards):
    return yards / 1760

def print_menu():
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Meters to Yards")
    print("4. Yards to Meters")
    print("5. Meters to Kilometers")
    print("6. Kilometers to Meters")
    print("7. Miles to Yards")
    print("8. Yards to Miles")
    print("9. Quit")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            km = float(input("Enter kilometers: "))
            print("Miles:", km_to_miles(km))
        elif choice == '2':
            miles = float(input("Enter miles: "))
            print("Kilometers:", miles_to_km(miles))
        elif choice == '3':
            meters = float(input("Enter meters: "))
            print("Yards:", m_to_yards(meters))
        elif choice == '4':
            yards = float(input("Enter yards: "))
            print("Meters:", yards_to_m(yards))
        elif choice == '5':
            meters = float(input("Enter meters: "))
            print("Kilometers:", m_to_km(meters))
        elif choice == '6':
            km = float(input("Enter kilometers: "))
            print("Meters:", km_to_m(km))
        elif choice == '7':
            miles = float(input("Enter miles: "))
            print("Yards:", miles_to_yards(miles))
        elif choice == '8':
            yards = float(input("Enter yards: "))
            print("Miles:", yards_to_miles(yards))
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
