count=0
inp = str(input("Enter the expression :\t"))
for x in range(len(inp)):
    if inp[x]=='(':
        count+=1
    if inp[x]==')':
        count-=1

if count==0:
    print("The expression is balanced.")
else:
    print("The expression is not balanced.")