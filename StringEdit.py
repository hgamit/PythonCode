from urllib.request import urlopen
from bs4 import BeautifulSoup

class StringEdit():

    def horoscope(self, sign):
        url = 'http://my.horoscope.com/astrology/free-daily-horoscope-%s.html' % sign
        page = urlopen(url)
        soup = BeautifulSoup(page, "html.parser")
        text = soup.p.text
        print("%s - %s" % (sign.capitalize(), text))

    def fizzbuzz(self, num):
        for i in range(1, num):
            if i % 3 == 0:
                if i % 5 == 0:
                    print("FizzBuzz")
                else:
                    print("Fizz", end="| ")
            elif i % 5 == 0:
                print("Buzz", end="| ")
            else:
                print(i, end="| ")

    def reverse(self, some_seq):
        """
            Input:     Sequence
            output:    Sequence:
                         reversed version
        """
        return some_seq[::-1]

    def count_vowels(self, string):
        """
            @param string:   String
            @return:         Integer:
                                No. of vowels or 0
        """
        vowels = "aeiou"
        count = {char: 0 for char in vowels}
        for char in string:
            if char in vowels:
                count[char] += 1
        return count

    def is_palindrome(self, some_seq):
        """
            @param some_seq: sequence of anything
            @return:         Boolean:
                        palindrome check of sequence passed
        """
        return some_seq == self.reverse(some_seq)

    def count_words(self, string=None, file=None):
        """
            @param string:    A string
            @param file:      A file to be read
        """
        word_count = 0
        if string:
            word_count = len(string.split())
        if file:
            with open(file) as f:
                word_count = len(f.read().split())
        return word_count

    #A lambda function is a small anonymous function.
    #Syntax --  lambda arguments : expression


    def find_in_iter(self, some_iter):
        if isinstance(some_iter, str):
            cond = lambda sequence, string: [char for char in string if char in sequence]
            vowels = ("a,e,i,o,u")
            return [word for word in some_iter.lower().split(" ") if len(cond(vowels, word)) > 1]
        elif isinstance(some_iter[0], int):
            return [num for num in some_iter if num > 5]

    def piglatin(self, string):
        """
        Pig Latin – Pig Latin is a game of alterations played on the English language game.
        To create the Pig Latin form of an English word the initial consonant sound is transposed
        to the end of the word and an ay is affixed
        (Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules.
        """
        words = []
        vowels = 'aeiou'
        for word in string.split():
            if len(word) > 2 and word[0] not in vowels:
                words.append(word[1:] + '-' + word[0] + 'ay')
            else:
                words.append(word + '-ay')
        return ' '.join(words)


if __name__ == '__main__':
    s = StringEdit()
    print("Printing Fizzbuzz:")
    s.fizzbuzz(21)
    text = "what is going on?" #str(input("String to process? "))

    print("\n\nText: ", text)
    print("\nVowels count: ", s.count_vowels(text))
    print("\nReverse text: ", s.reverse(text))
    print("\nPigLatin text: ", s.piglatin(text))
    print("\nIs palindrome?: ", s.is_palindrome(text))
    print("\nWord Count: ", s.count_words(text))
    print("\nHoroscope: ")
    s.horoscope("cancer")
    #word = s.find_in_iter(text)
    #num = s.find_in_iter(range(10))
    #print(word, '\n', num)
