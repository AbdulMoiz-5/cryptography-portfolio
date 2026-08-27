"""Basic number-theory exercises from the cryptography lab portfolio."""

def custom_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    return gcd, y1 - (b // a) * x1, x1

def modular_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def discrete_log_brute(base, target, mod):
    for x in range(mod):
        if pow(base, x, mod) == target:
            return x
    return None

if __name__ == "__main__":
    print("gcd(270, 192):", custom_gcd(270, 192))
    print("xgcd(102, 38):", extended_gcd(102, 38))
    print("Solutions to 4x = 12 (mod 14):", [x for x in range(14) if (4*x) % 14 == 12])
    print("17^-1 mod 43:", modular_inverse(17, 43))
    print("log_3(13) mod 17:", discrete_log_brute(3, 13, 17))
