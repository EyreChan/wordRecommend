from amount import amount_corpus
from pair import dic, w_dic, d_dic, interv
import math
from copy import deepcopy
import json
import re
import jieba.posseg as pseg

corpus = open('corpus.txt', 'r', encoding = 'utf-8-sig')

mi_dic = deepcopy(dic)

datalist1 = []
datalist2 = []
dict_match = {}

def mi(str1, str2):
    if (str1 + ' ' + str2) in mi_dic:
        mi_num = math.log((amount_corpus*dic[str1 + ' ' + str2])/(w_dic[str1]*w_dic[str2]), 2)
        mi_dic.pop(str1 + ' ' + str2)
        return mi_num;
    else:
        return 1;

def frq(str1, str2):
    sum = 0
    for i in range(1, interv + 1):
        str_i = str1 + ' ' + str2 + '%d' % i
        if (str1 + ' ' + str2) in dic and str_i in d_dic:
            sum = sum + d_dic[str_i]
    return sum

def add_dic(str1, str2):
    if str1 == str2:
        print("sta" + str1)
    datalist1.append(str1)
    datalist2.append(str2)
    return

def differ_cixing(str1, str2, j, k, f_strs):
    if f_strs[j] == "a" and f_strs[k] == "n":
        add_dic(str2, str1)
    elif f_strs[j] == "n" and f_strs[k] == "a":
        add_dic(str1, str2)
    elif f_strs[j] == "n" and f_strs[k] == "n":
        add_dic(str1, str2)
        add_dic(str2, str1)
    elif f_strs[j] == "v" and f_strs[k] == "n":
        add_dic(str1, str2)
        add_dic(str2, str1)
    elif f_strs[j] == "v" and f_strs[k] == "a":
        add_dic(str1, str2)
    elif f_strs[j] == "v" and f_strs[k] == "d":
        add_dic(str1, str2)
    else:
        pass

for line in corpus:
    d_strs = line.rstrip('\n').split()
    d_strs = "".join(d_strs)
    d_strs = pseg.cut(d_strs)
    w_strs = []
    f_strs = []
    for (word, flag) in d_strs:
        w_strs.append(word)
        f_strs.append(flag)
    for str in w_strs:
        max_num = min(len(w_strs) - w_strs.index(str) - 1, interv)
        for i in range(1, max_num + 1, 1):
            j = w_strs.index(str)
            str_i = w_strs[j + i]
            k = j + i
            if frq(str, str_i) > 5:
                mi_num = mi(str, str_i)
                if  mi_num >= 10:
                    differ_cixing(str, str_i, j, k, f_strs)

for i in range(0, len(datalist1)):
    if datalist1[i] not in dict_match:
        dict_match[datalist1[i]] = []
        dict_match[datalist1[i]].append(datalist2[i])
    elif datalist1[i] in dict_match:
        if datalist2[i] in dict_match[datalist1[i]]:
            pass
        else:
            dict_match[datalist1[i]].append(datalist2[i])

if "已有" in dict_match:
    dict_match.pop("已有")
if "条岁" in dict_match:
    dict_match.pop("条岁")
if "商震" in dict_match:
    dict_match.pop("商震")
if "兼" in dict_match:
    dict_match.pop("兼")
if "三轮车夫" in dict_match:
    dict_match.pop("三轮车夫")
for key in dict_match:
    if "已有" in dict_match[key]:
        dict_match[key].remove("已有")
    if "条岁" in dict_match[key]:
        dict_match[key].remove("条岁")
    if "商震" in dict_match[key]:
        dict_match[key].remove("商震")
    if "兼" in dict_match[key]:
        dict_match[key].remove("兼")
    if "三轮车夫" in dict_match[key]:
        dict_match[key].remove("三轮车夫")

with open("recommend.json","w", encoding='utf-8') as f1:
    f1.writelines(json.dumps(dict_match, ensure_ascii=False, indent=4))
