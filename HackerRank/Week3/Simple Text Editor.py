# Enter your code here. Read input from STDIN. Print output to STDOUT
q = int(input())
s=""
history=[]

for i in range(q):
    parts=input().split()
    op=parts[0]
    
    if op=="1":
        history.append(s)
        s+=parts[1]
        
    elif op=="2":
        history.append(s)
        k=int(parts[1])
        s=s[:-k]
        
    elif op=="3":
        k=int(parts[1])
        print(s[k-1])
        
    elif op=="4":
        s=history.pop()
            
