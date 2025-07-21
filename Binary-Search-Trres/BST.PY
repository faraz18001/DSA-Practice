def contains(self,current_node,value):
    if current_node is None:#Base Case
        return False
    
    if value==current_node.value:
        return True
    
    if value<current_node.value:
        return contains(current_node.left,value)
    
    if value>current_node.value:
        return contains(current_node.right,value)


def insert_node(self,current_node,value):
    if current_node.value==None:
        return Node(value)
    
    if value<current_node.value:
        current_node.left=insert_node(current_node.left,value)
        
    if value>current_node.value:
        current_node.left=insert_node(current_node.right,value)    
        
    return current_node
        
        

def delete_node(self,current_node,value):
    