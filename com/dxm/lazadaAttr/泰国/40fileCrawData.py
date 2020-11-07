import os
import traceback
import xlrd
from xlrd import XLRDError



dicMap = {}
dicCount = []
dir1 = r'C:\Users\DXM_0093\Desktop\lazada分类_zxy'
file_names = os.listdir(dir1)


def listToStr(arr):
    s = ''
    for item in arr:
        s += "\"" + str(item) + "\","
    return s

def read_sheet2(sheet2):
    categoryIds=[]
    for row in sheet2.get_rows():
        value = row[0].value
        if value is not None:
            if len(value.strip())>0:
                newValue = value.strip().split(" - ")[0]
                if newValue!='PrimaryCategory' :categoryIds.append(newValue)
    return categoryIds


def read_excel():
    with open(r'F:\othertool\you_get\com\dxm\lazadaAttr\泰国\record.txt',mode='w',encoding='utf-8') as f:
        for file_name in file_names:
            path = "{}/{}".format(dir1, file_name)
            if file_name.endswith(".csv") or file_name=='Color Family (1).xls' :
                print("{} is not valid xls".format(path))
                continue

            sheet = None
            x1 = None
            try:
                x1 = xlrd.open_workbook(path)

                sheet2 = x1.sheet_by_name("Valid Values")
                cids = read_sheet2(sheet2)

                sheet = x1.sheet_by_name('Upload Template')
            except XLRDError as e:
                print("{} can't get sheet {}".format(path, 'Upload Template'))
                print('str(e):\t\t', str(e))
                print('repr(e):\t', repr(e))
                print('traceback.print_exc():')
                # 以下两步都是输出错误的具体位置的
                traceback.print_exc()
                #print('traceback.format_exc():\n%s' % traceback.format_exc())
                continue
            finally:
                x1.release_resources()
            #print("{}  get sheet ===> sheets=>{}".format(path, x1.sheet_names()))

            row1 = sheet.row(1)
            row2 = sheet.row(2)
            for i in range(1, len(row1)):
                key = row2[i].value.strip()
                value = row1[i].value.replace('*', '').strip()
                dicMap[(key,listToStr(cids))] = value
                print(key,value,cids)
                f.write('{}|{}|{}|{}\n'.format(listToStr(cids),key,value,file_name))
            dicCount.append(i)

            x1.release_resources()

read_excel()
#write_date_to_xls(file_name='lazada_vi_attr.xls', dataMap=dicMap, title=['EN', 'VI'])
print(len(dicMap))


