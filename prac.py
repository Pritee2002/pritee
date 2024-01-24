n=list(map(int,input().split()))
temp=[]
update=[]
for i in range(0,len(n)):
    if n[i]!=0:
        update.append(n[i])
    elif n[i]<1:
        temp.append(n[i])
print(update+temp)
    
