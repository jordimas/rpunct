# -*- coding: utf-8 -*-

import sys

sys.path.append('rpunct/')


import logging
from simpletransformers.ner import NERModel
from punctuate import RestorePuncts

if __name__ == "__main__":
    punct_model = RestorePuncts(model="outputs/")
    for line in test_sample:
        line = line.strip()
        if len(line) == 0:
            continue

        print(f"source: '{line}'")
        punctuated = punct_model.punctuate(line)
        print(f"result: '{punctuated}'")
        print("--")
