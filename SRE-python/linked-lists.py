class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def add_elements(p,arr):
    for el in arr:
        add_element(p,el)

def add_element_on_place(p,el,place):
    if place == 0:
        p, p.next = Node(el),p
        return p
    else:
        start = p
        i = 1
        while p.next is not None:
            if i == place:
                p.next, p.next.next = Node(el), p.next
                return start
            else:
                p = p.next
            i+=1
        p.next = Node(el)
        return start




def add_element(pointer,el):
    if pointer is None:
        pointer.Node(el)
    else:
        while pointer.next != None:
            pointer = pointer.next
        pointer.next = Node(el)

def print_elements(pointer):
    while pointer.next is not None:
        print(pointer.value)
        pointer = pointer.next
    print(pointer.value)


#first appear of a number
def delete_element(head, data):
    if head is None:
        return None
    if head.value == data:
        return head.next  # new head of the list
    current = head
    while current.next is not None:
        if current.next.value == data:
            current.next = current.next.next
            return head  # return the head of the modified list
        current = current.next
    return head

def reverse_linklist(head):
    now = head
    prev = None
    while now is not None:
        next_node = now.next
        now.next = prev
        prev = now
        now = next_node
    return prev

def delete_duplicates(head):
    #O(n) solution set()
    arr = set()
    current = head
    arr.add(current.value)
    while current.next is not None:
        if current.next.value in arr:
            current.next = current.next.next
        else:
            arr.add(current.next.value)
        if current.next is not None:
            current = current.next
        else:
            break
    return head

def delete_duplicats_n2(head):
    prev = None
    current = head
    while current is not None:
        runner = current
        while runner is not None and runner.next is not None:
            if current.value == runner.next.value:
                runner.next = runner.next.next
            runner = runner.next
        current = current.next
    return head

p = Node(1)
add_elements(p,[1,5,7,3])
p = add_element_on_place(p,3,8)
p = delete_element(p,5)
p = reverse_linklist(p)
p = delete_duplicats_n2(p)
print_elements(p)