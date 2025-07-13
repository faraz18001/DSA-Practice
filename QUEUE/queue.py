# Simple Linear Queue - Basic Enqueue and Dequeue only

def create_queue(size):
    """Create a new queue and return initial state"""
    data = [None] * size
    front = -1
    rear = -1
    return data, front, rear, size

def enqueue(data, front, rear, size, item):
    """Add item to queue"""
    if rear == size - 1:
        print("Queue is full!")
        return data, front, rear
    
    if front == -1:
        front = 0
        rear = 0
    else:
        rear += 1
    
    data[rear] = item
    return data, front, rear

def dequeue(data, front, rear):
    """Remove item from queue"""
    if front == -1:
        print("Queue is empty!")
        return data, front, rear, None
    
    item = data[front]
    
    if front == rear:
        front = -1
        rear = -1
    else:
        front += 1
    
    return data, front, rear, item

# Example usage
if __name__ == "__main__":
    # Create queue
    data, front, rear, size = create_queue(5)
    
    # Add items
    data, front, rear = enqueue(data, front, rear, size, "A")
    data, front, rear = enqueue(data, front, rear, size, "B")
    data, front, rear = enqueue(data, front, rear, size, "C")
    
    print(f"Queue: {data}")
    print(f"Front: {front}, Rear: {rear}")
    
    # Remove items
    data, front, rear, item = dequeue(data, front, rear)
    print(f"Removed: {item}")
    
    data, front, rear, item = dequeue(data, front, rear)
    print(f"Removed: {item}")
    
    print(f"Queue: {data}")
    print(f"Front: {front}, Rear: {rear}")