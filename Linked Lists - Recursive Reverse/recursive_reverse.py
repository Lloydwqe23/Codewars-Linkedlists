class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    def recursive_reverse(node, prev):
        if node is None:
            return prev
        next_element = node.next
        node.next = prev
        return recursive_reverse(next_element, node)
    return recursive_reverse(head, None)

    