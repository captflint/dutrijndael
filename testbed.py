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

testmcstate = """
6353e08c0960e104cd70b751bacad0e7
"""

teststate = []

i = 0
word = []
for num in hexstring2nums(testmcstate):
    word.append(num)
    i += 1
    if i == 4:
        i = 0
        teststate.append(word)
        word = []

output = ''
for word in aes.mixcols(teststate):
    output += nums2hexstring(word)
print(output)
print("5f72641557f5bc92f7be3b291db9f91a")
