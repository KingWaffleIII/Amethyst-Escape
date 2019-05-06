alphabet = "abcdefghijklmnopqrstuvwxyz"
message = input("Please enter your encrypted message: ").lower()
encryptedMessage = ""
key = input("Please enter your decryption key: ")
while 1:
    try:
        key = int(key)
        break
    except ValueError:
        print("ERROR! Letters or Special Characters detected! Please enter numbers only")
        key = input("Please enter your decryption key: ")
        pass

key = int(key)

for char in message:
    if char in alphabet:
        position = alphabet.find(char)
        newPosition = (position - key) % 26
        encryptedMessage = encryptedMessage + alphabet[newPosition]
    else:
        encryptedMessage = encryptedMessage - char

print("Your decrypted message is:" , encryptedMessage)
        


