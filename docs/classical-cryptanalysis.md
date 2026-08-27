# Classical Cryptanalysis

This work studies why simple classical ciphers are vulnerable to analysis and exhaustive search.

## Caesar cipher
A Caesar cipher has a tiny key space, so all shifts can be tested quickly. The lab demonstrates recovering the plaintext `The quick brown fox` from a Caesar-shifted ciphertext by trying every possible shift.

## Vigenère cipher
Vigenère uses a repeating keyword and multiple shifts instead of one fixed shift. It hides simple frequency patterns better than Caesar, although classical Vigenère remains breakable under suitable conditions.

## XOR
XOR is self-inverse: `(P XOR K) XOR K = P`. A simple XOR construction is useful for understanding symmetric operations but should not be confused with a secure modern encryption scheme.

## Frequency analysis
The cryptanalysis lab also explores statistical analysis of ciphertext and brute-force techniques, showing why modern cryptographic systems need large key spaces and strong algorithmic design.
