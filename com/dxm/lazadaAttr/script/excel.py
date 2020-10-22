import os
import traceback
from _csv import reader

import xlrd
from xlrd import XLRDError

from com.dxm.lazadaAttr.script.excel_util import write_date_to_xls

dicMap = {}
dicCount = []
dir1 = r'C:\Users\DXM_0093\Desktop\lazada分类_zxy'
dir1 = r'C:\Users\DXM_0093\Desktop\lazada分类_ljl'
dir1 = r'C:\Users\DXM_0093\Desktop\Lazada分类树（印尼语）'
file_names = os.listdir(dir1)
# file_names=sorted(file_names,key=lambda x:int(x.split(".")[0]))
for file_name in file_names:
    path = "{}/{}".format(dir1, file_name)
    if file_name.endswith(".csv"):
        print("{} is not xls".format(path))
        continue

    sheet = None
    x1 = None
    try:
        x1 = xlrd.open_workbook(path)
        sheet = x1.sheet_by_name('Upload Template')
    except XLRDError as e:
        print("{} can't get sheet {}".format(path, 'Upload Template'))
        print('str(e):\t\t', str(e))
        print('repr(e):\t', repr(e))
        print('traceback.print_exc():')
        # 以下两步都是输出错误的具体位置的
        traceback.print_exc()
        print('traceback.format_exc():\n%s' % traceback.format_exc())
        continue
    finally:
        x1.release_resources()
    print("{}  get sheet ===> sheets=>{}".format(path, x1.sheet_names()))

    row1 = sheet.row(1)
    row2 = sheet.row(2)
    for i in range(1, len(row1)):
        dicMap[(row2[i].value.strip())] = row1[i].value.replace('*', '').strip()
    dicCount.append(i)
    x1.release_resources()

print(dicCount, len(dicMap))
# write_date_to_xls(file_name='lazada_th_attr.xls',dataMap=dicMap,title=['EN','TH'])
# write_date_to_xls(file_name='lazada_vi_attr.xls',dataMap=dicMap,title=['EN','VI'])
write_date_to_xls(file_name='lazada_id_attr.xls', dataMap=dicMap, title=['EN', 'ID'])

