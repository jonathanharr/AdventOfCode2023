class Node:
    # starting_nodes.append((node, ((left, right), left)))
    def __init__(self, node, left, right, current):
        self.node = node
        self.left = left
        self.right = right
        self.current = current

    def set_current(self, left_right_index):
        self.current = self.left if left_right_index == 1 else self.right

    def get_current(self):
        return self.current

    def contains_target_node(self):
        return self.left[2] == 'Z' or self.right[2] == 'Z'

    def __repr__(self):
        return f"{self.node}  =  ({self.left}, {self.right}) {self.current}"

    # def get_node(self):
    #     return self.node
