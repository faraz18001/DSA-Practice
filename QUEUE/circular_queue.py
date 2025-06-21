def create_circular_queue(size):
    circular_queue = [None] * size
    front = rear = -1

    def is_empty():
        return front == -1

    def is_full():
        return (rear + 1) % size == front

    def enqueue(item):
        if is_full():
            print("Queue is full")
            return False
        if is_empty():
            front = 0
        rear = (rear + 1) % size
        circular_queue[rear] = item
        return True

    def dequeue():
        if is_empty():
            raise IndexError("Dequeue from empty queue")
        item = circular_queue[front]
        if front == rear:  # Queue has only one element
            front = rear = -1
        else:
            front = (front + 1) % size
        return item

    def get_size():
        if is_empty():
            return 0
        return (rear - front + 1) % size + 1

    # Return a dictionary of operations to manipulate the circular queue
    return {
        "enqueue": enqueue,
        "dequeue": dequeue,
        "is_empty": is_empty,
        "is_full": is_full,
        "size": get_size
    }

# Example usage
queue_operations = create_circular_queue(5)
enqueue = queue_operations["enqueue"]
dequeue = queue_operations["dequeue"]
is_empty = queue_operations["is_empty"]
is_full = queue_operations["is_full"]
size = queue_operations["size"]

enqueue(10)
enqueue(20)
enqueue(30)
enqueue(40)
enqueue(50)

print(dequeue())  # Output: 10
print(dequeue())  # Output: 20

enqueue(60)

print(dequeue())  # Output: 30
print(dequeue())  # Output: 40
print(dequeue())  # Output: 50
print(dequeue())  # Output: 60
