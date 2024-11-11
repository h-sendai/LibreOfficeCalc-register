import uno

def my_first_macro_calc(*args):
    doc = XSCRIPTCONTEXT.getDocument()
    cell = doc.Sheets[0]['A1']  # com.sun.star.sheet.XSpreadsheetDocument
    cell.setString('PythonからCalcでHello World')

    return
