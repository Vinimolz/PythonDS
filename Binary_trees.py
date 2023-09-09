import queue


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def depth_first_value(root):
    stack = []
    if root is not None:
        stack.append(root)
    else:
        return []

    while len(stack) != 0:
        curr = stack.pop()
        print(curr.value)

        if curr.right:
            stack.append(curr.right)

        if curr.left:
            stack.append(curr.left)


def depth_first_value_recursive(root):

    if root is None:
        return []

    left = depth_first_value_recursive(root.left)

    right = depth_first_value_recursive(root.right)

    return [root.value] + left + right


def breadth_first_traversal(root):
    my_queue = queue.Queue()
    elem = []
    if root is None:
        return elem
    my_queue.put(root)

    while not my_queue.empty():
        curr = my_queue.get()
        elem.append(curr.value)

        if curr.left:
            my_queue.put(curr.left)

        if curr.right:
            my_queue.put(curr.right)

    return elem


def node_exists(root, target):
    if root is None:
        return False

    my_queue = queue.Queue()

    my_queue.put(root)

    while not my_queue.empty():
        curr = my_queue.get()

        if curr == target:
            return True

        if curr.left:
            my_queue.put(curr.left)

        if curr.right:
            my_queue.put(curr.right)

    return False


def node_exists_recur(root, target):
    if root is None:
        return False

    if root.value == target:
        return True

    return node_exists_recur(root.left, target) or node_exists_recur(root.right, target)


def tree_sum_recur(root):
    if root is None:
        return 0

    return root.value + tree_sum_recur(root.left) + tree_sum_recur(root.right)


def tree_sum(root):
    if root is None:
        return 0

    q = queue.Queue()
    q.put(root)

    t_sum = 0

    while not q.empty():
        curr = q.get()
        t_sum += curr.value

        if curr.left:
            q.put(curr.left)

        if curr.right:
            q.put(curr.right)

    return t_sum


def min_value(root):
    if root is None:
        return float("inf")

    left_min = min_value(root.left)
    right_min = min_value(root.right)

    return min(root.value, left_min, right_min)


if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.right = c
    a.left = b
    b.right = e
    b.left = d
    c.right = f

    # depth_first_value(a)

    # print(depth_first_value_recursive(a))

    # print(breadth_first_traversal(a))

    if node_exists(a, e):
        print('YESS SIR')
    else:
        print('TOO BAD')

    if node_exists_recur(a, 'e'):
        print('HERE TOO')
    else:
        print('TOO TOO BAD')

    a.value = 2
    b.value = 23
    c.value = 7
    d.value = 4
    e.value = 13
    f.value = 1

    print(tree_sum_recur(a))

    print(tree_sum(a))

    print(min_value(a))
