
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
def push(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def build_one_two_three():
    chained = None
    for number in range(3, 0, -1):
        chained = push(chained, number)
    return chained