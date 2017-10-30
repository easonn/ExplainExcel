#!/usr/bin/env python
# -*- coding: utf-8 -*-


import xlrd



def dictInit():
    data = xlrd.open_workbook('C:/Users/Administrator/Desktop/反欺诈/数据字典New.xlsx')
    table = data.sheets()[0]
    nrows = table.nrows
    for i in range(nrows):
        row_value = table.row_values(i)
        # print(row_value[1], row_value[4])
        key = "_".join(row_value[1].split("_")[2:])
        value = "，".join(row_value[4].split("，")[1:])
        print(key, value)
        dict[key] = value

def formateTxt():
    str = ""
    results=[]
    file = open("C:/Users/Administrator/Desktop/反欺诈/result（多头）New.txt",'r',encoding='utf-8')
    for line in file.readlines():
        lineTxt =  line.split(":")
        if len(lineTxt) > 1:
            key_words = lineTxt[0].strip().strip('"').split("_")
            key = "_".join(key_words[2:])
            if (dict.__contains__(key)):
                date = key_words[1]
                m = ""
                n = ""
                if date[0] == "d":
                    m = "天"
                elif date[0] == "m":
                    m = "月"
                res = dict[key]+lineTxt[1]
                results.append('近'+date[1]+m+'内，'+res)
        else:
            results.append(line)
    return results

dict = {}

dictInit()

results = formateTxt()

r = '\n'.join(results)

f = open("C:/Users/Administrator/Desktop/反欺诈/test.txt","w",encoding='utf-8')
f.write(r)
f.close()

print(dict['lm_cell_nbank_com_orgnum'])





