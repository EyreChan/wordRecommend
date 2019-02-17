import json

with open("recommend.json", "r", encoding='utf-8') as f:
    Rec_dic = json.load(f)

#词语搭配推荐
def wordColloc(word):
    if word in Rec_dic:
        return Rec_dic[word]
    else:
        return

#词语替换推荐
def wordSubstit(word):
    for k, v in Rec_dic:
        if word in Rec_dic[k]:
            Rec_dic[k].pop(word)
            return Rec_dic[k]

