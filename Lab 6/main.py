class Node:
    def __init__(self, key, value, color='red'):
        self.key = key
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, None, 'black')
        self.root = self.NIL

    def insert(self, key, value):
        new_node = Node(key, value)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = 'red'
        self._insert_fix(new_node)

    def _insert_fix(self, node):
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._rotate_left(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._rotate_left(node.parent.parent)
        self.root.color = 'black'

    def _rotate_left(self, node):
        right_node = node.right
        node.right = right_node.left
        if right_node.left != self.NIL:
            right_node.left.parent = node

        right_node.parent = node.parent
        if node.parent is None:
            self.root = right_node
        elif node == node.parent.left:
            node.parent.left = right_node
        else:
            node.parent.right = right_node
        right_node.left = node
        node.parent = right_node

    def _rotate_right(self, node):
        left_node = node.left
        node.left = left_node.right
        if left_node.right != self.NIL:
            left_node.right.parent = node

        left_node.parent = node.parent
        if node.parent is None:
            self.root = left_node
        elif node == node.parent.right:
            node.parent.right = left_node
        else:
            node.parent.left = left_node
        left_node.right = node
        node.parent = left_node

    def search(self, key):
        return self._search_tree(self.root, key)

    def _search_tree(self, node, key):
        if node == self.NIL or key == node.key:
            return node
        if key < node.key:
            return self._search_tree(node.left, key)
        return self._search_tree(node.right, key)

    def delete(self, key):
        node = self.search(key)
        if node != self.NIL:
            self._delete_node(node)

    def _delete_node(self, node):
        y = node
        y_original_color = y.color
        if node.left == self.NIL:
            x = node.right
            self._transplant(node, node.right)
        elif node.right == self.NIL:
            x = node.left
            self._transplant(node, node.left)
        else:
            y = self._minimum(node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self._transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color
        if y_original_color == 'black':
            self._delete_fix(x)

    def _delete_fix(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self._rotate_left(x.parent)
                    w = x.parent.right
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self._rotate_right(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self._rotate_left(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self._rotate_right(x.parent)
                    w = x.parent.left
                if w.right.color == 'black' and w.left.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self._rotate_left(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self._rotate_right(x.parent)
                    x = self.root
        x.color = 'black'

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def update(self, key, value):
        node = self.search(key)
        if node != self.NIL:
            node.value = value
        else:
            self.insert(key, value)

class HashTable:
    def __init__(self, size=8):
        self.size = size
        self.table = [RedBlackTree() for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        self.table[index].insert(key, value)

    def search(self, key):
        index = self._hash(key)
        node = self.table[index].search(key)
        if node != self.table[index].NIL:
            return node.value
        return None

    def delete(self, key):
        index = self._hash(key)
        self.table[index].delete(key)
    def update(self, key, value):
        index = self._hash(key)
        self.table[index].update(key, value)

# Создание хеш-таблицы
hash_table = HashTable(10)

# Вставка данных
hash_table.insert("key1", "value1")
hash_table.insert("key2", "value2")

# Поиск данных
print(hash_table.search("key1"))  # Output: value1
print(hash_table.search("key2"))  # Output: value2

# Обновление данных
hash_table.update("key1", "new_value1")
print(hash_table.search("key1"))  # Output: new_value1

# Удаление данных
hash_table.delete("key2")
print(hash_table.search("key2"))  # Output: None


rb_tree = RedBlackTree()

# Вставляем узлы
rb_tree.insert(20, "Value for 20")
rb_tree.insert(15, "Value for 15")
rb_tree.insert(25, "Value for 25")
rb_tree.insert(10, "Value for 10")
rb_tree.insert(18, "Value for 18")
rb_tree.insert(22, "Value for 22")
rb_tree.insert(30, "Value for 30")

# Удаляем узел с ключом 15
rb_tree.delete(15)

# Поиск узла с ключом 15 (должен вернуть NIL)
result = rb_tree.search(15)
if result == rb_tree.NIL:
    print("Узел с ключом 15 успешно удален.")
else:
    print("Ошибка при удалении узла с ключом 15.")

