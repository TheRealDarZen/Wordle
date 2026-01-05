
class Node:
    def __init__(self, letter):
        self.letter = letter
        self.children = []

    def __str__(self):
        return str(self.letter)