import pandas as pd
import xlrd
import datetime
import os
import xlsxwriter
import shutil
import time

x = datetime.datetime(2021, 5, 19)

####################User Input#####################
dest = "C:\\Users\\balakrishnang\\PycharmProjects\\Namechecker\\Output"#Destination path
path = 'C:\\Users\\balakrishnang\\PycharmProjects\\Namechecker\\Extracts'#extracts path
xlpath = 'C:\\Users\\balakrishnang\\PycharmProjects\\Namechecker\\Inv_File'#excel path
###################################################

date1 = x.strftime("%d%b%Y")
date2 =x.strftime("%d%m%Y")
date3=x.strftime("%d%m%y")
#,yyyyMMdd
date4=x.strftime("%y%m%d")
date5=x.strftime("%Y%m%d")
date6=x.strftime("%d%b%y")
print(date6)


######splitter method#####
def splitter(path):
    if "\\" in path:
      x = path.split("\\")
      S = (x[len(x)-1])
      return S
    else:
        return path
###########################


print("*********************************Execution started*******************************")
t0 = time.time()
filelist = []
xlfile = []
xldata = []
targetfile = ""

writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')
writer.save()

for root, dirs, files in os.walk(path):
    for file in files:
        # append the file name to the list
        filelist.append(os.path.join(root, file))

for root, dirs, files in os.walk(xlpath):
    for file in files:
        # append the file name to the list
        xlfile.append(os.path.join(root, file))

for i in xlfile:
    targetfile = i
    print(targetfile)

for name in filelist:
    print(name)

# open excel file
df = pd.read_excel(targetfile, sheet_name='Extracts', engine='openpyxl')
df1 = df['File name']
df1.to_excel('demo.xlsx',index=False)
df2 = pd.read_excel('demo.xlsx', sheet_name='Sheet1', engine='openpyxl')
#print(df2)
df2['path']=''
print(df2)
# Date to filename logic


for i in df2.index:
    if "\\" in df2['File name'][i]:
        x = df2['File name'][i].split("\\")
        #print(x[len(x) - 1])
        xldata.append(x[len(x) - 1])
        sts = df2['File name'][i]
    else:
        xldata.append(df2['File name'][i])
        sts=df2['File name'][i]

##########################################Replacing Logics ###########################################3333
#Replace %date% type files
    test1 = "ddMMMyyyy"
    if test1 in sts:
        nw=sts.replace(",ddMMMyyyy","").replace("%date%",date1)
        print(nw)
        print(sts)
        for file in filelist:
            if nw in file:
                shutil.copy(file, dest)
                df2['path'][i]=file
#Replace yyyymmdd
    test2 = "yyyyMMdd"
    if test2 in sts:
        nw = sts.replace(",yyyyMMdd,hulk_currentdate;", "").replace("%date%", date4)
        nw = splitter(nw)
        print("changed date "+nw)
        print(sts)
        for file in filelist:
            if nw in file:
                shutil.copy(file, dest)
                df2['path'][i] = file

#Replace ddmmyyyy
    test3 = "ddmmyyyy"
    if test3 in sts:
        nw = sts.replace("ddmmyyyy", date2).replace("%","")
        nw = splitter(nw)
        print(sts)
        for file in filelist:
            if nw in file:
                shutil.copy(file, dest)
                df2['path'][i] = file
                print("Identified :" + file)
        # Replace yyyymmdd
    test2 = "yyyyMMdd"
    if test2 in sts:
            nw = sts.replace(",yyyyMMdd,hulk_currentdate;", "").replace("%date%", date4)
            nw = splitter(nw)
            print("changed date " + nw)
            print(sts)
            for file in filelist:
                if nw in file:
                    shutil.copy(file, dest)
                    df2['path'][i] = file
                    print("Identified :" + file)
# Replace yymmdd without %date%
    test2 = "YYMMDD%"
    if test2 in sts:
            nw = sts.replace("YYMMDD", date4).replace("%","")
            nw = splitter(nw)
            print(sts)
            for file in filelist:
                if nw in file:
                    shutil.copy(file, dest)
                    df2['path'][i] = file
                    print("Identified :" + file)
# Replace yymmdd without %date%
    test2 = "YYYYMMDD"
    if test2 in sts:
        nw = sts.replace("YYYYMMDD", date5).replace("%", "")
        nw = splitter(nw)

        print(sts)
        for file in filelist:
            if nw in file:
                shutil.copy(file, dest)
                df2['path'][i] = file
# Replace ddmmmyy without %date%
    test2 = "DDMMMYY"
    if test2 in sts:
            nw = sts.replace("DDMMMYY", date6).replace("%", "")
            nw = splitter(nw)
            print("date6 Identified :" + nw)
            print(sts)
            for file in filelist:
                if nw in file:
                    shutil.copy(file, dest)
                    df2['path'][i] = file

    if "\n" in sts:
        df2['path'][i]="multiple files found"
df2.to_excel('demo.xlsx', index=False)

print(xldata)
t1 = time.time()
print("***************************Execution completed***********************")
print(f"Time taken for execution is {t1-t0} seconds")
print("*********************************************************************")