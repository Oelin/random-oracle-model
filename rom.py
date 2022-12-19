"""
Implements a random oracle model.

Random oracle models are abstract models representing the concept of
a collision-resistant hash function. They consist of a hash table and
a pseudorandom number generator. To compute the hash of a message m,
the oracle generates a pseudorandom k-bit string s. A new hash table
entry is then created such that m maps to s. Next time m is given as
input, the precomputed string will be returned.

This achieves two ideal properties of collision-resistant hash
functions:

(1) Determinism - identical messages map to identical hashes.
(2) Collision-resistance - there is negligible probability of finding
  a collision w.r.t. to k.

The first property follows from the definition of a correct hash
table. Now, as a result of the birthday problem, the probability of
finding collisions is in fact O(2^-{k/2}), which is non-negligible
w.r.t. to k. To retain the security of a brute-force search, we use
k' = 2*k as the security parameter.

Other desirable properties include preimage resistance and second-
preimage resistance.

(3) Preimage resistance - given some hash s, the probability of
    finding some m such that m maps to s, is negligible in k.

(4) Second preimage resistance - given some hash s and message m,
    the probability of finding another message m' != m, such that
    m' maps to s is negligible in k.

This along with their simplicity, makes random oracle models a
useful framework for deriving results about hash functions.
"""


from random import randint


class RandomOracleModel:

        def __init__(self, parameter: int = 32):

                self.parameter = parameter # in bytes
                self.cache = {}


        def __call__(self, message: bytes) -> bytes:

                if self.cache.get(message):
                        return self.cache.get(message)

                hash = bytes((randint(0, 255) for _ in range(self.parameter)))
                self.cache[message] = hash

                return hash
