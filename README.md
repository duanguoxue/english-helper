# english-helper

 > english reading tools

## 系统环境

 > centos 7

 ```
 yum install pdftotext  # 或者 yum install poppler-utils
 ```


## 使用方法
 > pdf 使用 pdftotext 转换为 text文本单词,
 > 使用 ECDICT 查询英文单词释义

 ```
 pdftotext my_en_paper.pdf dest_en_words.txt
 cat dest_en_words.txt | awk '{for (i=1; i<NF;i++) print $i}'  | sort -n | uniq -c  > en_uniq_words_list.txt
 python3 trans_words.py en_uniq_words_list.txt > result_word_zh.txt
 # 清理 中间文件
 ```

