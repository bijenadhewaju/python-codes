# Create a menu driven program
def menu():
    print("List of services:")
    print("1. BMI Calculator")
    print("2. Taxation System")
    print("3. Currency Converter")
    print("4. Remittance")
    print("5. Lagani Kosh")
    print("6. Exit")
    print("Choose 1-5 to select services or 6 to exit.")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            print("You selected BMI Calculator. The link to the GitHub repository is:\n(https://github.com/bidhyabhattarai/BMI_calculator)")
        elif choice == '2':
            print("You selected Taxation System. The link to the GitHub repository is:\n(https://github.com/Anujakhatri/Taxation-system-nepal)")
        elif choice == '3':
            print("You selected Currency Converter. The link to the GitHub repository is:\n(https://github.com/sneharitas/currency_converter)")
        elif choice == '4':
            print("You selected Remittance. The link to the GitHub repository is:\n(https://github.com/binisha77/nepal_remittance_calculator)")
        elif choice == '5':
            print("You selected Lagani Kosh. The link to the GitHub repository is:\n(https://github.com/kopiladevkota/nepal_lagani_kosh)")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

