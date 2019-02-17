corpus = open('corpus.txt', 'r', encoding = 'utf-8-sig')

dic = {}
w_dic = {}
d_dic = {}

interv = 5
for line in corpus:
    strs = line.rstrip('\n').split()
    for str in strs:
        max_num = min(len(strs) - strs.index(str) - 1, interv)
        for i in range(1, max_num + 1, 1):
            stri = strs[strs.index(str) + i]
            str_ = str + ' ' + strs[strs.index(str) + i]
            if stri != str and str_ not in dic:
                dic[str_] = 1
            elif stri != str and str_ in dic:
                dic[str_] = dic[str_] + 1
            str_i = str + ' ' + strs[strs.index(str) + i] + '%d'%i
            if str_i in d_dic:
                d_dic[str_i] = d_dic[str_i] + 1
            else:
                d_dic[str_i] = 1
        if str in w_dic:
            w_dic[str] = w_dic[str] + 1
        else:
            w_dic[str] = 1

#print(d_dic)
#print(dic)
#print(w_dic)