"""Chinese Remainder Theorem and RSA-CRT exercises."""

def crt(remainders, moduli):
    """Solve CRT for pairwise-coprime positive moduli."""
    if len(remainders) != len(moduli) or not moduli:
        raise ValueError("remainders and moduli must have the same non-zero length")
    N = 1
    for m in moduli: N *= m
    x = 0
    for r, m in zip(remainders, moduli):
        Ni = N // m
        inv = pow(Ni, -1, m)
        x += r * Ni * inv
    return x % N

def crt_rsa_decrypt(C, p, q, d):
    """Educational RSA-CRT decryption for distinct coprime primes p and q."""
    dp, dq = d % (p - 1), d % (q - 1)
    q_inv = pow(q, -1, p)
    mp, mq = pow(C, dp, p), pow(C, dq, q)
    h = (q_inv * (mp - mq)) % p
    return mq + h * q

def garners_crt(remainders, moduli):
    """Garner CRT reconstruction for pairwise-coprime moduli."""
    x = list(remainders)
    for i in range(len(moduli)):
        for j in range(i):
            x[i] = ((x[i] - x[j]) * pow(moduli[j], -1, moduli[i])) % moduli[i]
    result, base = 0, 1
    for xi, mi in zip(x, moduli):
        result += xi * base
        base *= mi
    return result

if __name__ == "__main__":
    print("CRT:", crt([2, 3, 2], [3, 5, 7]))
    p, q, e = 61, 53, 17
    n, phi = p*q, (p-1)*(q-1)
    d = pow(e, -1, phi)
    for msg in [65, 72, 88]:
        c = pow(msg, e, n)
        print(msg, c, pow(c, d, n), crt_rsa_decrypt(c, p, q, d))
    print("Garner CRT:", garners_crt([3,4,2,6], [5,7,9,11]))
