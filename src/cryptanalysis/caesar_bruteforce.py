"""Educational Caesar-cipher brute-force demonstration."""

def decrypt(text, shift):
    out = []
    for ch in text:
        if 'A' <= ch <= 'Z': out.append(chr((ord(ch)-65-shift)%26+65))
        elif 'a' <= ch <= 'z': out.append(chr((ord(ch)-97-shift)%26+97))
        else: out.append(ch)
    return ''.join(out)

if __name__ == '__main__':
    ciphertext = 'Wkh txlfn eurzq ira'
    for shift in range(26):
        print(f'{shift:2}: {decrypt(ciphertext, shift)}')
