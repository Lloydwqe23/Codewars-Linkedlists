class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    check = head
    if head is None:
        raise ValueError()
    
    count = 1
    while check.next:
        check = check.next
        count += 1

    if count < 2:
        raise ValueError()

    traverse = head
    lists = Context(Node(head.data), None)
    first_list = lists.first
    count = 2
    while traverse.next:
        traverse = traverse.next
        if count % 2 == 0:
            if lists.second is None:
                lists.second = Node(traverse.data)
                second_list = lists.second
            else:
                second_list.next = Node(traverse.data)
                second_list = second_list.next
        else:
            first_list.next = Node(traverse.data)
            first_list = first_list.next
        count += 1
    return lists
    