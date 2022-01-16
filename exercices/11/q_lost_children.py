def is_every_child_here(first_child):
    current_child = first_child
    while current_child:
        if current_child.is_next_valid():
            current_child = current_child.next_child()
            if current_child.next_child() == first_child:
                return True
        else:
            return False
