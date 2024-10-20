def encrypt(message, shift):
    message = message.upper()
    ciphertext = " "
    for letters in message:
        if letters.isupper():
            ciphertext += chr((ord(letters) + shift - 65) % 26 + 65)
        else:
            ciphertext += letters
    return ciphertext


def decrypt(message, shift):
    message = message.upper()
    original_message = " "
    for letters in message:
        if letters.isupper():
            original_message += chr((ord(letters) - shift - 65) % 26 + 65)
        else:
            original_message += letters
    return original_message

print("WELCOME TO MY SECRET MESSAGE ARENA")
print()
print("__CEASER CIPHER PROGRAM__")

print("DO YOU WANT TO ENCRYPT OR DECRYPT YOUR MESSAGE ?")
print("Enter 1 to encrypt your message \nEnter 2 to decrypt your message...")
user_response =input("Enter 1/2:")
if user_response == "1":
    print("CIPHER MODE ACTIVATED")
    message = input("input message you want to encrypt:")
    shift =int(input("input shift value:"))
    ciphertext = encrypt(message, shift )
    print(f"CIPHERTEXT: {ciphertext}")
    
    
elif user_response == "2":
    print("DECRYPTION MODE ACTIVATED")
    message = input("input message you want to decrypt:")
    shift =int(input("input shift value:"))
    original_message = decrypt(message, shift) 
    print(F"ORIGINAL_TEXT: {original_message}")

print("THANK YOU>>>>")    


print("DO YOU WISH TO PERFORM ANOTHER CEASER CIPHER OPERATION?")
input("yes/no?")
if user_response == "yes":
    print("DO YOU WANT TO ENCRYPT OR DECRYPT YOUR MESSAGE ?")
print("Enter 1 to encrypt your message \nEnter 2 to decrypt your message...")
user_response =input("Enter 1/2:")

if user_response == "1":
    print("CIPHER MODE ACTIVATED")
    message = input("input message you want to encrypt:")
    shift =int(input("input shift value:"))
    ciphertext = encrypt(message, shift )
    print(f"CIPHERTEXT: {ciphertext}")

elif user_response == "2":
    print("DECRYPTION MODE ACTIVATED")
    message = input("input message you want to decrypt:")
    shift =int(input("input shift value:"))
    original_message = decrypt(message, shift) 
    print(F"ORIGINAL_TEXT: {original_message}")

print("THANK YOU>>>>")    