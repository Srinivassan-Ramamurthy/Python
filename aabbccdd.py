a=input('Enter input').strip()
count=1
for i in range(len(a)-1):
    if(a[i]==a[i+1]):
        count+=1
    else:
        print(a[i],end='')
        print(count,end='')
        count=1
print(a[-1],end='')
print(count)
        
        
