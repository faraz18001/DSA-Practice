# Circular Queue Implementation without OOP using Python Arrays

def create_queue(size):
    """Create a new circular queue with given size"""
    return {
        'data': [None] * size,
        'front': -1,
        'rear': -1,
        'size': size,
        'count': 0
    }

def is_empty(queue):
    """Check if the queue is empty"""
    return queue['count'] == 0

def is_full(queue):
    """Check if the queue is full"""
    return queue['count'] == queue['size']

def enqueue(queue, item):
    """Add an item to the rear of the queue"""
    if is_full(queue):
        print("Queue is full! Cannot enqueue.")
        return False
    
    if is_empty(queue):
        queue['front'] = 0
        queue['rear'] = 0
    else:
        queue['rear'] = (queue['rear'] + 1) % queue['size']
    
    queue['data'][queue['rear']] = item
    queue['count'] += 1
    print(f"Enqueued: {item}")
    return True

def dequeue(queue):
    """Remove and return an item from the front of the queue"""
    if is_empty(queue):
        print("Queue is empty! Cannot dequeue.")
        return None
    
    item = queue['data'][queue['front']]
    queue['data'][queue['front']] = None  # Clear the slot
    
    if queue['count'] == 1:
        # Queue becomes empty
        queue['front'] = -1
        queue['rear'] = -1
    else:
        queue['front'] = (queue['front'] + 1) % queue['size']
    
    queue['count'] -= 1
    print(f"Dequeued: {item}")
    return item

def peek_front(queue):
    """Return the front item without removing it"""
    if is_empty(queue):
        print("Queue is empty!")
        return None
    return queue['data'][queue['front']]

def peek_rear(queue):
    """Return the rear item without removing it"""
    if is_empty(queue):
        print("Queue is empty!")
        return None
    return queue['data'][queue['rear']]

def display_queue(queue):
    """Display the current state of the queue"""
    if is_empty(queue):
        print("Queue is empty")
        return
    
    print(f"Queue state: {queue['data']}")
    print(f"Front index: {queue['front']}, Rear index: {queue['rear']}")
    print(f"Count: {queue['count']}/{queue['size']}")
    
    # Show actual queue elements in order
    elements = []
    if not is_empty(queue):
        i = queue['front']
        for _ in range(queue['count']):
            elements.append(queue['data'][i])
            i = (i + 1) % queue['size']
    
    print(f"Queue elements (front to rear): {elements}")

def get_size(queue):
    """Get the current number of elements in the queue"""
    return queue['count']

def get_capacity(queue):
    """Get the maximum capacity of the queue"""
    return queue['size']

# Example usage and testing
if __name__ == "__main__":
    print("=== Circular Queue Demo ===")
    
    # Create a queue with capacity of 5
    q = create_queue(5)
    
    print(f"Queue created with capacity: {get_capacity(q)}")
    print(f"Is empty: {is_empty(q)}")
    print(f"Is full: {is_full(q)}")
    
    print("\n--- Enqueue Operations ---")
    enqueue(q, 10)
    enqueue(q, 20)
    enqueue(q, 30)
    display_queue(q)
    
    print(f"\nFront element: {peek_front(q)}")
    print(f"Rear element: {peek_rear(q)}")
    
    print("\n--- More Enqueue Operations ---")
    enqueue(q, 40)
    enqueue(q, 50)
    display_queue(q)
    
    print(f"\nIs full: {is_full(q)}")
    
    # Try to enqueue when full
    print("\n--- Trying to enqueue when full ---")
    enqueue(q, 60)
    
    print("\n--- Dequeue Operations ---")
    dequeue(q)
    dequeue(q)
    display_queue(q)
    
    print("\n--- Enqueue after dequeue (circular behavior) ---")
    enqueue(q, 60)
    enqueue(q, 70)
    display_queue(q)
    
    print("\n--- Dequeue all elements ---")
    while not is_empty(q):
        dequeue(q)
    
    display_queue(q)
    
    # Try to dequeue when empty
    print("\n--- Trying to dequeue when empty ---")
    dequeue(q)