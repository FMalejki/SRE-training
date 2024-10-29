class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def add_element(pointer,el):
    if pointer is None:
        pointer.Node(el)
    else:
        while pointer.next != None:
            pointer = pointer.next
        pointer.next = Node(el)

def print_elements(pointer):
    while pointer.next != None:
        print(pointer.value)

def delete_element(p, data):
    while p.next is not None:
        print("aaa")

if __name__ == '__main__':
    p = Node(1)
    add_element(p,1)

#usunięcie duplikatów