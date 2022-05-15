# -*- coding: utf-8 -*-
# C> TnT_tagger_test.py input.txt

# Input : list of tokens (sentence)
# Output: POS-tagged

from nltk.tag import tnt
from pickle import dump, load
import time, sys, ast
sys.setrecursionlimit(1000000)

def load_tagging_model(model_file):
    tagger_file = open(model_file, 'rb')
    tnt_tagger = load(tagger_file)
    tagger_file.close()
    return tnt_tagger

def load_tagged_corpus(in_file):
    data = []
    with open(in_file, 'r', encoding='utf8') as fin:
        while True:
            d = fin.readline()
            if not d:
                break
            data.append(ast.literal_eval(d))
    fin.close()
    return data

def get_sentence_tokens(in_file):
    test_data_tokens = []
    with open(in_file, 'r', encoding='utf8') as fin:
        while True:
            sent = fin.readline().strip()
            if not sent:
                break
            test_data_tokens.append(ast.literal_eval(sent))
    return test_data_tokens

def evaluate_tnt_tagger(tnt_tagger, test_data):
    # evaluating -- 태거 성능 평가
    print('Evaluating...', time.ctime())

    #n_data = len(test_data)
    #a = tnt_tagging.evaluate(test_data)
    #n_data = 100  # for testing 100 sentences
    n_data = len(test_data)
    a = tnt_tagger.evaluate(test_data)

    print(f"--> Accuracy of TnT tagging for {n_data} sentences:", a)


if __name__ == "__main__":
    model_file = "model/TnT_tagger_model.pkl"
    in_file = "corpus/test_data_tokens.txt"
    result_file = in_file[:-4] + '_tagged_result.txt'
    tnt_tagger = load_tagging_model(model_file)  # 직접 학습 대신에 model 파일 로딩

    sent = ['이', '정부', '가', ',', '국민', '에게', '탄핵당한', '정부', '가', '왜', '이렇', '게', '사드', '배치', '를', '서두르', '는지', '이해할', '수', '가', '없', '다', '.']
    sent_tagged = tnt_tagger.tag(sent)
    print('\n', sent, '\n-->\n', sent_tagged)


    test_data_tokens = get_sentence_tokens(in_file)
    with open(result_file, 'w', encoding='utf8') as fout:
        for sent in test_data_tokens:
            sent_tagged = tnt_tagger.tag(sent)
            fout.write(str(sent_tagged)+'\n')
            print('\n', sent, '\n-->\n', sent_tagged)

    print(f'--- Created {result_file} ---')    
    # test_data = load_tagged_corpus(in_file)
    # print('Test data size: ', len(test_data))
    # evaluate_tnt_tagger(tnt_tagger, test_data)