
import random
import string

print("===== PASSWORD GENERATOR =====")

print("\nAvailable Character Types:")
print("1. Letters (A-Z, a-z)")
print("2. Letters and Numbers")
print("3. Letters, Numbers and Special Characters")

choice = input("\nSelect password complexity (1-3): ")

length = int(input("Enter password length: "))

if length <= 0:
    print("\nPassword length must be greater than 0.")

else:
    if choice == "1":
        characters = string.ascii_letters

    elif choice == "2":
        characters = string.ascii_letters + string.digits

    elif choice == "3":
        characters = string.ascii_letters + string.digits + string.punctuation

    else:
        characters = ""

    if characters == "":
        print("\nInvalid choice! Please select between 1 and 3.")

    else:
        password = ""

        for i in range(length):
            password = password + random.choice(characters)

        print("\nGenerated Password:", password)
