import uno
import os
import string
# string.ascii_uppercase: 'ABCD ... XYZ'
# string.ascii_uppercase[0]: 'A'
# string.ascii_uppercase[1]: 'B'

debug = False

# https://stackoverflow.com/a/12640614
def col2num(col):
    # convert 'A' -> 1
    #         'B' -> 2
    #          :
    #         'Z' -> 26
    #         'AA' -> 27
    #         'AB' -> 28
    #          :
    #         'ZZ' -> 702 (26*26 + 26)
    num = 0
    for c in col:
        if c in string.ascii_letters:
            num = num * 26 + (ord(c.upper()) - ord('A')) + 1
    return num

def convert_for_calc_cell(cell):
    # convert "A1", "B1" to (0 + 1, 0 + 1), (1 + 1, 0 + 1) etc.
    c = cell.upper()
    for i in string.ascii_uppercase:
        c = c.replace(i, '')
    y = int(c)

    al = cell.replace(str(y), '')
    x = col2num(al)

    # -1: for python script cell index
    return (x - 1, y - 1)

# def write_to_file(*args):
def main(*args):
    doc = XSCRIPTCONTEXT.getDocument()
    sheet = doc.getSheets().getByIndex(0)

    # bit data range
    # Cell number assignment
    # A1:(0, 0) B1:(1, 0) C1:(2, 0) D:1(3, 0) ...
    # A2:(0, 1) B2:(1, 1) C2:(2, 1) D:2(3, 1) ...
    # A3:(0, 2) B3:(1, 2) C3:(2, 2) D:3(3, 2) ...
    # hard coding example
    #y_min =   3
    #y_max = 160
    #x_min =   4
    #x_max = x_min + 16 - 1 # 16: 16 bits
    # 
    # (x_min, y_min) == (4, 3) == E4
    # (x_max, y_max) == (19, 160) == T161

    # get bit pattern cell index
    # Read A1 cell and extract upper left cell index and lower right cell index
    # Format: B2:E5 (Upper left cell index : (colon) Lower right cell index
    cell = sheet.getCellByPosition(0, 0).String
    if cell == '':
        raise ValueError('No bits region scecified.  Please specify like B2:E5 (Upper Left, : and Lower Right)')
    upper_left_s, lower_right_s = cell.split(':')
    upper_left_s  = upper_left_s.strip()
    lower_right_s = lower_right_s.strip()

    upper_left_n  = convert_for_calc_cell(upper_left_s)
    lower_right_n = convert_for_calc_cell(lower_right_s)
    x_min = upper_left_n[0]
    x_max = lower_right_n[0]
    y_min = upper_left_n[1]
    y_max = lower_right_n[1]

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
    filename = sheet.getCellByPosition(1, 0).String # (1, 0) == B1
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
    # print('done')

    return
