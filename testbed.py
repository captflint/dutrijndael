import libdutrijndaelpy as aes
from tests.parsekatdata import encryptkat, decryptkat

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

def encrypttest(d):
    testkey = d['KEY']
    testdata = d['PLAINTEXT']
    
    testkey = hexstring2nums(testkey)
    testkey = aes.nums2bytes(testkey)

    testdata = hexstring2nums(testdata)
    testdata = aes.nums2bytes(testdata)
    testdata = aes.encrypt(testkey, testdata)
    testdata = aes.bytes2nums(testdata)
    testdata = nums2hexstring(testdata)
    print('expected:', d['CIPHERTEXT'])
    print('got:     ', testdata)
    if d['CIPHERTEXT'] == testdata:
        print('PASSED')
    else:
        print('FAILED')
    print()

for d in encryptkat:
    encrypttest(d)
