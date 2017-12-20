class Element(object):

    def __init__(self, data):
        self.previous = None
        self.next = None
        self.data = data

    def set_next(self, next):
        self.next = next

    def set_previous(self, previous):
        self.previous = previous

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous

    def get_data(self):
        return self.data


class FastLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_to_first(self, element):
        if self.list_size() == 0:
            self.head = element
            self.tail = element
        else:
            self.head.set_previous(element)
            element.set_next(self.head)
            self.head = element
        self.size += 1

    def add_to_last(self, element):
        if self.list_size() == 0:
            self.head = element
            self.tail = element
        else:
            self.tail.set_next(element)
            element.set_previous(self.tail)
            self.tail = element
        self.size += 1

    def move_to_first(self, element):
        if element == self.head:
            return
        prev = element.get_previous()
        next = element.get_next()
        prev.set_next(next)
        if next is not None:
            next.set_previous(prev)
        else:
            self.tail = prev
        element.set_previous(None)
        element.set_next(self.head)
        self.head.set_previous(element)
        self.head = element

    def remove_element(self, element):
        prev = element.get_previous()
        next = element.get_next()
        if prev is not None:
            prev.set_next(next)
        else:
            self.head = next
        if next is not None:
            next.set_previous(prev)
        else:
            self.tail = prev
        element.set_previous(None)
        element.set_next(None)
        self.size -= 1

    def remove_from_first(self):
        h = self.head
        next = h.get_next()
        if next is not None:
            next.set_previous(None)
        else:
            self.tail = None
        h.set_next(None)
        self.head = next
        self.size -= 1
        return h

    def remove_from_last(self):
        t = self.tail
        prev = t.get_previous()
        if prev is not None:
            prev.set_next(None)
        else:
            self.head = None
        t.set_previous(None)
        self.tail = prev
        self.size -= 1
        return t

    def get_first(self):
        return self.head

    def get_last(self):
        return self.tail

    def list_size(self):
        return self.size

    def is_empty(self):
        return self.list_size() == 0
