class Cesar:
    """Cesar encryption"""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shift = 2

    def encrypt(self, m):
        encrypted = ""
        for c in m:
            u = c.isupper()
            c = c.lower()
            if c == " ":
                encrypted += " "
                continue
            idx = self.alphabet.index(c)
            newIdx = idx + self.shift
            if newIdx > 25:
                newIdx = (newIdx % 25) - 1
            new_c = self.alphabet[newIdx]
            new_c = new_c.upper() if u else new_c
            encrypted += new_c
        return encrypted

    def decrypt(self, m):
        decrypted = ""
        for c in m:
            u = c.isupper()
            c = c.lower()
            if c == " ":
                decrypted += " "
                continue
            idx = (self.alphabet.index(c))
            if (idx + self.shift) < 0:
                idx = (idx % 26)
            newIdx = idx - self.shift

            new_c = self.alphabet[newIdx]
            new_c = new_c.upper() if u else new_c
            decrypted += new_c
        return decrypted


if __name__ == "__main__":
    cesar = Cesar()

    cesar.shift = 3
    message = "xyz abc XYZ ABC"
    print("message:", message)
    message_encrypted = cesar.encrypt(message)
    print("encrypted:", message_encrypted)
    message_decrypted = cesar.decrypt(message_encrypted)
    print("decrypted:", message_decrypted)
