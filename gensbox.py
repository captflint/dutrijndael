def xtime(x):
    x = x << 1
    if x > 255:
        x = x ^ 0x11b
    return(x)

def multiply(b, c):
    if c < b:
        b, c = c, b
    if b == 0:
        return(0)
    if b == 1:
        return(c)
    if b >= 128:
        r = 7
    elif b >= 64:
        r = 6
    elif b >= 32:
        r = 5
    elif b >= 16:
        r = 4
    elif b >= 8:
        r = 3
    elif b >= 4:
        r = 2
    elif b >= 2:
        r = 1
    d = c
    b -= 2 ** r
    while r > 0:
        d = xtime(d)
        r -= 1
    return(d ^ multiply(b, c))

tt = []
rw = []
a = 0
b = 0

while a <= 255:
    rw.append(multiply(a, b))
    b += 1
    if b == 256:
        b = 0
        tt.append(rw)
        rw = []
        a += 1

def findgfinv(b):
    if b == 0:
        return(0)
    return(tt[b].index(1))

def getbit(b, i):
    i = i % 8
    i = 2 ** i
    b = b & i
    if b == 0:
        return(0)
    else:
        return(1)

def affinetran(b):
    i = 0
    r = 0
    while i < 8:
        bit = getbit(b, i)
        bit = bit ^ getbit(b, i + 4)
        bit = bit ^ getbit(b, i + 5)
        bit = bit ^ getbit(b, i + 6)
        bit = bit ^ getbit(b, i + 7)
        bit = bit << i
        r = r | bit
        i += 1
    r = r ^ 0x63
    return(r)

def invtran(b):
    i = 0
    r = 0
    while i < 8:
        bit = getbit(b, i)
        bit = bit ^ getbit(b, i)
        bit = bit ^ getbit(b, i + 1)
        bit = bit ^ getbit(b, i + 2)
        bit = bit ^ getbit(b, i + 3)
        bit = bit << i
        r = r | bit
        i += 1
    r = r ^ 0x63
    return(r)
