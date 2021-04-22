"""
Palindrome class realization.
"""
from arrays import Array, ArrayExpanded
from abstractstack import AbstractStack


class ArrayStack(AbstractStack):
    """An array-based stack implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = ArrayExpanded(ArrayStack.DEFAULT_CAPACITY)
        AbstractStack.__init__(self, sourceCollection)

    def __iter__(self):
        """Supports iteration over a view of self.
        Visits items from bottom to top of stack."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def peek(self):
        """Returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if stack is empty."""
        if self.isEmpty():
            raise KeyError("The stack is empty")
        return self._items[len(self) - 1]

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)

    def push(self, item):
        """Inserts item at top of the stack."""
        if len(self) == len(self._items):

            self._items.grow()

        self._items[len(self)] = item
        self._size += 1

    def pop(self):
        """Removes and returns the item at the top of the stack.
        Precondition: the stack is not empty.
        Raises: KeyError if stack is empty.
        Postcondition: the top item is removed from the stack."""
        if self.isEmpty():
            raise KeyError("The stack is empty")
        oldItem = self._items[len(self) - 1]
        self._size -= 1
        # Resize the array here if necessary
        if len(self) <= len(self._items) // 4 and \
           len(self._items) >= 2 * ArrayStack.DEFAULT_CAPACITY:
            #temp = Array(len(self._items) // 2)
            #for i in range(len(self)):
            #    temp [i] = self._items[i]
            #self._items = temp
            self._items.shrink()
        return oldItem


class Palindrome:
    """
    Represents a palindrome object, using which allows to find
    all palindromes from one file and rewrite it into another one
    """
    def read_file(self, path: str) -> list:
        """
        Returns a list with data from the file
        """
        with open(path, "r", encoding="utf-8") as file:
            return list(map(lambda word: word.split()[0], file.readlines()))

    def write_in_file(self, path: str, palindromes: list) -> None:
        """
        Writes the data in the file
        """
        with open(path, "w", encoding="utf-8") as file:
            file.write("\n".join(palindromes))

    def find_palindromes(self, read_from: str, write_to: str) -> list:
        """
        Finds all palindromes from the file and
        write it into another one
        Returns a list with palindromes
        """
        words = self.read_file(read_from)
        palindromes = list()
        stack_with_words = ArrayStack()
        reversed_word = ""

        for word in words:
            for char in word:
                stack_with_words.push(char)

            while not stack_with_words.isEmpty():
                reversed_word += stack_with_words.pop()

            if reversed_word == word:
                palindromes.append(word)

            reversed_word = ""

        self.write_in_file(write_to, palindromes)

        return palindromes
