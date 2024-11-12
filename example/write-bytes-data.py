import uno
import os
import string
# string.ascii_uppercase: 'ABCD ... XYZ'
# string.ascii_uppercase[0]: 'A'
# string.ascii_uppercase[1]: 'B'

debug = False

def write_to_file(*args):
    doc = XSCRIPTCONTEXT.getDocument()
    sheet = doc.getSheets().getByIndex(0)

    # bit data range
    # Cell number assignment
    # A1:(0, 0) B1:(1, 0) C1:(2, 0) D:1(3, 0) ...
    # A2:(0, 1) B2:(1, 1) C2:(2, 1) D:2(3, 1) ...
    # A3:(0, 2) B3:(1, 2) C3:(2, 2) D:3(3, 2) ...
    y_min =   3
    y_max = 160
    x_min =   4
    x_max = x_min + 16 - 1 # 16: 16 bits
    # 
    # (x_min, y_min) == (4, 3) == E4
    # (x_max, y_max) == (19, 160) == T161

    bits = list()
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            s = sheet.getCellByPosition(x, y).String
            try:
                v = int(s)
            except ValueError as e:
                continue
            bits.append(v)
            if debug:
                print('debug:', y + 1, string.ascii_uppercase[x], v)
    if debug:
        print('debug: bits length:', len(bits))
    if (len(bits) % 8 != 0):
        raise ValueError('bit length is not multiple of 8: length: %d' % (len(bits)))

    # filename = os.environ['HOME'] + '/data.txt'
    filename = sheet.getCellByPosition(22, 19).String # (22, 19) == W20
    f = open(filename, 'w')
    for i in range(0, len(bits)//8):
        value =   (bits[8*i + 0] << 7)  \
                + (bits[8*i + 1] << 6)  \
                + (bits[8*i + 2] << 5)  \
                + (bits[8*i + 3] << 4)  \
                + (bits[8*i + 4] << 3)  \
                + (bits[8*i + 5] << 2)  \
                + (bits[8*i + 6] << 1)  \
                + (bits[8*i + 7])
        s = '%02X' % (value)
        f.write(s + '\n')
    f.close()
    print('done')

    return
