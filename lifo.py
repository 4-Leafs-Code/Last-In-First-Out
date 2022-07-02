class LIFO(object):
    def __init__(self):
        self.items = []
        self.popped = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop(-1)

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items

    def size(self):
        return len(self.items)


s = LIFO()
choice = ""
while choice != "5":
    print("""
    1. Push
    2. Pop
    3. Peek
    4. Size
    5. Quit """)
    choice = input("Enter your choice: ")
    if choice == "1":
        item = input("Enter item to push: ")
        s.push(item)
        print("Stack Items:", s.peek())
    elif choice == "2":
        item = s.items.pop()
        s.popped.append(item)
        print("Stack Items:", s.peek())
    elif choice == "3":
        print("Peek: " + s.peek())
    elif choice == "4":
        print("Size: " + str(s.size()))
    elif choice == "5":
        print("Popped: " + str(s.popped))
        break
    else:
        print("Invalid choice")
