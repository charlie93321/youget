import xlrd
import xlwt


def getDatas():
    datas = []
    with open('record.txt', mode='r', encoding='utf-8') as f:
        for line in f.readlines():
            arr = line.split("|")
            cids = arr[0].replace("\"", "").replace(",", "|")
            label = arr[1]
            label_site = arr[2]
            file = arr[3]
            datas.append(['VN', label, label_site, cids,file])
    return datas


labels=[]
lableSites=[]
record={}
record2={}
is_change= False
with open('../lazada分类/now.txt',mode='r',encoding='utf-8') as f:
    for line in f.readlines():
        if "|||||||||||||"==line.strip():
            is_change=True
            continue
        if is_change:
            lableSites.append(line.replace("\n","").strip())
        else:
            labels.append(line.replace("\n","").strip())
for i in range(0,len(labels)):
    record[labels[i]]=lableSites[i]
    record2[labels[i].upper()]=labels[i]

datas = getDatas()
newDatas=[]
dicMap={}
for data in datas:
    key = data[1]
    val = data[2]
    file1 = data[4].replace("\n",'')
    if key not in dicMap:
        dicMap[key]={}
    dicMap[key][val]=file1
    if key not in record:
        if key.upper() in record2:
            print("key is  not in  record but can be up lower match :{},{},{}".format(key, record[record2[key.upper()]], val))
        else:
            print("key is not record:{},{}".format(key, val))
    else:
       if  record[key] != val:
            #print("value is not match:{},{},{},{}".format(key,record[key],val,file1))
            newDatas.append([key,record[key],val])







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

for d in newDatas:
    k = d[0]
    v1 = d[1]
    v2 = d[2]
    d.append(dicMap[k][v1])
    d.append(dicMap[k][v2])
    print(d)

write_data_to_xls('diff_vn_attr.xls',newDatas,['label','越南语1','越南语2','文件1','文件2'])