import uno

def set_cell(*args):
    doc = XSCRIPTCONTEXT.getDocument()
    sheet = doc.getSheets().getByIndex(0)

    cell = sheet.getCellByPosition(0, 0)
    cell.String = 'ABC'

    cell = sheet.getCellByPosition(1, 0)
    cell.Value = 123

    print('done')

    return
