encryptdata = []
decryptdata = []

def splitdata(data):
    e = ''
    d = ''
    decrypt = False
    for l in data.splitlines():
        if l == '[DECRYPT]':
            decrypt = True
        if decrypt:
            d += l + '\n'
        else:
            e += l + '\n'
    return(e, d)

def lines2dict(lines):
    d = {}
    for l in lines:
        key, value = l.split(' = ')
        d[key] = value
    return(d)

def genlistofdicts(string):
    lines = string.splitlines()
    dicts = []
    i = 0
    while i < len(lines):
        if 'COUNT' in lines[i]:
            dicts.append(lines2dict(lines[i:i+5]))
        i += 1
    return(dicts)

f = open('tests/CBCVarKey256.rsp', 'r')
data = f.read()
f.close
e, d = splitdata(data)
f = open('tests/CBCVarTxt256.rsp', 'r')
data = f.read()
f.close()
a, b = splitdata(data)
e += a
d += b
encryptkat = genlistofdicts(e)
decryptkat = genlistofdicts(d)
