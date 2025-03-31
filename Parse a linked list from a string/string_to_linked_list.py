class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next


def linked_list_from_string(s):
    new_node = Node(5)
    curr_node = new_node
    for element in s.split(" -> ")[:-1]:
        curr_node.next = Node(int(element))
        curr_node = curr_node.next
    return new_node.next