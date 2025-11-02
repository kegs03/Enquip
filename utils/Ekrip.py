from random import randint

def char_to_binary(word):
    word_binary = []

    # Convert each character of the word to binary
    for char in word:
        ascii_value = ord(char)
        binary_value = bin(ascii_value)[2:].zfill(8)  # Ensure 8-bit representation
        word_binary.append(binary_value)

    return word_binary

def generateKey():
    key = randint(1,10000)
    return key

def encrypt(binaries, key):
    encrypted_value = ''

    # Convert the key to binary (ensure it's 8 bits)
    key_binary = bin(key)[2:].zfill(8)

    # Encrypt by XOR-ing each bit of each character
    for binary in binaries:
        xor_result = ''
        for i in range(len(binary)):
            xor_result += str(int(binary[i]) ^ int(key_binary[i]))  # XOR each bit

        encrypted_value += xor_result  # Add the encrypted binary chunk

    return encrypted_value


def binary_to_char(binary):
    # Convert the binary string to an integer
    ascii_value = int(binary, 2)
    # Convert the integer to the corresponding character
    return chr(ascii_value)


def encrypt_word(word, key):
    # Step 1: Convert the word to a list of binary strings
    binaries = char_to_binary(word)

    # Step 2: Encrypt each character (binary string) using the key
    encrypted_binary = encrypt(binaries, key)

    # Step 3: Convert the encrypted binary back to characters
    encrypted_word = ''
    for i in range(0, len(encrypted_binary), 8):  # Process each 8-bit chunk
        encrypted_word += binary_to_char(encrypted_binary[i:i + 8])  # Take 8 bits at a time

    print("Encrypted word:", encrypted_word + "\n" + "key:" + str(key))
    return encrypted_word

def decrypt_check(encrypted_word, key):
    inputKey = input("Enter the key to decrypt: ")

    try:
        if inputKey.isnumeric() and not type(inputKey) == bool:
            inputKey = int(inputKey)
            if key == inputKey:
                return encrypt_word(encrypted_word, key)
            else:
                return "Invalid key"
        else:
            raise TypeError

    except TypeError as e:
        print("Must be all digits", e)

    except Exception as e:
        print("invalid exception", e)

