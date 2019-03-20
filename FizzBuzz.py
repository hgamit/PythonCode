'''
Fizz Buzz - Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” 
instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three 
and five print “FizzBuzz”.
'''

if __name__ == '__main__':
    for i in range(1, 101):
        if i % 3 == 0:
            if i % 5 == 0:
                print ("FizzBuzz")
            else:
                print ("Fizz", end="| ")
        elif i % 5 == 0:
            print ("Buzz", end="| ")
        else:
            print (i, end="| ")
