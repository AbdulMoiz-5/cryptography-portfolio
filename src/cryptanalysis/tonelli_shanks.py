"""Educational Tonelli-Shanks implementation for odd prime moduli."""

def tonelli_shanks(a, p):
    """Return a square root of a modulo odd prime p, or None if none exists."""
    if p == 2:
        return a % p
    a %= p
    if a == 0:
        return 0
    if p <= 2 or p % 2 == 0:
        raise ValueError("p must be an odd prime")
    if pow(a, (p - 1) // 2, p) != 1:
        return None

    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(a, (p + 1) // 4, p)

    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1

    m = s
    c = pow(z, q, p)
    t = pow(a, q, p)
    r = pow(a, (q + 1) // 2, p)

    while t != 1:
        i = 1
        temp = (t * t) % p
        while temp != 1:
            temp = (temp * temp) % p
            i += 1
            if i >= m:
                raise ArithmeticError("Tonelli-Shanks failed; check that p is prime")
        b = pow(c, 2 ** (m - i - 1), p)
        m = i
        c = (b * b) % p
        t = (t * c) % p
        r = (r * b) % p
    return r
