zhuangtai=[0,0,0,0,0,
                    0,1,0,0,1,
                    0,0,0,0,0,
                    0,0,0,0,1,
                    0,0,0,0,0,
                    0,0,0,0,]
name=["袁文博","于申顺","高小立","高鸿文","弯伟杰",
        "舒文君","靳文祥","高恒星","郑金萌","张凯乐",
        "郭溢河","顾光豪","杨晋硕","问涛也","亢欣欣",
        "杨迎龙","王家骏","张豪石","王子豪","李展旗",
        "姚纪川","王宏宇","张子豪","刘任杰","刘成真",
        "宋久阳","景阳阳","樊创","宋傲仔"]
import os

dir_ls=os.listdir()

for i in range(0,len(dir_ls)):
    mm=dir_ls[i]
    if '.' not in mm:
        mz=mm.split('_')[0]
        try:
            zhuangtai[name.index(mz)]=1
        except ValueError:
            print(mz,"名单中未出现该任务名称")
s=1
for i in range(0,len(zhuangtai)):

    print(zhuangtai[i],end='')
    if i==len(zhuangtai)-1:
        break
    print(',',end='')
    if s==5:
        print()
        s=0
    s+=1


