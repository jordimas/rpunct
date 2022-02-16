# -*- coding: utf-8 -*-

import sys
import datetime

sys.path.append('rpunct/')


import logging
from simpletransformers.ner import NERModel
from punctuate import RestorePuncts

if __name__ == "__main__":

    start_time = datetime.datetime.now()

    with open('inference/sample_text.txt', 'r') as fp:
        test_sample = fp.readlines()

    punct_model = RestorePuncts(model="outputs/")
    for line in test_sample:
        line = line.strip()
        if len(line) == 0:
            continue

        print(f"source: '{line}'")
        punctuated = punct_model.punctuate(line)
        print(f"result: '{punctuated}'")
        print("--")


    s = 'Time used: {0}'.format(datetime.datetime.now() - start_time)
    print(s)
