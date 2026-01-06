import pickle
from os.path import exists

imported_tree = None

if not exists('tree.pickle'):
    from create_tree import tree
    with open('tree.pickle', 'wb') as file:
        pickle.dump(tree, file)

with open('tree.pickle', 'rb') as file:
    imported_tree = pickle.load(file)


