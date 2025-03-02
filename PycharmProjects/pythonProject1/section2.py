def zigzag_encrypt(message, key):
    #message = message.replace(" ", "%").upper()
    matrix = [['' for _ in range(len(message))] for _ in range(key)]
    row = 0
    col = 0
    i = 1
    while col < len(message):
        matrix[row][col] = message[col]
        if row == 0:
            i = 1
        elif row == key - 1:
            i = -1
        row+= i
        col += 1

    encrypted_message = ''
    for j in matrix:
        encrypted_message += ''.join(j)
    return encrypted_message




def zigzag_decrypt(encrypted_message, key):
    #encrypted_message = encrypted_message.replace("%", " ").upper()
    matrix = [['' for _ in range(len(encrypted_message))] for _ in range(key)]
    row = 0
    i = 1
    for col in range(len(encrypted_message)):
        matrix[row][col] = '*'
        if row == 0:
            i=1
        elif row == key - 1:
            i=-1
        row += i

    index = 0
    for r in range(key):
        for c in range(len(encrypted_message)):
            if matrix[r][c] == '*':
                matrix[r][c] = encrypted_message[index]
                index += 1

    row = 0
    i = 0
    decrypted_message = ''
    for col in range(len(encrypted_message)):
        decrypted_message += matrix[row][col]
        if row == 0:
            i = 1
        elif row == key - 1:
            i=-1
        row += i
    return decrypted_message


mod = input("Do you want to encrypt(e) or decrypt(d) your message? ")
if mod == 'e':
    encrypted_Text = zigzag_encrypt(input("Enter a message to encrypt: "), int(input("Enter a key to encrypt: ")))
    print(' Encrypted Message: ', encrypted_Text)
elif mod == 'd':
    decrypted_Text = zigzag_decrypt(input("Enter a message to decrypt: "), int(input("Enter a key to decrypt: ")))
    print('Decrypted Message: ', decrypted_Text)
else:
    print("Wrong input")