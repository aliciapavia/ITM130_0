def shift_letter(letter, shift):
    if (ord(letter) + shift) > 90:
        print(chr(ord(letter) + shift - 26))
    elif (ord(letter) + shift) < 65:
        print(" ")
    else:
        print(chr(ord(letter) + shift))

shift_letter("A", 0) 
shift_letter("A", 2) 
shift_letter("Z", 1) 
shift_letter("X", 5)
shift_letter(" ", 20) 

def caesar_cipher(message, shift):
    shifted_message = ""
    for n in message:
        if (ord(n) + shift) > 122:
            shifted_message = shifted_message + (chr(ord(n) + shift - 26))
        elif (ord(n) + shift) < 97:
            shifted_message = shifted_message + " "
        else:
            shifted_message = shifted_message + (chr(ord(n) + shift))
    print(shifted_message)

caesar_cipher("hello world", 1)

def shift_by_letter(letter, letter_shift):
    shift_num = ord(letter_shift) - 65
    if (ord(letter) + shift_num) > 90:
        print(chr(ord(letter) + shift_num - 26))
    elif (ord(letter) + shift_num) < 65:
        print(" ")
    else:
        print(chr(ord(letter) + shift_num))

shift_by_letter("A", "A")
shift_by_letter("A", "C")
shift_by_letter("B", "K")
shift_by_letter(" ", "P")

def vigenere_cipher(message, key):
    new_msg = ""
    counter = 0
    for n in message:
        if (ord(n) + ord(key[counter]) - 65) > 90:
            new_msg = new_msg + (chr((ord(n) + ord(key[counter]) - 91)))
        elif (ord(n) + ord(key[counter]) - 65) < 65:
            new_msg = new_msg + (" ")
        else:
            new_msg = new_msg + (chr((ord(n) + ord(key[counter])) - 65))
        counter = counter + 1
    print(new_msg)
        
vigenere_cipher("A C", "KEY")

def scytale_cipher(message, shift):
    n = len(message)
    columns = n // shift
    ciphertext = ['-'] * n

    def check_length(message, shift):
        if len(message) % shift == 0:
            return message
        else:
            while len(message) % shift > 0:
                message = message + "_"

    check_length(message, shift)
    
    for i in range(n):
        row = i // columns
        col = i % columns
        ciphertext[col * shift + row] = message[i]

    new_msg = "".join(ciphertext)
    print(new_msg)
    
scytale_cipher("INFORMATION_AGE", 3)
scytale_cipher("INFORMATION_AGE", 4)
scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8)

def scytale_decipher(message, shift):
    
    scytale_cipher(message, len(message) // shift)

scytale_decipher("IMNNA_FTAOIGROE", 3)
scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8)
scytale_decipher("IRIANMOGFANEOT__", 4)