# Дан односвязный список.
# У списка есть только два свойства: для доступа к данным в ячейке и для доступа к следующей ячейке списка.
# Задача. Вывести содержимое всех ячеек списка в обратном порядке. Список разрешается обойти всего один раз.
# Использовать вспомогательные переменные запрещено.


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


forw_list = Node(0, Node(1, Node(2, Node(3))))


def print_nodes(head):
    while head:
        print(head.value)
        head = head.next


def add_elemetd(head, data):
    if head.next is not None:
        add_elemetd(head.next, data)
    else:
        head.next = Node(data, None)


def print_revers(head):
    if head.next is not None:
        print_revers(head.next)
    print(head.value)


# print(print_nodes(forw_list))
# add_elemetd(forw_list, 4)
# print(print_nodes(forw_list))
print_revers(forw_list)
