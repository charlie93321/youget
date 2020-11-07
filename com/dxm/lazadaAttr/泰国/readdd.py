import xlwt


import xlrd


xls = xlrd.open_workbook(r"C:\Users\DXM_0093\AppData\Local\JetBrains\IntelliJIdea2020.1\tomcat\Unnamed_bigseller_2\work\Catalina\localhost\1111.xlsx")

sheet = xls.sheet_by_name("attr")

for row in sheet.get_rows():
    print(row)
xls.release_resources()
