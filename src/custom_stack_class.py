class StackEmptyException(Exception):
    pass

class StackFullException(Exception):
    pass

class CustomStack:

    def __init__(self, pLimit):
        self.limit = pLimit
        self.elements = []
    
    def size(self):
        return len(self.elements)

    def is_empty(self):
        return self.size() == 0

    def push(self, element):
        if self.size() == self.limit:
            raise StackFullException()
        self.elements.append(element)
    
    def pop(self):
        if self.is_empty():
            raise StackEmptyException()
        return self.elements.pop()
    
    def top(self):
        if self.is_empty():
            raise StackEmptyException()
        return self.elements[-1]

# ----------------------------------------------- #

class NumberAscOrder:

    def sort(self, stack: CustomStack) -> list:
        if stack.is_empty():
            raise ValueError("Pilha está vazia sem numéros para ordenar com Sort")

        result = []
        while not stack.is_empty():
            result.append(stack.pop())

        return sorted(result)