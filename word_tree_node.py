
class Node:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.is_word = False

    def __str__(self):
        return str(self.letter)