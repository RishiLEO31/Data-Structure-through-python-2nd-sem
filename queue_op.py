# Queue
queue = []
def enqueue(item):
    queue.append(item)
    print(f"Enqueued: {item}")

def dequeue():
    if queue:
        item = queue.pop(0)
        print(f"Dequeued: {item}")
    else:
        print("Queue is empty")

def display_queue():
    if queue == []:
        print("Queue is empty")
    else:
        print("Current Queue:", queue)

while True:
    command = input("Enter command (enqueue/dequeue/display/exit): ")
    if command == "1":
        item = input("Enter item to enqueue: ")
        enqueue(item)
    elif command == "2":
        dequeue()
    elif command == "3":
        display_queue()
    else:
        print("Exiting...")
        break
