txt_content=[]

TXT=open('yq_in.txt', 'r', encoding='gbk')
content = TXT.readlines()
long = len(content)
for i in range(long):
    content[i] = content[i].rstrip('\n')
name = content[0].split('\t',1)
txt_content.append(name[0])

for i in range(len(content)):
    province,sceond = content[i].split('\t',1)
    if(province == name):
        txt_content.append('\n'+sceond)
    if(province != name):
        name=province
        txt_content.append('\n'+name)
        txt_content.append('\n'+sceond)

NEWTXT=open('yq_out.txt', 'w', encoding='gbk')
for a in txt_content:
    NEWTXT.write(a)
