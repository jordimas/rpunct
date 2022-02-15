# -*- coding: utf-8 -*-

import sys

sys.path.append('rpunct/')


import logging
from simpletransformers.ner import NERModel
from punctuate import RestorePuncts

if __name__ == "__main__":
    with open('tests/sample_text.txt', 'r') as fp:
        test_sample = fp.readlines()

    punct_model = RestorePuncts(model="outputs/")
    # read test file
    while True:
        text = input("text:")
    # predict text and print
        punctuated = punct_model.punctuate(text)
        print(punctuated)
