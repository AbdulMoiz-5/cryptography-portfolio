"""Small correctness checks for the educational cryptography examples."""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "src"

def load(name, relative):
    spec = spec_from_file_location(name, ROOT / relative)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

nt = load("number_theory", "number-theory/basic_number_theory.py")
crt_mod = load("crt_rsa", "crt-rsa/crt_rsa.py")
caesar = load("caesar", "cryptanalysis/caesar_bruteforce.py")
ts = load("tonelli", "cryptanalysis/tonelli_shanks.py")

assert nt.custom_gcd(66528, 52920) == 1512
g, x, y = nt.extended_gcd(102, 38)
assert g == 2 and 102 * x + 38 * y == g
assert nt.modular_inverse(3, 13) == 9
assert nt.discrete_log_brute(3, 13, 17) == 4
assert crt_mod.crt([2, 3, 2], [3, 5, 7]) == 23

p, q, e = 61, 53, 17
d = pow(e, -1, (p - 1) * (q - 1))
for msg in (65, 72, 88):
    c = pow(msg, e, p * q)
    assert crt_mod.crt_rsa_decrypt(c, p, q, d) == msg

assert crt_mod.garners_crt([2, 3, 2], [3, 5, 7]) == 23
assert caesar.decrypt("Wkh txlfn eurzq ira", 3) == "The quick brown fox"
r = ts.tonelli_shanks(10, 13)
assert r is not None and r * r % 13 == 10
assert ts.tonelli_shanks(0, 13) == 0

print("All cryptography portfolio tests passed.")
