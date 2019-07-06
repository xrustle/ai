from collections import Counter


class MyNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def __repr__(self):
        return f'({self.left}^{self.right})'


class Huffman:
    def __init__(self, string):
        self.string = string
        self.tree = self.__root()
        self.codes = {}
        self.__add_code(self.tree, '')
        self.code = ''
        self.__encode()

    def __root(self):  # Строим дерево Хаффмана, возвращаем корень
        tree = Counter(self.string)

        while len(tree) > 1:
            left, right = tree.most_common()[:-3:-1]

            tree[left[0]] = 0
            tree[right[0]] = 0
            tree += Counter()

            tree[MyNode(left=left[0], right=right[0])] = left[1] + right[1]
        return tree.popitem()[0]

    def __add_code(self, node: MyNode, prefix: str):  # На основе дерева заполняем словарь кодов
        if not isinstance(node.left, MyNode):
            self.codes[node.left] = prefix + '0'
        else:
            self.__add_code(node.left, prefix + '0')

        if not isinstance(node.right, MyNode):
            self.codes[node.right] = prefix + '1'
        else:
            self.__add_code(node.right, prefix + '1')

    def __encode(self):
        for i in self.string:
            self.code += self.codes[i]


if __name__ == '__main__':
    h = Huffman('beep boop beer!')

    print(f'Строка: {h.string}')
    print(f'Дерево: {h.tree}')
    print(f'Коды символов: {h.codes}')
    print(f'Закодированная строка: {h.code}')
