# coding=gbk
import sys

def GetData():
    #�±���һ����Ϊ��������׼��
    fileInPath = sys.argv[1]                    # ��ȡ�ļ���·��
    fileOutPath = "yq_out_04.txt"               # ������ļ�Ĭ����Ϊyq_out_04.txt
    if len(sys.argv) >= 3:
        fileOutPath = sys.argv[2]
    provincialName = ""                         # ������ѡȡ��ʡ��Ĭ����Ϊyq_out_04.txt
    if len(sys.argv) >= 4:
        provincialName = sys.argv[3]
    fileContent = []
    # �±���һ���Ƕ�ȡ����
    with open(fileInPath, "r") as f:            # ���ļ�
        data = f.readlines()                    # ��ȡ�ļ���ÿ������
        for fline in data:                      # ѭ����ȡÿ������
            fileContent.append(fline.split())   # ��ÿ�����ݷָ���ٴ���list��
    # �±���һ����Ϊ��ȥ������ȷ�����Լ�ȥ�����д���ʡ��
    Temp = []
    province = " "
    fileContentFinal = []
    default_string = "����ȷ����"
    for fline in fileContent:
        if fline[0] != province:                # ���������ʡ�����ݺ�֮ǰ��¼�����ݲ�ͬ����
            Temp.append(fline[0])               # Temp�������ʡ��
            fileContentFinal.append(Temp)       # fileContentFina���Temp
            Temp = []                           # ��Temp�ÿ�
            province = fline[0]                 # ����ʡ��
            Temp.append(fline[1])               # Temp����ӳ���������
            Temp.append(fline[2])
            fileContentFinal.append(Temp)       # fileContentFina���Temp
            Temp = []
        elif fline[1] != default_string:        # ʡ����ͬ����ֻ���ߵĳ��������֣��Ӹ��ж���Ϊ��ȥ��������ȷ������
            Temp.append(fline[1])
            Temp.append(fline[2])
            fileContentFinal.append(Temp)
            Temp = []
    # �±���һ����Ϊ�˽�ʡ�ݽ�ÿ��ʡ�����������ʡ�ݵĳ��з���һ��list�У��ٽ���Щlist����һ����list��
    fileContentTemp = []
    fileContentFinal2 = []
    for i in range(len(fileContentFinal)):
        fileContentTemp.append(fileContentFinal[i])
        if i == len(fileContentFinal)-1 or (i < len(fileContentFinal)-1 and len(fileContentFinal[i+1]) == 1):
            fileContentFinal2.append(fileContentTemp)
            fileContentTemp = []
    # ��󷵻ش���õĽṹ�Ķ�ȡ���������Լ�����ļ�����ѡȡ�ض�ʡ����
    return fileContentFinal2, fileOutPath, provincialName

def ProcessingData(fileContent):
    # ���ѭ����ͳ��ÿ��ʡ�ݵĳ��������ٽ����ּӵ�����ʡ������list��
    for i in range(len(fileContent)):
        fileContent[i][0].append(str(len(fileContent[i])-1))
    # �±���Ϊ��ʡ�ݵĳ������Ӵ�С���������������ͬ����ʡ������ĸ�Ӵ�С����
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
    # �±���Ϊ�������Ӵ�С���������������ͬ����ʡ������ĸ�Ӵ�С����
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
    # ���ش���õ�����
    return fileContent

def OutData(fileContent, fileOutPath, provincialName):
    # д���ļ�
    with open(fileOutPath, "w") as f:
        for i in range(len(fileContent)):
            # ���Ҫѡ���ض�ʡ�ݵ����
            if len(provincialName) > 0:
                if fileContent[i][0][0] == provincialName:
                    for j in range(len(fileContent[i])):
                        if len(fileContent[i][j]) == 1:
                            f.write(fileContent[i][j][0]+'\n')
                        elif len(fileContent[i][j]) == 2:
                            f.write(fileContent[i][j][0]+'\t'+fileContent[i][j][1]+'\n')
                    f.write('\n')
            # �����ѡ���ض�ʡ�ݵ����
            else:
                for j in range(len(fileContent[i])):
                    if len(fileContent[i][j]) == 1:
                        f.write(fileContent[i][j][0]+'\n')
                    elif len(fileContent[i][j]) == 2:
                        f.write(fileContent[i][j][0]+'\t'+fileContent[i][j][1]+'\n')
                f.write('\n')

if __name__ == '__main__':
    # �������ж�ȡ����ģ��
    fileContent, fileOutPath, provincialName = GetData()
    print(fileContent)
    print(fileOutPath, provincialName)
    # Ȼ�����д�������ģ��
    fileContent = ProcessingData(fileContent)
    print(fileContent)
    # ��������������ģ��
    OutData(fileContent, fileOutPath, provincialName)