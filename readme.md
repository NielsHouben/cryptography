OBS - this is for educational purpouses only!

# RSA and AES encryption

## RSA
The `rsa.py` file is an implementation of the algorithm explained on [brilliant.org](https://brilliant.org/wiki/rsa-encryption/).

Firstly, we generate two prime numbers. The product of these two is our public key which is used to transform message into encrypted messages. The private key is based on our two secret prime numbers, and with this private key, it is possible to undo transformations. But this only works as long as no one is able to found out which two primes make up the public key. Fortunately, there is no efficient algorithm for factoring yet.

However, in the future, it is predicted that quantum computers might be able to do exactly this at great speed. Even increasing the size of prime numbers will not suffice. This is why new methods such as lattice-based encryption are being experimented with.

Even though no method of uncovering secure RSA-encrypted messages exists today, one can still store these messages in the hope of decrypting them later.

### Prime Gen
The `generatePrime.py` file is an implementation from the math on [crypto.stanford.edu](https://crypto.stanford.edu/pbc/notes/numbertheory/millerrabin.html#:~:text=The%20Miller%2DRabin%20test%20picks,Rabin%20test%20is%20at%20most%20.).

This method of generating prime numbers is probabilistic and not determenistic. This does mean that a probability for generating non-primes exists, however, this is extremely unlikely. The benefits of this methods is the speed at which large prime numbers can be found. By using Rabin Miller tests we avoid having to check all posible divisors.

## AES
The `aes.py` file is An adaptation of the algorithm described by [simplilearn.com](https://www.simplilearn.com/tutorials/cryptography-tutorial/aes-encryption#:~:text=Key%20Expansion%3A%20It%20takes%20a,bytes%20during%20the%20encryption%20procedure.).

In addition to Simplilearn, I used [braincoke.fr](https://braincoke.fr/blog/2020/08/the-aes-key-schedule-explained/#rotword) and [brainkart.com](https://www.brainkart.com/article/AES-Key-Expansion_8410/) for learning about the key schedule.

`mixColumns` was done with lookup tables from [wikipedia.org](https://en.wikipedia.org/wiki/Rijndael_MixColumns)

