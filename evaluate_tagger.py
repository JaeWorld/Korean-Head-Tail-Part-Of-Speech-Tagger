# -*- coding: utf-8 -*-
# C> evaluate_tagger.py input.txt

# Input : list of (tokens, tags) 
# Output: POS-tagging accuracy

from nltk.tag import tnt
from pickle import dump, load
import time, sys, ast
sys.setrecursionlimit(1000000)

def load_tagging_model(model_file):
    tagger_file = open(model_file, 'rb')
    tnt_tagger = load(tagger_file)
    tagger_file.close()
    return tnt_tagger

def evaluate_tnt_tagger(tnt_tagger, test_data):
    print('Evaluating...', time.ctime())

    n_data = 100  # for testing specific number of sentences
    # n_data = len(test_data)
    a = tnt_tagger.evaluate(test_data[:n_data])

    print(f"--> Accuracy of TnT tagging for {n_data} sentences: {a:.4f}")

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

if __name__ == "__main__":
    model_file = "model/TnT_tagger_model.pkl"
    in_file = f"corpus/{sys.argv[1]}"
    result_file = in_file[:-4] + '_tagged_result.txt'
    tnt_tagger = load_tagging_model(model_file)  # 직접 학습 대신에 model 파일 로딩

    print('--- Starting evaluation ---')

    test_data = load_tagged_corpus(in_file)
    print('Test data size: ', len(test_data))
    evaluate_tnt_tagger(tnt_tagger, test_data)