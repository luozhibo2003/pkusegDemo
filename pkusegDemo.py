
import pkuseg
from collections import Counter
import pprint

content = []
with open('zhangxiaolongyanjiang.txt',encoding='utf-8') as f:
    content = f.read()
    # print(content)

# 希望分词时用户词典中的词固定不分开
lexicon = ['小程序','公众号','朋友圈']

# 以默认配置加载模型,给定用户词典
seg = pkuseg.pkuseg(user_dict=lexicon)

# 进行分词
text = seg.cut(content)


#停用词
stopwords = []
with open('stopwords.txt',encoding='utf-8') as f:
    stopwords = f.read()

new_text = []
for w in text:
    if w not in stopwords:
        new_text.append(w)

counter = Counter(new_text)
pprint.pprint(counter.most_common(20))