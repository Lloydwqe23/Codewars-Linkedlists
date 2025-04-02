def loop_size(node):
    fast = node
    length = 0
    elements = {}
    while fast != None and fast.next != None:
        if fast in elements:
            return length - elements[fast]
        elements[fast] = length
        fast = fast.next
        length += 1
    return 0