class CaeserCipher:
    """Class for doing encryption and decryption using Caeser Algorithm for any key"""

    def __init__(self, shift):
        """Construct Caeser Cipher using given key for shifting"""
        encoder = [None] * 26       # array for encryption
        decoder = [None] * 26       # array for decryption

        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))  # for capital letters
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)                    # storing as string to keep fixed
        self._backward = ''.join(decoder)

    def encrypt(self, message):
        """Returns encrypted message"""
        return self._transform(message, self._forward)

    def decrypt(self, message):
        """Returns decrypted message"""
        return self._transform(message, self._backward)

    def _transform(self, original, code):
        """Given a message and a code (either encrypting or decrypting) returns the other message"""
        msg = list(original)
        for i in range(len(msg)):
            if msg[i].isupper():                        # changing capital letters
                msg[i] = code[ord(msg[i]) - ord('A')]
            elif msg[i].islower():
                msg[i] = code[ord(msg[i]) - ord('a')].lower()
        return ''.join(msg)


######## Testing #######
if __name__ == "__main__":
    cipher = CaeserCipher(13)
    file = open("email.txt",'r')
    lines = file.readlines()
    for line in lines:
        decoded = cipher.decrypt(line)
        print(decoded, end = '')
    file.close()

