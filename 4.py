n=int(input())
i=0
l=[]
while n:
    a=n%10
    n=n//10
    l.append(str(a)+'*10^'+str(i))
    i+=1
print('+'.join(l[::-1]))