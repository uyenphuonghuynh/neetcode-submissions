class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None

class LinkedList: 
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        if not curr:
            return -1
        for i in range(0, index):
            if curr:
                curr = curr.next
            else: 
                return -1
        if curr is None: return -1
        return curr.val

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        if index <0:
            return False
        curr = self.head
        
        for i in range(index):
            if curr.next:
                curr = curr.next
            else: return False

        if not curr.next:
            return False
        if curr.next == self.tail:
            self.tail = curr
        curr.next = curr.next.next
        return True

    def getValues(self) -> List[int]:
        curr = self.head.next
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr 
