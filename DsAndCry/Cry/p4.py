# Importing the Fernet class from the cryptography library for AES encryption
from cryptography.fernet import Fernet

# Function to generate a random key for encryption
def generate_key():
    return Fernet.generate_key()

# Function to encrypt a file using the provided key
def encrypt_file(key, input_file):
    # Creating a Fernet cipher suite with the provided key
    cipher_suite = Fernet(key)
    
    # Opening and reading the content of the input file in binary mode
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    
    # Encrypting the plaintext using the Fernet cipher suite
    encrypted_data = cipher_suite.encrypt(plaintext)
    return encrypted_data

# Function to decrypt data using the provided key
def decrypt_file(key, encrypted_data):
    # Creating a Fernet cipher suite with the provided key
    cipher_suite = Fernet(key)
    print("\n")
    
    # Decrypting the encrypted data using the Fernet cipher suite
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    return decrypted_data

# Main function to execute file encryption and decryption operations
def main():
    # Infinite loop for user interaction until explicitly exited
    while True:
        # Displaying menu options
        print("==="*10)
        print("AES File Encryption and Decryption")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        choice = input("Enter your choice (1/2): ")
        print("==="*10)

        # Handling user choice
        if choice == '1':
            # Generating a random key for encryption
            key = generate_key()
            print("Key:")
            print(key.decode())
            
            # Taking user input for the file to be encrypted
            input_file = input("Enter the name of the file to encrypt: ")
            
            # Encrypting the file and displaying the result
            encrypted_data = encrypt_file(key, input_file)
            print("Encrypted Text:")
            print(encrypted_data.decode())
            print("\n")

        elif choice == '2':
            # Taking user input for key and encrypted text
            key = input("Enter key: ")
            encrypted_text = input("Enter the encrypted text: ")
            
            # Decrypting the text and displaying the result
            decrypted_data = decrypt_file(key.encode(), encrypted_text.encode())
            print("Decrypted Text:")
            print(decrypted_data.decode())
            print("\n")
            
        else:
            # Displaying an error message for an invalid choice
            print("Invalid choice. Please choose only given alternatives")
    
# Ensuring that the main function is executed only if the script is run as the main program
if __name__ == '__main__':
    main()













