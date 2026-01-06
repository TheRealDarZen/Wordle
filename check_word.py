from create_tree import tree

def check_word(word, curr_tree):
    if not word:
        if curr_tree.is_word:
            return True
        else:
            return False
    letter = word[0]

    if letter not in curr_tree.children:
        return False
    return check_word(word[1:], curr_tree.children[letter])

if __name__ == '__main__':
    word = 'A-and-R'
    print(check_word(word, tree))