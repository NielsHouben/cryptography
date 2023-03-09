from utils.primeGen import generateLargePrime


class RSA:
    """RSA encryption"""

    def keygen(self, keysize=1024):
        """
        generate public and private key

        keysize is in bytes
        """

        p, q, = generateLargePrime(keysize), generateLargePrime(keysize)

        n = p * q
        fi = (p - 1) * (q - 1)
        e = 65537
        # e = 3
        if p % e == 1 or q % e == 1:
            print("we have a problem")
        d = pow(e, -1, fi)
        return {"n": n, "e": e}, d

    def encrypt(self, m, pub_key):
        """Encrypts message m with public key"""

        encoded = m.encode('ascii')
        encrypted = (pow(c, pub_key["e"], pub_key["n"]) for c in encoded)
        return encrypted

    def decrypt(self, m, pub_key, d):
        """Decrypts message m with public and private key"""

        decrypted = "".join(chr(pow(c, d, pub_key["n"])) for c in m)
        return decrypted


if __name__ == "__main__":
    rsa = RSA()

    public_key, private_key = rsa.keygen(16)
    print("pup_key:", public_key)
    print("private_key:", private_key)

    message = "HI, this is an encrypted message"
    print("message:", message)

    message_encrypted = rsa.encrypt(message, public_key)
    print("encrypted:", message_encrypted)

    message_decrypted = rsa.decrypt(message_encrypted, public_key, private_key)
    print("decrypted:", message_decrypted)
