def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    if a.startswith(''):
        a = a[2:]
    if b.startswith(''):
        b = b[2:]
    a, b = fill_zeros(a, b)
    carry = 0
    sonuc = ''
    for i in range(len(a)-1, -1, -1):
        bit_sum = (int(a[i])) + (int(b[i])) + carry
        sonuc = str(bit_sum % 2) + sonuc
        carry = bit_sum // 2
    if carry:
        sonuc = '1' + sonuc
    i = 0
    while i < len(sonuc) and sonuc[i] == '0':
        i += 1
    sonuc = sonuc[i:]
    if not sonuc:
        sonuc = '0'
    return '0b' + sonuc
def fill_zeros(a, b):
    maxlen = max(len(a), len(b))
    a = ('0' * (maxlen - len(a))) + a
    b = ('0' * (maxlen - len(b))) + b
    return a, b    
