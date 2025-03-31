class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def get_nth(node, index):
    if node.data is None:
        raise ValueError()
    count = 0
    while count != index:
        node = node.next
        if node.data is None:
            raise ValueError()
        count += 1
    return node