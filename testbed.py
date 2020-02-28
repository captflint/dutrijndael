import libdutrijndaelpy as aes

def hexstring2nums(hs):
    valid = ''
    if type(hs) != str:
        raise TypeError
    hs = hs.casefold()
    for c in hs:
        if c in '0123456789abcdef':
            valid += c
    if len(valid) % 2 != 0:
        raise ValueError
    i = 0
    r = []
    while i < len(valid):
        r.append(int(valid[i:i + 2], base = 16))
        i += 2
    return(r)

def nums2hexstring(ns):
    r = ''
    for n in ns:
        r += hex(n)[2:].rjust(2, '0')
    return(r)

print("8ea2b7ca516745bfeafc49904b496089")

testdata = """
00112233445566778899aabbccddeeff
"""

testkey = """
000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f
"""

testkey = hexstring2nums(testkey)
testkey = aes.nums2bytes(testkey)

testdata = hexstring2nums(testdata)
testdata = aes.nums2bytes(testdata)
testdata = aes.encrypt(testkey, testdata)
testdata = aes.bytes2nums(testdata)
testdata = nums2hexstring(testdata)
print(testdata)
