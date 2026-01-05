import os

from pandas.core.interchange.dataframe_protocol import DataFrame

from word_tree_node import Node
import pandas as pd

tree = Node('')

def add_word(word, curr_tree):
    if not word:
        return
    letter = word[0]
    child = None
    for tree_child in curr_tree.children:
        if str(tree_child) == str(letter):
                child = tree_child
                curr_tree.children.remove(tree_child)
                break
    if child is None:
        child = Node(letter)

    add_word(word[1:], child)
    curr_tree.children.append(child)


dir = 'datasets'
for file in os.listdir(f'{dir}/'):
    data = pd.read_csv(f'{dir}/{file}')
    for row in data.itertuples():
        add_word(row[1], tree)




