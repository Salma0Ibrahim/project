def columnar_encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper() #Removes spaces-Converts to uppercase
    num_columns = len(key) #The number of columns is determined by the length of the key.
    num_rows = -(-len(plaintext) // num_columns)  # The number of rows is calculated using ceiling division to ensure the plaintext fits into the grid.
    plaintext = plaintext.ljust(num_rows * num_columns, 'X')  #Ensures the plaintext fills the grid completely by appending the letter 'X' as padding.

    key_order = sorted(range(len(key)), key=lambda x: key[x]) #To determine the order in which the columns are read, based on the numerical values of the key
    cipher_text = ''.join(
        ''.join(plaintext[row * num_columns + col] for row in range(num_rows))
        for col in key_order
    ) #defines the order in which the columns are read, based on sorting of the encryption key (either numeric or alphabetic).
    return cipher_text

def columnar_decrypt(ciphertext, key):
    num_columns = len(key)
    num_rows = len(ciphertext) // num_columns
    key_order = sorted(range(len(key)), key=lambda x: key[x]) #To determine the order in which the columns are read, based on the numerical values of the key

    columns = [''] * num_columns
    idx = 0 #Tracks the current position in the ciphertext string as we extract characters for each column.
    for col in key_order:
        columns[col] = ciphertext[idx:idx + num_rows]
        idx += num_rows

    decrypted_text = ''.join(''.join(row[col] for col in range(num_columns)) for row in zip(*columns))
    return decrypted_text


def main():
    # Asking the user whether they want to encrypt or decrypt
    action = input("Do you want to encrypt or decrypt a message? (Enter 'encrypt' or 'decrypt'): ").strip().lower()

    if action == 'encrypt':
        plaintext = input("Enter the message to encrypt: ").strip()
        key = input("Enter the key (integer or string): ").strip()
        encrypted_message = columnar_encrypt(plaintext, key)
        print("Encrypted message:", encrypted_message)

    elif action == 'decrypt':
        ciphertext = input("Enter the ciphertext to decrypt: ").strip()
        key = input("Enter the key (integer or string): ").strip()
        decrypted_message = columnar_decrypt(ciphertext, key)
        print("Decrypted message:", decrypted_message)

    else:
        print("Invalid action. Please enter 'encrypt' or 'decrypt'.")