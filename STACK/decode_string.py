"""
sample_input=3[a]2[bc]
3*a + 2*bc = aaa + bcbc = aaabcbc

sample_input#2=3[a2[c]]
deal with nested brackets first
2*c = cc, then a+cc = acc, then 3*acc = aaacccccc

sample_input#3=2[abc]3[cd]ef
2*abc + 3*cd + ef = abcabc + cdcdcd + ef = abcabccdcdcdef

general steps
1. loop through the string
2. push stuff (numbers, letters, brackets) onto a stack until we hit a closing bracket
3. when we see ']', pop letters to build a substring, pop '[', then pop digits to get the number
4. multiply the substring by the number and push it back to the stack
5. at the end, join everything in the stack to get the final string

how do we utilize stack?
stack=[]
s="3[a]2[bc]"
final_string=''

for char in s:
    if char isn’t ']', we just push it to the stack
    so for '3', '[', 'a', stack = ['3', '[', 'a']

    when we hit ']', we start popping:
    - pop until we hit '[' to build the substring (e.g., 'a')
    - pop the '['
    - pop digits to build the number (e.g., '3')
    - multiply substring by number (3*a = 'aaa') and push it back

stack now has ['aaa']
loop continues, we hit '2', push it, stack = ['aaa', '2']
then '[', push it, stack = ['aaa', '2', '[']
then 'b', 'c', push them, stack = ['aaa', '2', '[', 'b', 'c']

hit ']' again:
    - pop 'c', 'b' to build substring 'bc' (note: we reverse as we pop)
    - pop '['
    - pop '2' to get number
    - multiply 2*bc = 'bcbc', push it back
stack = ['aaa', 'bcbc']

string ends, join stack to get 'aaabcbc'

for nested case like 3[a2[c]]:
- same deal, but inner bracket 2[c] gets processed first
- when we hit ']' for 2[c], stack has ['3', '[', 'a', '2', '[', 'c']
- pop 'c', build 'c', pop '[', pop '2', get 2*c = 'cc'
- push 'cc', stack = ['3', '[', 'a', 'cc']
- then process outer bracket, pop 'cc', 'a' for substring 'acc', pop '[', pop '3'
- get 3*acc = 'aaacccccc'

stack keeps track of numbers, brackets, and letters, and we build the string step-by-step!
"""


def decodeString(s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s[i]!=']':
                stack.append(s[i])

            else:
                substring=''
                while stack[-1]!='[':
                    substring=stack.pop()+substring
                stack.pop()



                k=''
                while len(stack)!=0 and stack[-1].isdigit():
                    k=stack.pop()+k

                stack.append(int(k)*substring)



        return ''.join(stack)

s="3[a]2[bc]"
res=decodeString(s)
print(res)








