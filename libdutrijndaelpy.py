def debug(state): # delete this after debugging
    ns = outp(state)
    r = ''
    for n in ns:
        r += hex(n)[2:].rjust(2, '0')
    print(r)
    input()

def nums2bytes(nums):
    hexstring = ''
    for num in nums:
        hexstring += hex(num)[2:].rjust(2, '0')
    return(bytes.fromhex(hexstring))

def bytes2nums(b):
    nums = []
    i = 0
    while i < len(b):
        nums.append(b[i])
        i += 1
    return(nums)

def inp(data):
    if type(data) != bytes:
        raise TypeError
    if len(data) != 16:
        raise ValueError
    data = bytes2nums(data)
    state = []
    i = 0
    while i < 4:
        word = [data[i], data[i+4], data[i+8], data[i+12]]
        state.append(word)
        i += 1
    return(state)

def outp(state):
    output = []
    i = 0
    while i < 4:
        for word in state:
            output.append(word[i])
        i += 1
    output = nums2bytes(output)
    return(output)

sbox = [99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103,
        43, 254, 215, 171, 118, 202, 130, 201, 125, 250, 89,
        71, 240, 173, 212, 162, 175, 156, 164, 114, 192,
        183, 253, 147, 38, 54, 63, 247, 204, 52, 165, 229,
        241, 113, 216, 49, 21, 4, 199, 35, 195, 24, 150, 5,
        154, 7, 18, 128, 226, 235, 39, 178, 117, 9, 131, 44,
        26, 27, 110, 90, 160, 82, 59, 214, 179, 41, 227, 47,
        132, 83, 209, 0, 237, 32, 252, 177, 91, 106, 203,
        190, 57, 74, 76, 88, 207, 208, 239, 170, 251, 67,
        77, 51, 133, 69, 249, 2, 127, 80, 60, 159, 168, 81,
        163, 64, 143, 146, 157, 56, 245, 188, 182, 218, 33,
        16, 255, 243, 210, 205, 12, 19, 236, 95, 151, 68,
        23, 196, 167, 126, 61, 100, 93, 25, 115, 96, 129,
        79, 220, 34, 42, 144, 136, 70, 238, 184, 20, 222,
        94, 11, 219, 224, 50, 58, 10, 73, 6, 36, 92, 194,
        211, 172, 98, 145, 149, 228, 121, 231, 200, 55, 109,
        141, 213, 78, 169, 108, 86, 244, 234, 101, 122, 174,
        8, 186, 120, 37, 46, 28, 166, 180, 198, 232, 221,
        116, 31, 75, 189, 139, 138, 112, 62, 181, 102, 72,
        3, 246, 14, 97, 53, 87, 185, 134, 193, 29, 158, 225,
        248, 152, 17, 105, 217, 142, 148, 155, 30, 135, 233,
        206, 85, 40, 223, 140, 161, 137, 13, 191, 230, 66,
        104, 65, 153, 45, 15, 176, 84, 187, 22]

invsbox = [82, 9, 106, 213, 48, 54, 165, 56, 191, 64, 163,
        158, 129, 243, 215, 251, 124, 227, 57, 130, 155, 47,
        255, 135, 52, 142, 67, 68, 196, 222, 233, 203, 84,
        123, 148, 50, 166, 194, 35, 61, 238, 76, 149, 11,
        66, 250, 195, 78, 8, 46, 161, 102, 40, 217, 36, 178,
        118, 91, 162, 73, 109, 139, 209, 37, 114, 248, 246,
        100, 134, 104, 152, 22, 212, 164, 92, 204, 93, 101,
        182, 146, 108, 112, 72, 80, 253, 237, 185, 218, 94,
        21, 70, 87, 167, 141, 157, 132, 144, 216, 171, 0,
        140, 188, 211, 10, 247, 228, 88, 5, 184, 179, 69, 6,
        208, 44, 30, 143, 202, 63, 15, 2, 193, 175, 189, 3,
        1, 19, 138, 107, 58, 145, 17, 65, 79, 103, 220, 234,
        151, 242, 207, 206, 240, 180, 230, 115, 150, 172,
        116, 34, 231, 173, 53, 133, 226, 249, 55, 232, 28,
        117, 223, 110, 71, 241, 26, 113, 29, 41, 197, 137,
        111, 183, 98, 14, 170, 24, 190, 27, 252, 86, 62, 75,
        198, 210, 121, 32, 154, 219, 192, 254, 120, 205, 90,
        244, 31, 221, 168, 51, 136, 7, 199, 49, 177, 18, 16,
        89, 39, 128, 236, 95, 96, 81, 127, 169, 25, 181, 74,
        13, 45, 229, 122, 159, 147, 201, 156, 239, 160, 224,
        59, 77, 174, 42, 245, 176, 200, 235, 187, 60, 131,
        83, 153, 97, 23, 43, 4, 126, 186, 119, 214, 38, 225,
        105, 20, 99, 85, 33, 12, 125]

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

def subnums(ns, inv=False):
    r = []
    if inv:
        sb = invsbox
    else:
        sb = sbox
    for n in ns:
        r.append(sb[n])
    return(r)

def substate(state):
    r = []
    for word in state:
        r.append(subnums(word))
    return(r)

def rotatenums(ns, reps):
    if reps == 0:
        return(ns)
    i = len(ns) - 1
    b = 0
    c = ns[i]
    while i >= 0:
        b = ns[i-1]
        ns[i-1] = c
        i -= 1
        c = b
    if reps:
        rotatenums(ns, reps-1)

def shiftrows(state):
    i = 1
    while i < 4:
        rotatenums(state[i], i)
        i += 1

def expandkey(key):
    rconcount = 0
    expanded = []
    i = 0
    while i < len(key):
        expanded.append(key[i:i+4])
        i += 4
    i = 8
    while i < 60:
        temp = []
        for num in expanded[i-1]:
            temp.append(num)
        if i % 8 == 0:
            rotatenums(temp, 1)
            temp = subnums(temp)
            temp[0] = temp[0] ^ (2 ** rconcount)
            rconcount += 1
        elif i % 8 == 4:
            temp = subnums(temp)
        j = 0
        while j < 4:
            temp[j] = expanded[i-8][j] ^ temp[j]
            j += 1
        expanded.append(temp)
        i += 1
    return(expanded)

def mixcols(state):
    newstate = [[], [], [], []]
    c = 0
    while c < 4:
        s = multiply(2, state[0][c])
        s = s ^ multiply(3, state[1][c])
        s = s ^ state[2][c]
        s = s ^ state[3][c]
        c += 1
        newstate[0].append(s)
    c = 0
    while c < 4:
        s = state[0][c]
        s = s ^ multiply(2, state[1][c])
        s = s ^ multiply(3, state[2][c])
        s = s ^ state[3][c]
        c += 1
        newstate[1].append(s)
    c = 0
    while c < 4:
        s = state[0][c]
        s = s ^ state[1][c]
        s = s ^ multiply(2, state[2][c])
        s = s ^ multiply(3, state[3][c])
        c += 1
        newstate[2].append(s)
    c = 0
    while c < 4:
        s = multiply(3, state[0][c])
        s = s ^ state[1][c]
        s = s ^ state[2][c]
        s = s ^ multiply(2, state[3][c])
        c += 1
        newstate[3].append(s)
    for word in state:
        i = 0
        while i < 4:
            word[i] = 0
            i += 1
    return(newstate)

def addroundkey(state, expkey, roundn):
    roundkey = expkey[4*roundn:4*roundn+4]
    i = 0
    while i < 16:
        x = i // 4
        y = i % 4
        state[y][x] = state[y][x] ^ roundkey[x][y]
        i += 1

def setup(key, data):
    state = inp(data)
    if type(key) != bytes:
        raise TypeError
    if len(key) != 32:
        raise ValueError
    key = bytes2nums(key)
    expkey = expandkey(key)
    i = 0
    while i < 32:
        key[i] = 0
        i += 1
    return(expkey, state)

def encrypt(key, data):
    expkey, state = setup(key, data)
    debug(state)
    addroundkey(state, expkey, 0)
    debug(state)
    roundn = 1
    while roundn < 14:
        state = substate(state)
        debug(state)
        shiftrows(state)
        debug(state)
        state = mixcols(state)
        debug(state)
        addroundkey(state, expkey, roundn)
        debug(state)
        roundn += 1
    state = substate(state)
    debug(state)
    shiftrows(state)
    debug(state)
    addroundkey(state, expkey, 14)
    debug(state)
    return(outp(state))
