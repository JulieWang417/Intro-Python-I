"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
print('----FOO.txt -----')
foo = open('foo.txt', 'r')
print(foo.read())
foo.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

"""Create a txt file"""
bar = open("bar.txt", "w+")

"""Write 3 lines of code using a range"""
for n in range(3):
    bar.write("I love lambda school! %d\n" % (n+1))

    """
    \r, this is a carriage return. A carriage return returns the 
    cursor to the beginning of the same line, and \n is a newline character.
    a newline moves the cursor down by one line.
    """

"""Close the txt to save the changes"""
bar.close()

"""
Open the txt file
print the text inside sing 'read()'
and close the txt file
"""
bar = open('bar.txt', 'r')
print('----BAR.txt -----')
print(bar.read())
bar.close()