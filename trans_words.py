'''
usage :
yum install pdftotext or yum install poppler-utils
pdftotext my.pdf my.txt
cat my.txt | awk '{for (i=1; i<NF;i++) print $i}'  | sort | uniq -c  > en_words.txt
'''
import re
import sys
sys.path.append('./ECDICT')
#print (sys.path)
from stardict import LemmaDB
from stardict import DictCsv
import stopwords

if len(sys.argv) < 2:
    sys.exit(0)

lemma = LemmaDB()
lemma.load('./ECDICT/lemma.en.txt')
dc = DictCsv('./ECDICT/ecdict.csv')

uniq_word = set()
with open(sys.argv[1]) as f:
  for line in f:
    #words = re.findall(r'\'?\w+', s)
    words = re.findall(r'[\w]+', line)
    for w in words:
        l = lemma.word_stem(w.lower())
        if not l:
            continue
        # 排除单字母及重复词
        if l[0] in uniq_word or l[0] in stopwords.stopwords or len(l[0]) < 2:
            continue
        uniq_word.add(l[0])  # 去重set
        query_val = dc.query(l[0])
        if not query_val:
            continue
        print ([l[0]], [query_val.get('phonetic', '')], query_val.get('translation', "").replace('\n', ', '))

