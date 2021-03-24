import pandas as pd
import streamlit
from collections import defaultdict
from ntlk import metrics

word_list_paths = ['./data/development/english.csv', './data/development/german.csv']
ignore_columns = ['confidence', 'description', 'domainelement_pk', 'frequency', 'jsondata', 'loan', 'markup_description', 'pk', 'valueset_pk']

# asjp named all of the columns :shrug:
name = 'name'
nameId = 'id'

# columns for the meta table
edit_distance = "edit_distance"
lcp = 'longest_common_prefix'
cbg = 'number_of_common_bigrams'
word_length = 'wordlength'
wlabs = 'absolute_diff_word_length'


def same_meaning(x, y):
    """ takes two ids  eg.(ENGLISH-1-1, GERMAN-11-2) """
    return x.split('-')[:-2] != y.split('-')[-2]

def load(path):
    df = pd.read_csv(path)
    return df.drop(ignore_columns)


def trainBinaryClassifier(word_lists):
    """ word_lists is an array of dataframes each containing a list of words and their meanings"""

def pairwise(x, y):
    """ expects two dataframes to compare """
    meta_x = defaultdict([])
    for word in x:
        meta_x[edit_distance] =


def Run(paths):
    # sets = [load(path) for path in path]


