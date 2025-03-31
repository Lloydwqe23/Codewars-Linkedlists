class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    start = head
    if head is None:
        return head
    already_seen = set([head.data])
    while head.next:
        if head.next.data in already_seen:
            head.next = head.next.next
        else:
            already_seen.add(head.next.data)
            head = head.next
    return start
    