import xlwt



def write_date_to_xls(file_name,dataMap,title):
    wb = xlwt.Workbook(encoding='utf-8')  # 创建工作簿对象
    ws = wb.add_sheet('attr')
    ws.write(0,0,title[0])
    ws.write(0, 1, title[1])
    # 下面类似，写入内容
    row = 1  # 第三行开始写内容数据
    keyList = list(dataMap.keys())
    keyList = sorted(keyList,key=lambda x:x)

    for key in keyList:
        ws.write(row,0,key)
        ws.write(row,1, dataMap[key])
        row += 1
    # 指定每列的宽度
    ws.col(0).width = 6500  # 第0列
    ws.col(1).width = 6500  # 第1列

    # 将数据流保存到本地磁盘
    wb.save('../temp/{}'.format(file_name))

