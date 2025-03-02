def zigzag_encrypt(message, key):
    #message = message.replace(" ", "%").upper()
    matrix = [['' for _ in range(len(message))] for _ in range(key)]
    row = 0
    col = 0
    i = 1
    while col < len(message):
        matrix[row][col] = message[col] #put message into matrix row and column
        if row == 0:
            i = 1 #move down
        elif row == key - 1:
            i = -1 #move up
        row+= i #+1 then move row
        col += 1 #+1 then move column

    encrypted_message = '' #Initializes an empty string to store the encrypted message
    for j in matrix: #each row (j) in the zigzag matrix.
        encrypted_message += ''.join(j) # (join j)joins all the characters in the current row (j) into a single string remove spaces
                                        # (encrypted message +=)Appends the row’s string to the growing encrypted_message.
    return encrypted_message




def zigzag_decrypt(encrypted_message, key):
    #encrypted_message = encrypted_message.replace("%", " ").upper()
    matrix = [['' for _ in range(len(encrypted_message))] for _ in range(key)]
    row = 0
    i = 1
    for col in range(len(encrypted_message)):
        matrix[row][col] = '*' #Marks the current position in the matrix as '*' to indicate that this cell corresponds to a character in the zigzag pattern.
        if row == 0:
            i=1 #move down
        elif row == key - 1:
            i=-1 #move up
        row += i #+1 in each step

    index = 0
    for r in range(key): #each row (r) of the matrix.Rows correspond to the key
        for c in range(len(encrypted_message)): #Columns correspond to the characters in the encrypted_message.
            if matrix[r][c] == '*': #Checks if the current cell in the matrix contains a '*'.
                matrix[r][c] = encrypted_message[index] #Replaces the '*' at the current position with the character at the current index of the encrypted_message
                index += 1

    row = 0 #Starts at the top row of the matrix.
    i = 0 #Tracks the direction of movement (+1 for down, -1 for up).
    decrypted_message = ''
    for col in range(len(encrypted_message)): #Each column corresponds to a character in the encrypted_message.
        decrypted_message += matrix[row][col] #Adds the character at the current matrix[row][col] position to the decrypted_message.
        if row == 0:
            i = 1 #move down
        elif row == key - 1:
            i=-1 #move up
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
