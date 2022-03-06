"""
Задание 1.

Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на примеры с урока,
 сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""
from collections import Counter, deque


class MyNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def huffman_tree(my_text):
    count_s = Counter(my_text)
    sorted_s = deque(sorted(count_s.items(), key=lambda items: items[1]))
    while len(sorted_s) > 1:
        weight = sorted_s[0][1] + sorted_s[1][1]
        node = MyNode(left=sorted_s.popleft()[0], right=sorted_s.popleft()[0])
        for i, item in enumerate(sorted_s):
            if weight > item[1]:
                continue
            else:
                sorted_s.insert(i, (node, weight))
                break
        else:
            sorted_s.append((node, weight))
    return sorted_s[0][0]


def huffman_code(tree, path=''):
    if not isinstance(tree, MyNode):
        code_table[tree] = path
    else:
        huffman_code(tree.left, path=f'{path}0')
        huffman_code(tree.right, path=f'{path}1')


code_table = dict()
text = "beep boop beer!"
huffman_code(huffman_tree(text))
for s in text:
    print(code_table[s], end=' ')