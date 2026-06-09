# Stack
stack = []
def push(insert):
    stack.append(insert)
    print("Pushed element: ", insert)

def pop():
    if stack != []:
        print("Element poped: ", stack[-1])
        del(stack[-1])
    else:
        print("Stack is empty")

def traverse():
    i = 0
    while stack != [] and i < len(stack):
        print(stack[i], end = " ")
        i += 1
    if stack == []:
        print("Stack is empty")

def search(element):
    if element in stack:
        print("Element found at index: ", stack.index(element))
    else:
        print("Element not found")

# Start
while  True:
    choice = int(input("\n1 or 2 or 3 or 4: "))
    if choice == 1:
        push(insert = input("New element: "))
    elif choice == 2:
        pop()
    elif choice == 3:
        traverse()
    elif choice == 4:
        element = input("Element to search: ")
        search(element)
    else:
        print("Exiting program")
        break

# stack = ['2', '3', '4', '5']
# print(stack)

# del(stack[-1])
# print("New stack", stack)

# print(stack)
