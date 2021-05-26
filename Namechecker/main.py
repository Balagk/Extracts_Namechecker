import pandas as pd
import xlrd
import datetime
import os
import xlsxwriter
import shutil

x = datetime.datetime(2021, 5, 19)

date1 = x.strftime("%d%b%Y")
date2 =x.strftime("%d%m%Y")
date3=x.strftime("%d%m%y")

######splitter method#####
def splitter(path):
    if "\\" in path:
      x = path.split("\\")
      S = (x[len(x)-1])
      return S
    else:
        return path
###########################
# Copy src to dst. (cp src dst)
shutil.copy("C:\\Users\\balakrishnang\\PycharmProjects\\Namechecker\\Extracts\\two\\aaa19May2021.txt", "C:\\Users\\balakrishnang\\PycharmProjects\\Namechecker")

path = 'C:\\Users\\balakrishnang\\PycharmProjects\\Namechecker\\Extracts'
xlpath = 'C:\\Users\\balakrishnang\\PycharmProjects\\Namechecker\\Inv_File'
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
    xldata.append(df2['File name'][i])
    sts=df2['File name'][i]
    #Replace %date% type files
    test1 = "date"
    if test1 in sts:
        nw=sts.replace(",ddMMMyyyy","").replace("%date%",date1)
        print(nw)
        print(sts)
        for file in filelist:
            if nw in file:
                df2['path'][i]=file
    if "\n" in sts:
        df2['path'][i]="multiple files found"
df2.to_excel('demo.xlsx', index=False)




