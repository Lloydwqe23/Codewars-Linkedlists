class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    if source.data is None:
        raise ValueError()
    check = dest
    dest = Node(source.data)
    dest.next = check
    source = source.next

    return Context(source, dest)