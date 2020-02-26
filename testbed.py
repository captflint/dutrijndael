import aes

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

testkey = """
60 3d eb 10 15 ca 71 be 2b 73 ae f0 85 7d 77 81
1f 35 2c 07 3b 61 08 d7 2d 98 10 a3 09 14 df f4
"""

a = hexstring2nums(testkey)
for word in aes.expandkey(a):
    print(nums2hexstring(word))
