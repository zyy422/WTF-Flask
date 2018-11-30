import xlrd


def read_excel(f):

    f = f.read()
    book = xlrd.open_workbook(file_contents=f)
    sheet_1_obj = book.sheet_by_index(0)

    machine = [sheet_1_obj.cell(23, 1).value, sheet_1_obj.cell(24, 1).value]

    column_1 = sheet_1_obj.col_values(1)    # 存取漏率
    leakrate_data = column_1[2:23]

    exhaust_nor_data = []   # 存取室温下的真空度
    for i in range(3, 16):
        data = xlrd.xldate_as_tuple(sheet_1_obj.cell(i, 3).value, 0)
        data = data[3] * 60 + data[4] * 60 + data[5]
        exhaust_nor_data.append(data)

    exhaust_150_data = []   # 存取加热到150摄氏度下的真空度
    for i in range(3, 16):
        data = xlrd.xldate_as_tuple(sheet_1_obj.cell(i, 5).value, 0)
        data = data[3] * 3600 + data[4] * 60 + data[5]
        exhaust_150_data.append(data)

    excel_data = [machine, leakrate_data, exhaust_nor_data, exhaust_150_data]
    return excel_data
