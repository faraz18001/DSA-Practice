"""
input=/home/
problem  we can't have path with ending / 

this should be removed

lets a stack 
stack=[]

for char in s:
    if char is not alphanumberic char.append stack


    stack.append(char)

stack=[/,/]





    '



"""


"""s='/home/'
stack=[]
result_stack=[]
seen=set()
for char in s:
    if not char.isalnum():
        stack.append(char)
#Remove duplicate chars
for char in result_stack:
        seen.add(char)

        result_stack.append(char)"""



    



"""
elements=['1','2','1',"2","3","4","5","6",]
seen=set()
result=[]
for i in elements:
    if i not in seen:
        seen.add(i)
        result.append(i)
ack:
    if char not in seen:
print(result)
"""


input_string='/home//user/'        
seprated_strings=input_string.split("/")
final_stack=[]
for char in seprated_strings:
    if char!="":
        final_stack.append(char)

print('/' + '/'.join(final_stack))



    



   
        






