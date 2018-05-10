from machine_learning.deep_learning import Classifier
from data_extraction.data_extractor import Parser

if __name__ == '__main__':
    print('Preprocessing data')
    Parser().pre_process_data()
    print('Training')
    Classifier().train()
