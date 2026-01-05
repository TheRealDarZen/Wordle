from create_tree import tree

def check_word(word, curr_tree):
    if not word and len(curr_tree.children) == 0:
        return True
    letter = word[0]
    for tree_child in curr_tree.children:
        if str(tree_child) == str(letter):
            return check_word(word[1:], tree_child)
    return False

if __name__ == '__main__':
    word = 'house'
    print(check_word(word, tree))