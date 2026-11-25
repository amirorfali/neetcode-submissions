class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            #print(stack)
            #print(f'i: {i}')
            if tokens[i] in '+-/*':
                a=stack.pop()
                b=stack.pop()
                if tokens[i]=='+':
                    stack.append(int(a+b))

                elif tokens[i]=='-':
                    stack.append(int(b-a))

                elif tokens[i]=='*':
                    stack.append(int(a*b))

                elif tokens[i]=='/':
                    stack.append(int(b/a))
            else:
                stack.append(int(tokens[i]))
        return stack[0]  
        
        
        