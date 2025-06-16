"""
Input: /home/
Problem: We can't have path with ending /
This should be removed

Let's use a stack 
stack = []

For each character in string:
    If character is not alphanumeric, append to stack
    
    stack.append(char)

stack = [/, /]
"""

"""
s = '/home/'
stack = []
result_stack = []
seen = set()

for char in s:
    if not char.isalnum():
        stack.append(char)

# Remove duplicate chars
for char in result_stack:
        seen.add(char)
        result_stack.append(char)
"""

"""
Remove duplicates from list example:
"""
elements = ['1', '2', '1', "2", "3", "4", "5", "6"]
seen = set()
result = []

for i in elements:
    if i not in seen:
        seen.add(i)
        result.append(i)
        
# Note: There's some incomplete code here that was commented out
# ack:
#     if char not in seen:
        
#print(result)
"""
# Main path processing logic
input_string = '/home/user/../documents/'        
seprated_strings = input_string.split("/")
final_stack = []

# Add non-empty path components to stack
for char in seprated_strings:
    if char != "":
        final_stack.append(char)

# Handle '..' (parent directory) by removing last element
result_stack=[]
for char in final_stack:
    if char == '..':
        final_stack.pop()

for char in final_stack:
    if char !='.' or '..':
        result_stack.append(char)
    

# Reconstruct the path
print('/' + '/'.join(result_stack))"""


s="/home/user/Documents/../Pictures"
components=s.split('/')

final_stack=[]
for component in components:
    if component=='':
        pass

    elif component=="..":
        if len(final_stack)!=0:
            final_stack.pop()

    elif component=='.':
        pass

    else:
        final_stack.append(component)


print('/' + '/'.join(final_stack))







