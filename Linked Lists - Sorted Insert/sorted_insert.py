""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    if head is None or head.data > data:
        check = head
        head = Node(data)
        head.next = check
        return head
    start = head
    while start.next and start.next.data < data:
        start = start.next
    if start.data > data:
        next_element = start
        start = Node(data)
        start.next = next_element
    else:
        next_element = start.next
        start.next = Node(data)
        start.next.next = next_element
    return head
