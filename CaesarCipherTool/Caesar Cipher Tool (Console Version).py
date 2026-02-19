def encrypt(text, key):
    key %= 26
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char)-ord("A")+key)%26 + ord("A"))
        elif char.islower():
            result += chr((ord(char)-ord("a")+key)%26 + ord("a"))
        else:
            result += char
    return result

def decrypt(text, key):
    key %= 26
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char)-ord("A")-key)%26 + ord("A"))
        elif char.islower():
            result += chr((ord(char)-ord("a")-key)%26 + ord("a"))
        else:
            result += char
    return result

def main():
    print("=== Caesar Cipher Tool ===")
    while True:
        mode = input("\nEncrypt or Decrypt? (press Enter to exit): ").strip().lower()
        if mode == "":
            break
        elif mode not in ["encrypt", "decrypt"]:
            print("Invalid choice. Type 'encrypt' or 'decrypt'.")
            continue

        text = input("Enter your text: ")
        try:
            key = int(input("Enter key (number): "))
        except ValueError:
            print("Key must be a number.")
            continue

        if mode == "encrypt":
            print("Result:", encrypt(text, key))
        else:
            print("Result:", decrypt(text, key))

    print("\nGoodbye!")

if __name__ == "__main__":
    main()
