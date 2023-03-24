from utils.generatePrime import generatePrime


class RSA_text:
    """
    Attributes
    ----------
    e : int
        a constant used to genrerate private key and encrypt messages 

    Methods
    -------
    keygen(keysize=1024)
        Generates public and private key

    encrypt(message, public_key)
        Encrypts message with public key

    decrypt(message, public_key, private_key)
        Decrypts message with private key
    """

    e = 65537

    def keygen(self, keysize=128):
        """
        generate public and private key

        keysize is in bytes
        """

        p, q, = generatePrime(keysize), generatePrime(keysize)

        n = p * q
        fi = (p - 1) * (q - 1)
        # e = 65537
        if p % self.e == 1 or q % self.e == 1:
            print("we have a problem")

        d = pow(self.e, -1, fi)
        return {"n": n, "e": self.e}, d

    def encrypt(self, m: str, pub_key: dict):
        """Encrypts message m with public key

        Step 1. Encode message with ascii

        Step 2. Encrypt each key individually by calculating c^e in mod n
        """

        encoded = m.encode('ascii')
        encrypted = (pow(c, pub_key["e"], pub_key["n"]) for c in encoded)
        return list(encrypted)

    def decrypt(self, m: str, pub_key: dict, d: int):
        """Decrypts message m with public and private key"""

        decrypted = "".join(chr(pow(c, d, pub_key["n"])) for c in m)
        return decrypted


if __name__ == "__main__":
    rsa = RSA_text()

    public_key, private_key = rsa.keygen(16)
    print("pup_key:", public_key)
    print("private_key:", private_key)

    message = "HI, this is an encrypted message"
    print("message:", message)

    message_encrypted = rsa.encrypt(message, public_key)
    print("encrypted:", message_encrypted)

    message_decrypted = rsa.decrypt(message_encrypted, public_key, private_key)
    print("decrypted:", message_decrypted)
