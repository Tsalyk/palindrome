"""
Palindrome class realization.
"""

# from Stack.arraystack import ArrayStack

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

    def find_palindromes(self, readFrom: str, writeTo: str) -> None:
        """
        Finds all palindromes from the file and
        write it into another one
        """
        words = self.read_file(readFrom)
        pass
