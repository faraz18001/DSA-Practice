# Hash Table Implementation without OOP

def create_hash_table(size=7):
    """Create a new hash table with given size"""
    return [None] * size

def hash_function(key, table_size):
    """Hash function to compute index for a given key"""
    my_hash = 0
    for letter in key:
        my_hash = (my_hash + ord(letter) * 23) % table_size
    return my_hash

def set_item(hash_table, key, value):
    """Insert a key-value pair in the hash table"""
    index = hash_function(key, len(hash_table))
    
    if hash_table[index] is None:
        hash_table[index] = []
    
    hash_table[index].append([key, value])

# Example usage:
if __name__ == "__main__":
    # Create hash table
    my_table = create_hash_table(7)
    
    # Add some items
    set_item(my_table, "grapes", 10000)
    set_item(my_table, "apples", 54)
    set_item(my_table, "oranges", 99)
    
    # Display table
    for i in range(len(my_table)):
        print(f"Index {i}: {my_table[i]}"))