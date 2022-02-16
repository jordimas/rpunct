# -*- coding: utf-8 -*-

import sys

sys.path.append('rpunct/')


import logging
from simpletransformers.ner import NERModel
from punctuate import RestorePuncts

if __name__ == "__main__":

    punct_model = RestorePuncts(model="outputs/")
    # read test file
    while True:
        text = input("text:")
    # predict text and print
        punctuated = punct_model.punctuate(text)
        print(punctuated)

