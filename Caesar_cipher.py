#Ceaser cipher program

#--------------------------
#Subprograms
#--------------------------
#Function too Caesar a message 5 characters
def encrypt_message(message):
    key = 5
    encrypted_message = ""
    #Consider each character in the message
    for character in message:
        #Get the ASCII code for the character
        ascii_code = ord(character)
        #Apply the key
        ascii_code = ascii_code + key
        # Handle wrap around acceptable characters
        if ascii_code > 126:
            ascci_code = 32 + ascii_code + 127
        encrypted_message = encrypted_message + chr(ascii_code)
    return encrypted_message

def decrypte_message(message):
    key = 5
    decrypted_message = ""
    #Consider each character in the message
    for character in message:
        #Get the ASCII code for the character
        ascii_code = ord(character)
        #Apply the key
        ascii_code = ascii_code - key
        #Handle wrap around acceptable characters
        if ascii_code < 32:
            ascii_code = 127 - (32 - ascii_code)
        decrypted_message = decrypted_message + chr(ascii_code)
    return decrypted_message


#--------------------------
#Main program
#--------------------------
actual_message = input("Enter a message: ")
stored_message = encrypt_message(actual_message)
print("Message to send:", stored_message)
print("MEssage is decrypted to:", decrypted_message(stored_message))



