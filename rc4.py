import binascii


def xor_en(input_str, key):
    output = ''.join(chr(ord(char) ^ ord(key)) for char in input_str)
    print(output)


def ksa(key):
    S = list(range(256))
    j = 0
    key_length = len(key)

    for i in range(256):
        j = (j + S[i] + ord(key[i % key_length])) % 256
        S[i], S[j] = S[j], S[i]

    return S


def prga(S, input_str):
    i = 0
    j = 0
    output = []

    for char in input_str:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        keystream = S[(S[i] + S[j]) % 256]
        output.append(chr(ord(char) ^ keystream))

    return ''.join(output)


def rc4(input_str, key):
    S = ksa(key)
    return prga(S, input_str)


def to_hex(input_str):
    return binascii.hexlify(input_str.encode()).decode()


def from_hex(hex_str):
    return binascii.unhexlify(hex_str).decode()


if __name__ == "__main__":
    xor_en("Hello World", 'k')

    plaintext = "Hello RC4"
    key = "secret"
    encrypted = rc4(plaintext, key)
    print("Encrypted:", to_hex(encrypted))

    decrypted = rc4(encrypted, key)
    print("Decrypted:", decrypted)

    hex_str = to_hex("Hello Hex")
    print("Hex:", hex_str)

    original_str = from_hex(hex_str)
    print("Original:", original_str)
