class Node: 
    def __init__(self, value): 
        self.value = value  # Данные
        self.left = self.right = None  # Ссылки на Node's


tree = Node(10)

tree.left = Node(5)  
tree.right = Node(15) 

tree.left.left = Node(3)
tree.left.right = Node(8)

tree.right.left = Node(11)
tree.right.right = Node(16)

print(tree.right.right)  # Выведет <__main__.Node object at 0x0000020F0F592E10>
print(tree.right.right.value)  # Выведет 16
