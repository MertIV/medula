import openpyxl as excel

def readContacts(fileName):
    lst = []
    file = excel.load_workbook(fileName)
    sheet = file.active
    firstCol = sheet['A']
    for cell in range(len(firstCol)):
        if firstCol[cell].value is not None:
            contact = str(firstCol[cell].value)
            # contact = "\"" + contact + "\""
            lst.append(contact)
    return lst

def format_number(phone_number_list):
    formatted_list = []
    for phone_number in phone_number_list:
        phone_number = phone_number.replace(" ", "").replace("+", "").strip()
        formatted_list.append(phone_number)
    return formatted_list