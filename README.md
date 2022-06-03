# Korean Head-Tail TnT Part-Of-Speech-Tagger
---

### Introduction
A TnT part-of-speech tagger model trained on Head-Tail tokenized Korean corpus.

This tagger was trained with a Korean corpus consisting of 9,896,518 sentences.

Link to Korean corpus used in training: https://github.com/bufsnlp2030/BUFS-JBNUCorpus2020

### Metrics
<img src="https://ifh.cc/g/mjVqS2.png" width=300>

This tagger was evaluated with a Korean corpus consisting of 30,000 sentences (397,190 Eojeols / 625,180 Tokens).

Eventually, it showed accuracy of 97.00%, 95.49% in eojeol unit test and token unit test respectively.


### What is Head-Tail tokenization?
Head-tail tokenization is a tokenization method for Korean language that separates words into two tokens: a head and a tail.

This tokenization method does not segment all morphemes. Instead, it takes a simple method of separating vocabulary morphemes into heads and grammar morphemes into tails.



### How to use
First, clone the repository. 

Then put the Head-Tail tokenized text file you want to tag in the 'corpus' folder. The format of the data should be as follows.
```
['통합보건교육', '은', '이', '대학', '만의', '특화된', '프로그램', '이다', '.']
['세계', '금융시장', '이', '극심한', '공포', '에서', '잠시', '벗어났', '다', '.']
```


In order to perform POS-tagging, run the following command.
```
python TnT_tagger.py input_file_name.txt
```


This command will create a new text file with POS-tags attached to the tokens in the 'corpus' folder. 
```
[('통합보건교육', 'NNG'), ('은', 'JX'), ('이', 'NP'), ('대학', 'NNG'), ('만의', 'JX_JKG'), ('특화된', 'VV_ETM'), ('프로그램', 'NNG'), ('이다', 'VCP_EF'), ('.', 'SF')]
[('세계', 'NNG'), ('금융시장', 'NNG'), ('이', 'JKS'), ('극심한', 'VA_ETM'), ('공포', 'NNG'), ('에서', 'JKB'), ('잠시', 'MAG'), ('벗어났', 'VV'), ('다', 'EP_EF'), ('.', 'SF')]
```


