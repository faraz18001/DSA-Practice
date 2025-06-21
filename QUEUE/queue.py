# Linear Queue Implementation without OOP using only Python Arrays and Variables

# Global variables to maintain queue state
queue_data = []
front = -1
rear = -1
max_size = 0

def create_queue(size):
    """Initialize a new linear queue with given size"""
    global queue_data, front, rear, max_size
    queue_data = [None] * size
    front = -1
    rear = -1
    max_size = size
    print(f"Queue created with size: {size}")

def is_empty():
    """Check if the queue is empty"""
    return front == -1

def is_full():
    """Check if the queue is full"""
    return rear == max_size - 1

def enqueue(item):
    """Add an item to the rear of the queue"""
    global front, rear
    
    if is_full():
        print("Queue overflow! Cannot enqueue.")
        return False
    
    if is_empty():
        front = 0
        rear = 0
    else:
        rear += 1
    
    queue_data[rear] = item
    print(f"Enqueued: {item}")
    return True

def dequeue():
    """Remove and return an item from the front of the queue"""
    global front, rear
    
    if is_empty():
        print("Queue underflow! Cannot dequeue.")
        return None
    
    item = queue_data[front]
    queue_data[front] = None  # Clear the slot
    
    # If queue becomes empty after this operation
    if front == rear:
        front = -1
        rear = -1
    else:
        front += 1
    
    print(f"Dequeued: {item}")
    return item

def peek_front():
    """Return the front item without removing it"""
    if is_empty():
        print("Queue is empty!")
        return None
    return queue_data[front]

def peek_rear():
    """Return the rear item without removing it"""
    if is_empty():
        print("Queue is empty!")
        return None
    return queue_data[rear]

def display_queue():
    """Display the current state of the queue"""
    if is_empty():
        print("Queue is empty")
        return
    
    print(f"Queue array: {queue_data}")
    print(f"Front index: {front}, Rear index: {rear}")
    
    # Show actual queue elements
    elements = []
    for i in range(front, rear + 1):
        elements.append(queue_data[i])
    
    print(f"Queue elements (front to rear): {elements}")
    print(f"Available space: {max_size - (rear + 1)} slots")

def get_current_size():
    """Get the current number of elements in the queue"""
    if is_empty():
        return 0
    return rear - front + 1

def get_capacity():
    """Get the maximum capacity of the queue"""
    return max_size

def clear_queue():
    """Clear all elements from the queue"""
    global front, rear
    front = -1
    rear = -1
    for i in range(max_size):
        queue_data[i] = None
    print("Queue cleared")

# Alternative implementation using local arrays (function-based approach)
def demo_local_array_queue():
    """Demonstrate queue operations using local arrays"""
    print("\n=== Local Array Queue Demo ===")
    
    # Local variables
    size = 4
    data = [None] * size
    f = -1  # front
    r = -1  # rear
    
    def local_enqueue(arr, front_idx, rear_idx, item, capacity):
        if rear_idx == capacity - 1:
            print(f"Cannot enqueue {item} - Queue is full")
            return front_idx, rear_idx, False
        
        if front_idx == -1:
            front_idx = 0
            rear_idx = 0
        else:
            rear_idx += 1
            
        arr[rear_idx] = item
        print(f"Enqueued: {item}")
        return front_idx, rear_idx, True
    
    def local_dequeue(arr, front_idx, rear_idx):
        if front_idx == -1:
            print("Cannot dequeue - Queue is empty")
            return front_idx, rear_idx, None
        
        item = arr[front_idx]
        arr[front_idx] = None
        
        if front_idx == rear_idx:
            front_idx = -1
            rear_idx = -1
        else:
            front_idx += 1
            
        print(f"Dequeued: {item}")
        return front_idx, rear_idx, item
    
    # Test local array queue
    print(f"Created local queue with size: {size}")
    print(f"Initial array: {data}")
    
    # Enqueue operations
    f, r, _ = local_enqueue(data, f, r, "X", size)
    f, r, _ = local_enqueue(data, f, r, "Y", size)
    f, r, _ = local_enqueue(data, f, r, "Z", size)
    print(f"After enqueues - Array: {data}, Front: {f}, Rear: {r}")
    
    # Dequeue operations
    f, r, item = local_dequeue(data, f, r)
    print(f"After dequeue - Array: {data}, Front: {f}, Rear: {r}")
    
    # More operations
    f, r, _ = local_enqueue(data, f, r, "W", size)
    f, r, _ = local_enqueue(data, f, r, "V", size)  # This should fail (demonstrate false full)
    print(f"Final state - Array: {data}, Front: {f}, Rear: {r}")

# Example usage and testing
if __name__ == "__main__":
    print("=== Simple Linear Queue Demo (Global Variables) ===")
    
    # Create a queue with capacity of 5
    create_queue(5)
    
    print(f"Is empty: {is_empty()}")
    print(f"Is full: {is_full()}")
    
    print("\n--- Enqueue Operations ---")
    enqueue("A")
    enqueue("B")
    enqueue("C")
    display_queue()
    
    print(f"\nFront element: {peek_front()}")
    print(f"Rear element: {peek_rear()}")
    print(f"Current size: {get_current_size()}")
    
    print("\n--- Fill the queue ---")
    enqueue("D")
    enqueue("E")
    display_queue()
    
    print(f"\nIs full: {is_full()}")
    
    # Try to enqueue when full
    print("\n--- Trying to enqueue when full ---")
    enqueue("F")
    
    print("\n--- Dequeue Operations ---")
    dequeue()
    dequeue()
    display_queue()
    
    print(f"Current size: {get_current_size()}")
    
    # Demonstrate the "false full" problem
    print("\n--- Demonstrating 'False Full' Problem ---")
    enqueue("F")  # This will fail because rear is at the end
    
    print("\n--- Clear and restart ---")
    clear_queue()
    display_queue()
    
    # Test with new elements
    enqueue("NEW1")
    enqueue("NEW2")
    display_queue()
    
    print("\n--- Dequeue all remaining elements ---")
    while not is_empty():
        dequeue()
    
    display_queue()
    
    # Try to dequeue when empty
    print("\n--- Trying to dequeue when empty ---")
    dequeue()
    
    # Demonstrate local array approach
    demo_local_array_queue()