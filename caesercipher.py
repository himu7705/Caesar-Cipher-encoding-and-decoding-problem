def encrypt_caesar(msg, shift):
    res = ''
    for ch in msg:
        if ch.isalpha():
            if ch.isupper():
                base = ord('A')
            else:
                base = ord('a')
            code = ord(ch) - base
            code = (code + shift) % 26
            res += chr(base + code)
        else:
            res += ch
    return res
def decrypt_caesar(msg, shift):
    return encrypt_caesar(msg, -shift)
