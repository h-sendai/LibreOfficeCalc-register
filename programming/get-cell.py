import uno

def get_cell(*args):
    doc = XSCRIPTCONTEXT.getDocument()
    sheet = doc.getSheets().getByIndex(0)
    cell = sheet.getCellByPosition(0, 0)
    print(cell.String)

    cell = sheet.getCellByPosition(1, 0)
    print(type(cell.Value), cell.Value)
    print('convert to int:', int(cell.Value))
    # or get as string then conver to int
    print('get as string and conver to int', type(cell.String), int(cell.String))
    print('done')

    return
