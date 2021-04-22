"""
Palindrome class realization.
"""
from arraystack import ArrayStack


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
