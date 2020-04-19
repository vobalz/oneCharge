class node():
    def __init__(self, num):
        self.var = num
        self.next = None

    def __str__(self):
        return 'Node var {}'.format(self.var)

class SLinkedList():
    def __init__(self,):
        self.head = None

    def push(self, num):
        new_node = node(num)
        new_node.next = self.head
        self.head = new_node

def find_middle_node(LList):
    slow = fast = LList.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

if __name__ == '__main__':
    list = [i for i in range(7)]
    print(list)

    LList = SLinkedList()
    for n in list:
        LList.push(n)

    result = find_middle_node(LList)
    print('The middle node is', result)
