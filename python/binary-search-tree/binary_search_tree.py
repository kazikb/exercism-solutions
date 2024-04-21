# Fajne wyjaśnienie tematu:
# https://www.alpharithms.com/binary-trees-in-python-162215/
# https://www.youtube.com/watch?v=lFq5mYUWEBk
#
# Opis algorytmu na wiki
# https://en.wikipedia.org/wiki/Binary_search_tree

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        self._root = None
        for data in tree_data:
            self.insert(data)

    def insert(self, data):
        if self._root is None:
            self._root = TreeNode(data)
            return

        find_place = False
        curent_leaf = self._root

        while not find_place:
            # add data on a right subtree
            if data > curent_leaf.data:
                if curent_leaf.right:
                    curent_leaf = curent_leaf.right
                else:
                    curent_leaf.right = TreeNode(data)
                    find_place = True
            # add data on a left subtree
            else:
                if curent_leaf.left:
                    curent_leaf = curent_leaf.left
                else:
                    curent_leaf.left = TreeNode(data)
                    find_place = True


    def data(self):
        return self._root

    def in_order_traversal(self, leaf, sorted_elements):
        # In order traversal outputs the Left Node, the Root Node, and then the Right Node.

        if leaf is not None:
            self.in_order_traversal(leaf.left, sorted_elements)
            sorted_elements.append(leaf.data)
            self.in_order_traversal(leaf.right, sorted_elements)

    def sorted_data(self):
        sorted_elements = []
        self.in_order_traversal(self._root, sorted_elements)
        return sorted_elements
