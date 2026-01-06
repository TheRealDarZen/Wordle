import os

from word_tree_node import Node
import pandas as pd

def add_word(word, curr_tree):
    if not word:
        curr_tree.is_word = True
        return
    letter = word[0]
    if letter not in curr_tree.children:
        curr_tree.children[letter] = Node(letter)

    add_word(word[1:], curr_tree.children[letter])


tree = Node('')

dir = 'datasets'
for file in os.listdir(f'{dir}/'):
    if file.endswith('.csv'):
        data = pd.read_csv(f'{dir}/{file}')
        for row in data.itertuples():
            add_word(row[1], tree)
    elif file.endswith('.txt'):
        with open(f'{dir}/{file}', 'r') as file:
            while line := file.readline():
                add_word(line.rstrip(), tree)




