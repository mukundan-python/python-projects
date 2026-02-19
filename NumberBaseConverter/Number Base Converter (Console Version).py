# Number Base Converter (Console Version)

def decimal_to_binary(decimal):
    return bin(decimal)[2:]  # remove '0b' prefix

def decimal_to_hex(decimal):
    return hex(decimal)[2:].upper()  # remove '0x' prefix

def binary_to_decimal(binary):
    return int(binary, 2)

def hex_to_decimal(hex_value):
    return int(hex_value, 16)

def main():
    print("=== Number Base Converter ===")
    while True:
        print("\nOptions:")
        print("1: Decimal → Binary")
        print("2: Decimal → Hex")
        print("3: Binary → Decimal")
        print("4: Hex → Decimal")
        print("Press Enter to exit")
        
        choice = input("Choose an option: ").strip()
        if choice == "":
            break
        
        value = input("Enter the number: ").strip()
        
        try:
            if choice == "1":
                result = decimal_to_binary(int(value))
            elif choice == "2":
                result = decimal_to_hex(int(value))
            elif choice == "3":
                result = binary_to_decimal(value)
            elif choice == "4":
                result = hex_to_decimal(value)
            else:
                print("Invalid option")
                continue

            print("Result:", result)
        except ValueError:
            print("Invalid input for the selected conversion")

    print("\nGoodbye!")

if __name__ == "__main__":
    main()
