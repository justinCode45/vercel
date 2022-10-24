# 資料來源 https://data.taipei/dataset/detail?id=63f31c7e-7fc3-418b-bd82-b95158755b4d  9月
# 用途 ； 把市政府的進出站分離出來，把人數為0的資料剃除
#2022.10.24 30925 陳柏瑄
import csv
f=open("./test.csv",mode="r",encoding="utf-8") 
fi=open("./fi.csv",mode="w",encoding="utf-8", newline='')
fo=open("./fo.csv",mode="w",encoding="utf-8", newline='')

rows=csv.reader(f)


writeri = csv.writer(fi)
writero = csv.writer(fo)


for r in rows:

    if r[2]=="市政府" :
        if r[4]!='0' :
            writeri.writerow(r)
    if r[3]=="市政府" :
        if r[4] !='0':
            writero.writerow(r)


f.close()
fi.close()
