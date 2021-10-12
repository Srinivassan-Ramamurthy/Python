a=int(input('Enter a number '))
b=int(input('Enter a number '))
c=int(input('Enter a number '))
if(a>b and a>c):
    print(f'{a} is greater')
    if(b>c):
        print(f'{c} is smaller')
    else:
        print(f'{b} is smaller')
elif(b>c):
    print(f'{b} is greater')
    if(a>c):
        print(f'{c} is smaller')
    else:
        print(f'{a} is smaller')
else:
    print(f'{c} is greater')
    if(a>b):
        print(f'{b} is smaller')
    else:
        print(f'{a} is smaller')
    
    
    
    
      
        


