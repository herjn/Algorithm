#[후위 표기식]- Gold 4

n=input()
stack=[]; res=''

for x in n:
    if x.isalpha(): #피연산자 확인
        res+=x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x =='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                res+=stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                res+=stack.pop()
            stack.pop()
         
while stack:
    res += stack.pop()
print(res)