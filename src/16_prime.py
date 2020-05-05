"""
Stretch Goals
One of Python's main philosophical tenets is its emphasis on readability.
 To that end, the Python community has standardized around a style guide called PEP 8. 
 Take a look at it and then go over the code you've written and make sure it adheres 
 to what PEP 8 recommends. Alternatively, PEP 8 linters exist for most code editors 
 (you can find instructions on installing a Python linter for VSCode here). 
 Try installing one for your editor!

Rewrite code challenges you've solved before or projects you've implemented before
 in a different language in Python. Start getting in as much practice with the
  language as possible!

Write a program to determine if a number, given on the command line, is prime.

How can you optimize this program?
Implement The Sieve of Eratosthenes, one of the oldest algorithms known (ca. 200 BC).
"""

"""
Input: number
Output: list of primes
"""
            


num = input('Write a number bigger than 0 to find if it is a prime: ')

def isPrime(num):
    if num > 1:  
        for i in range(2,num):  
            if (num % i) == 0:  
                print(num,"is not a prime number")  
                print(i,"times",num//i,"is",num)  
                break  
        else:  
            print(num,"is a prime number")  
         
    else:  
        print(num,"is not a prime number")  


isPrime(int(num))

