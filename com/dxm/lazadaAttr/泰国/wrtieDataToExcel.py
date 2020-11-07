import xlwt
import csv

def write_data_to_xls(file_name,datas,title):
    wb = xlwt.Workbook(encoding='utf-8')  # 创建工作簿对象
    ws = wb.add_sheet('attr')
    for i in range(0,len(title)):
        ws.write(0,i,title[i])
    # 下面类似，写入内容
    row = 1  # 第三行开始写内容数据


    for data in datas:
        for i in range(0,len(data)):
            ws.write(row,i,data[i])
        row += 1
    # 指定每列的宽度
    for i in range(0,len(title)):
        ws.col(i).width = 6500  # 第0列

    # 将数据流保存到本地磁盘
    #wb.save('../temp/{}'.format(file_name))
    wb.save('d://{}'.format(file_name))
datas=[]
with open('record.txt', mode='r', encoding='utf-8') as f:
        for line in f.readlines():
            arr= line.replace("\n","").split("|")

            cids = arr[0].replace("\"","").replace(",","|")
            label = arr[1]
            label_site = arr[2]
            print(label,label_site,cids)
            datas.append(['TH',label,label_site,cids])

write_data_to_xls('lazada_th_attrs_generate.xls',datas,['site','label','labelSite','categoryIds'])
