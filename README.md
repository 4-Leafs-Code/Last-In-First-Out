# Last-In-First-Out

Create and test a Stack class to represent a "last-in, first-out" stack (commonly referred to as a LIFO stack). Your stacks should support the following methods:   

__init__(self)	Create an empty stack using a Python list
isEmpty(self)	Check to see if stack is empty, returns true if stack is empty
push(self, item)	Pushes the item onto the top of the stack.
pop(self)	Removes the top-most item from the stack and returns it.
peek(self)	Examines the stack returning a list of items on the stack
size(self)	Returns a count of the number of items in the stack.

Test your class by writing code to add several items to a stack and then pop them off one at a time. Verify that the most recent items are 
popped off the stack first

In the main module:

Create a stack called s.
Write a loop that will prompt the user to push a value on the stack, pop a value from the stack, or quit.
When an item is pushed or popped from the stack print the contents of the stack.
Maintain a list of the items popped from the list and print that list when the user quits
Perform the following operations on your stack

push 34
push 45
push 3
push 90
pop
pop
push 5
pop
pop
pop
quit
