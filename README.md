
# Caesar Cipher Program

## Overview
This Python program implements a **Caesar Cipher** for both encrypting and decrypting messages. A Caesar Cipher shifts each letter in a message by a fixed number of positions in the alphabet. The program supports uppercase letters and retains non-alphabetic characters (like spaces and punctuation) in their original positions.

## Features
- **Encryption**: Shifts each letter of the message forward by a specified number of positions.
- **Decryption**: Reverses the shift to restore the original message.
- Maintains the case of letters (converts to uppercase for consistency).
- Non-alphabetic characters (spaces, punctuation) remain unchanged during encryption and decryption.

## Prerequisites
- Python 3.x installed on your system.

## How to Run
1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt and navigate to the directory containing the code.
3. Run the program using Python:

   ```bash
   python caesar_cipher.py
   ```

4. Follow the prompts to encrypt or decrypt a message:
   - Enter `1` to encrypt a message.
   - Enter `2` to decrypt a message.
   - Provide the message and the shift value when prompted.

## Example Usage
```
WELCOME TO MY SECRET MESSAGE ARENA

__CAESAR CIPHER PROGRAM__

DO YOU WANT TO ENCRYPT OR DECRYPT YOUR MESSAGE?
Enter 1 to encrypt your message 
Enter 2 to decrypt your message...
Enter 1/2: 1
CIPHER MODE ACTIVATED
input message you want to encrypt: Hello World!
input shift value: 3
CIPHERTEXT: KHOOR ZRUOG!

THANK YOU>>>>
```

### Decryption Example:
```
WELCOME TO MY SECRET MESSAGE ARENA

__CAESAR CIPHER PROGRAM__

DO YOU WANT TO ENCRYPT OR DECRYPT YOUR MESSAGE?
Enter 1 to encrypt your message 
Enter 2 to decrypt your message...
Enter 1/2: 2
DECRYPTION MODE ACTIVATED
input message you want to decrypt: KHOOR ZRUOG!
input shift value: 3
ORIGINAL_TEXT: HELLO WORLD!

THANK YOU>>>>
```

## Code Explanation
### Functions:
- **`encrypt(message, shift)`**:
   - Converts the `message` to uppercase for uniformity.
   - Shifts each uppercase letter forward by the `shift` value using the formula `chr((ord(letter) + shift - 65) % 26 + 65)`.
   - Adds non-alphabetic characters directly to the `ciphertext`.

- **`decrypt(message, shift)`**:
   - Converts the `message` to uppercase.
   - Shifts each letter backward by the `shift` value using the formula `chr((ord(letter) - shift - 65) % 26 + 65)`.
   - Adds non-alphabetic characters directly to the `original_message`.

## Notes
- The shift value should be a positive integer, typically between `1` and `25` for best results, but other values are technically valid due to the modulo operation.
- The program assumes input messages will contain alphabetic characters and may include spaces and punctuation.
- All messages are converted to uppercase to maintain consistency in the encryption/decryption process.

## License
This project is licensed under the MIT License 
## Author
Opeyemi Kayode
