import copy


class List():
    """
    Doubly linked list: The methods are
      - pushright/pushleft to add items
      - popright/popleft to remove and return items

      - Much familiar behavior has been implemented:
         > mylist = List([1,2,3,4,5])
         > sublist = mylist[1:4]
         > mylist[3]
         > mylist[3] = 4
         > mylist[2:5] = List([3,4,5])
     - Supports copy and deepcopy
     - + between two lists does what you expect (returns a new list which is a
         concatenated copy of each of the two lists, not a deep copy!)
    """
    class Node():

        def __init__(self, data=None, prev=None, next=None):
            self.data = data
            self.next = next
            self.prev = prev

        def __str__(self):
            return "{}".format(str(self.data))

        def __repr__(self):
            return f'Node({self.data})'

    def __init__(self, data=[]):
        self.sentinel = List.Node()
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        self.length = 0
        for item in data:
            self.pushright(item)

    class ListIter():

        def __init__(self, sentinel):
            self.cur = sentinel.next
            self.sentinel = sentinel

        def __iter__(self):
            return self

        def __next__(self):
            if self.cur is self.sentinel:
                raise StopIteration
            data = self.cur.data
            self.cur = self.cur.next
            return data

    def get_node(self, i):
        if i >= self.length:
            raise IndexError(f'{i} is out of range!')
        node = self.sentinel
        if i < self.length // 2:
            cur = -1
            while cur < i:
                node = node.next
                cur += 1
        else:
            cur = 0
            while self.length - cur > i:
                node = node.prev
                cur += 1
        return node

    def pushright(self, data):
        self.insert_before(self.sentinel, data)
        return self

    def pushleft(self, data):
        self.insert_after(self.sentinel, data)
        return self

    def popright(self):
        return self.delete_node(self.sentinel.prev)

    def popleft(self):
        return self.delete_node(self.sentinel.next)

    def insert_after(self, node, data):
        new_node = List.Node(data, node, node.next)
        node.next.prev = new_node
        node.next = new_node
        self.length += 1

    def insert(self, i, data):
        if i > self.length:
            raise IndexError(f'{i} is out of range!')
        if i == 0:
            self.insert_after(self.sentinel, data)
        else:
            self.insert_after(self.get_node(i - 1), data)

    def insert_before(self, node, data):
        self.insert_after(node.prev, data)

    def delete_node(self, node):
        if node is not self.sentinel:
            node.next.prev = node.prev
            node.prev.next = node.next
            self.length -= 1
            return node.data
        else:
            raise Exception('Can never remove sentinel')

    def remove(self, i):
        node = self.get_node(i)
        node.prev.next = node.next
        node.next.prev = node.prev

    def __getitem__(self, key):
        if isinstance(key, slice):
            # Get the start, stop, and step from the slice
            return List([self[ii] for ii in range(*key.indices(len(self)))])
        elif isinstance(key, int):
            return self.get_node(key).data

        else:
            raise TypeError(f"{key} is an invalid key.")

    def __setitem__(self, i, data):
        if i >= self.length:
            raise IndexError(f'{i} is out of range!')
        node = self.get_node(i)
        self.insert_after(node, data)
        self.delete_node(node)

    def __iter__(self):
        return List.ListIter(self.sentinel)

    def __len__(self):
        return self.length

    def __copy__(self):
        return List(self.__iter__())

    def __deepcopy__(self, memo):
        newList = List()
        for i in self.__iter__():
            if repr(i) not in memo:
                print(f'{repr(i)} in memo')
                memo[repr(i)] = copy.deepcopy(i)
            newList.pushright(memo[repr(i)])
        return newList

    def __add__(self, other):
        newList = self.__copy__()
        for item in other:
            newList.pushright(item)
        return newList

    def __str__(self):
        # if self.length > 10:
        #    list_str = " -> ".join(itertools.islice((str(node) for node in self),5))
        #    list_str += f' -> ... -> {self.sentinel.prev.data}'
        # else:
        list_str = " -> ".join((str(node) for node in self))
        return f'[{list_str}]'

    def __repr__(self):
        # if self.length > 10:
        #    list_str = ", ".join(itertools.islice((repr(node) for node in self),5))
        #    list_str += f', ..., {self.sentinel.prev.data}'
        # else:
        list_str = ", ".join((repr(node) for node in self))
        return f'List([{list_str}])'
