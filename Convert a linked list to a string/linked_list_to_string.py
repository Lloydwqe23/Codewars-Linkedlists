class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next


def stringify(node):
    result = ''
    while node:
        result += f'{str(node.data)} -> '
        node = node.next
    result += 'None'
    return result