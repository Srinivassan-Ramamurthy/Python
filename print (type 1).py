a=input()
x=a.split()
y=int(x[0])
z=int(x[2])
if(x[1]=='+'):
    print(y+z)
if(x[1]=='-'):
    print(y-z)
if(x[1]=='*'):
    print(y*z)
if(x[1]=='/'):
    print(y/z)
