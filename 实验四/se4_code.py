# coding=gbk
import sys

def GetData():
    #下边这一块是为读数据做准备
    fileInPath = sys.argv[1]                    # 读取文件的路径
    fileOutPath = "yq_out_04.txt"               # 将输出文件默认置为yq_out_04.txt
    if len(sys.argv) >= 3:
        fileOutPath = sys.argv[2]
    provincialName = ""                         # 将单独选取的省份默认置为yq_out_04.txt
    if len(sys.argv) >= 4:
        provincialName = sys.argv[3]
    fileContent = []
    # 下边这一块是读取数据
    with open(fileInPath, "r") as f:            # 打开文件
        data = f.readlines()                    # 读取文件中每行数据
        for fline in data:                      # 循环读取每行数据
            fileContent.append(fline.split())   # 将每行数据分割后再存入list中
    # 下边这一块是为了去除待明确地区以及去除城市带的省份
    Temp = []
    province = " "
    fileContentFinal = []
    default_string = "待明确地区"
    for fline in fileContent:
        if fline[0] != province:                # 如果读到的省份数据和之前记录的数据不同，则
            Temp.append(fline[0])               # Temp中添加新省份
            fileContentFinal.append(Temp)       # fileContentFina添加Temp
            Temp = []                           # 将Temp置空
            province = fline[0]                 # 更新省份
            Temp.append(fline[1])               # Temp中添加城市与数量
            Temp.append(fline[2])
            fileContentFinal.append(Temp)       # fileContentFina添加Temp
            Temp = []
        elif fline[1] != default_string:        # 省份相同，则只存后边的城市与数字，加个判断是为了去除“待明确地区”
            Temp.append(fline[1])
            Temp.append(fline[2])
            fileContentFinal.append(Temp)
            Temp = []
    # 下边这一块是为了将省份将每个省份与属于这个省份的城市防到一个list中，再将这些list放入一个大list中
    fileContentTemp = []
    fileContentFinal2 = []
    for i in range(len(fileContentFinal)):
        fileContentTemp.append(fileContentFinal[i])
        if i == len(fileContentFinal)-1 or (i < len(fileContentFinal)-1 and len(fileContentFinal[i+1]) == 1):
            fileContentFinal2.append(fileContentTemp)
            fileContentTemp = []
    # 最后返回处理好的结构的读取到的数据以及输出文件名与选取特定省份名
    return fileContentFinal2, fileOutPath, provincialName

def ProcessingData(fileContent):
    # 这个循环是统计每个省份的城市数，再将数字加到包含省份名的list中
    for i in range(len(fileContent)):
        fileContent[i][0].append(str(len(fileContent[i])-1))
    # 下边是为按省份的城市数从大到小排序，如果城市数相同，则按省份名字母从大到小排序
    for i in range(len(fileContent)):
        for j in range(len(fileContent)):
            temp = []
            if int(fileContent[i][0][1]) > int(fileContent[j][0][1]):
                temp = fileContent[i]
                fileContent[i] = fileContent[j]
                fileContent[j] = temp
            if int(fileContent[i][0][1]) == int(fileContent[j][0][1]):
                if fileContent[i][0][0] > fileContent[j][0][0]:
                    temp = fileContent[i]
                    fileContent[i] = fileContent[j]
                    fileContent[j] = temp
    # 下边是为城市数从大到小排序，如果城市数相同，则按省份名字母从大到小排序
    for i in range(len(fileContent)):
        for j in range(len(fileContent[i]))[1:]:
            temp = []
            for k in range(len(fileContent[i]))[1:]:
                if int(fileContent[i][j][1]) > int(fileContent[i][k][1]):
                    temp = fileContent[i][j]
                    fileContent[i][j] = fileContent[i][k]
                    fileContent[i][k] = temp
                if int(fileContent[i][j][1]) == int(fileContent[i][k][1]):
                    if fileContent[i][j][0] > fileContent[i][k][0]:
                        temp = fileContent[i][j]
                        fileContent[i][j] = fileContent[i][k]
                        fileContent[i][k] = temp
    # 返回处理好的数据
    return fileContent

def OutData(fileContent, fileOutPath, provincialName):
    # 写入文件
    with open(fileOutPath, "w") as f:
        for i in range(len(fileContent)):
            # 如果要选定特定省份的情况
            if len(provincialName) > 0:
                if fileContent[i][0][0] == provincialName:
                    for j in range(len(fileContent[i])):
                        if len(fileContent[i][j]) == 1:
                            f.write(fileContent[i][j][0]+'\n')
                        elif len(fileContent[i][j]) == 2:
                            f.write(fileContent[i][j][0]+'\t'+fileContent[i][j][1]+'\n')
                    f.write('\n')
            # 如果不选定特定省份的情况
            else:
                for j in range(len(fileContent[i])):
                    if len(fileContent[i][j]) == 1:
                        f.write(fileContent[i][j][0]+'\n')
                    elif len(fileContent[i][j]) == 2:
                        f.write(fileContent[i][j][0]+'\t'+fileContent[i][j][1]+'\n')
                f.write('\n')

if __name__ == '__main__':
    # 首先运行读取数据模块
    fileContent, fileOutPath, provincialName = GetData()
    print(fileContent)
    print(fileOutPath, provincialName)
    # 然后运行处理数据模块
    fileContent = ProcessingData(fileContent)
    print(fileContent)
    # 最后运行输出数据模块
    OutData(fileContent, fileOutPath, provincialName)